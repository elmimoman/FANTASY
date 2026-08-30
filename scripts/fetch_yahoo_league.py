#!/usr/bin/env python3
"""
Trae los datos crudos de tu liga de Yahoo Fantasy (NFL): ligas disponibles,
configuración, equipos y rosters. Guarda todo en JSON tal cual lo devuelve
Yahoo — se procesa después (el formato de Yahoo es bastante enredado por
venir originalmente de XML).

Requiere haber corrido antes yahoo_auth.py una vez (guarda el token en
scripts/.yahoo_tokens.json).

Uso:
    # Paso 1: listar tus ligas de NFL para encontrar el league_key
    python3 fetch_yahoo_league.py --list_leagues

    # Paso 2: con el league_key ya identificado (ej. 449.l.123456)
    python3 fetch_yahoo_league.py --league_key 449.l.123456

No requiere instalar nada más: solo Python 3 (librería estándar).
"""
import argparse
import base64
import json
import os
import urllib.parse
import urllib.request

BASE = "https://fantasysports.yahooapis.com/fantasy/v2"
TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"
TOKENS_PATH = os.path.join(os.path.dirname(__file__), ".yahoo_tokens.json")


def load_tokens():
    with open(TOKENS_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_tokens(tokens):
    with open(TOKENS_PATH, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2)


def refresh_access_token(tokens):
    auth_header = base64.b64encode(f'{tokens["client_id"]}:{tokens["client_secret"]}'.encode()).decode()
    data = urllib.parse.urlencode(
        {
            "grant_type": "refresh_token",
            "redirect_uri": "https://localhost:8080",
            "refresh_token": tokens["refresh_token"],
        }
    ).encode()
    req = urllib.request.Request(
        TOKEN_URL,
        data=data,
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        new_tokens = json.load(r)
    tokens.update(new_tokens)
    save_tokens(tokens)
    return tokens


def api_get(path, access_token):
    url = f"{BASE}/{path}"
    sep = "&" if "?" in url else "?"
    url = f"{url}{sep}format=json"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def list_leagues(access_token):
    data = api_get("users;use_login=1/games;game_keys=nfl/leagues", access_token)
    out_path = "yahoo_leagues.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Guardado en {out_path}.")
    print("Buscá adentro los campos 'league_key' y 'name' para identificar tu liga,")
    print("o mandale el archivo directo a Claude para que lo lea.")


def fetch_league(league_key, access_token, out_prefix):
    result = {}

    result["settings"] = api_get(f"league/{league_key}/settings", access_token)
    result["standings"] = api_get(f"league/{league_key}/standings", access_token)
    result["teams"] = api_get(f"league/{league_key}/teams", access_token)

    # Rosters: hay que pedirlos por equipo. Sacamos los team_key de la respuesta de teams
    # de forma tolerante (la estructura de Yahoo es una lista con índices como string).
    team_keys = []
    try:
        teams_blob = result["teams"]["fantasy_content"]["league"][1]["teams"]
        for k, v in teams_blob.items():
            if k == "count":
                continue
            team_fields = v["team"][0]
            for field in team_fields:
                if isinstance(field, dict) and "team_key" in field:
                    team_keys.append(field["team_key"])
    except Exception as e:
        print(f"No se pudieron extraer los team_keys automáticamente ({e}).")
        print("Igual quedó todo guardado en crudo — Claude puede sacarlos del JSON.")

    rosters = {}
    for tk in team_keys:
        try:
            rosters[tk] = api_get(f"team/{tk}/roster", access_token)
        except Exception as e:
            rosters[tk] = {"error": str(e)}

    result["rosters"] = rosters

    # Jugadores libres (free agents) de la liga, primeras 100 (paginado de a 25)
    free_agents = []
    for start in range(0, 100, 25):
        try:
            fa = api_get(f"league/{league_key}/players;status=FA;start={start};count=25", access_token)
            free_agents.append(fa)
        except Exception as e:
            free_agents.append({"error": str(e), "start": start})
    result["free_agents"] = free_agents

    out_path = f"{out_prefix}_raw.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Listo. Todo guardado en {out_path} ({len(team_keys)} equipos encontrados).")
    print("Pasale este archivo a Claude para que lo procese y arme el dashboard.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list_leagues", action="store_true", help="Lista tus ligas de NFL para encontrar el league_key")
    parser.add_argument("--league_key", help="El league_key de tu liga, ej. 449.l.123456")
    parser.add_argument("--out", default="yahoo_liga", help="Prefijo del archivo de salida")
    args = parser.parse_args()

    tokens = load_tokens()
    tokens = refresh_access_token(tokens)
    access_token = tokens["access_token"]

    if args.list_leagues:
        list_leagues(access_token)
        return

    if not args.league_key:
        parser.error("Pasá --list_leagues o --league_key")

    fetch_league(args.league_key, access_token, args.out)


if __name__ == "__main__":
    main()
