#!/usr/bin/env python3
"""
Trae los datos de tu liga de Sleeper (NFL Fantasy): configuración de puntuación,
posiciones de roster, y tu equipo actual con nombres de jugadores legibles.

La API de Sleeper es pública, no necesita login ni token.

Uso:
    # Si no sabés tu league_id, buscá tus ligas por username:
    python3 fetch_sleeper_league.py --username TU_USUARIO_DE_SLEEPER

    # Con el league_id ya identificado (te lo imprime el comando de arriba):
    python3 fetch_sleeper_league.py --league_id 123456789012345678

No requiere instalar nada: solo Python 3 (librería estándar).
"""
import argparse
import csv
import json
import urllib.request

BASE = "https://api.sleeper.app/v1"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def current_season():
    return get(f"{BASE}/state/nfl")["season"]


def list_leagues(username, season):
    user = get(f"{BASE}/user/{username}")
    leagues = get(f"{BASE}/user/{user['user_id']}/leagues/nfl/{season}")
    print(f"Ligas de {username} para la temporada {season}:\n")
    for lg in leagues:
        print(f"  league_id={lg['league_id']}  nombre=\"{lg['name']}\"  equipos={lg['total_rosters']}")
    print("\nCorré de nuevo con: python3 fetch_sleeper_league.py --league_id <el que quieras>")


def fetch_league(league_id, out_prefix):
    league = get(f"{BASE}/league/{league_id}")
    rosters = get(f"{BASE}/league/{league_id}/rosters")
    users = get(f"{BASE}/league/{league_id}/users")
    players = get(f"{BASE}/players/nfl")  # diccionario completo de la NFL, ~5MB

    config = {
        "name": league["name"],
        "season": league["season"],
        "scoring_settings": league["scoring_settings"],
        "roster_positions": league["roster_positions"],
        "total_rosters": league["total_rosters"],
    }
    config_path = f"{out_prefix}_config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"Config guardada en {config_path}")

    user_by_id = {u["user_id"]: u.get("display_name", u["user_id"]) for u in users}

    rows = []
    for roster in rosters:
        owner = user_by_id.get(roster.get("owner_id"), "?")
        starters = set(roster.get("starters") or [])
        for pid in (roster.get("players") or []):
            p = players.get(pid, {})
            rows.append(
                {
                    "equipo_fantasy": owner,
                    "jugador": p.get("full_name", pid),
                    "posicion": p.get("position", ""),
                    "equipo_nfl": p.get("team", ""),
                    "estado_lesion": p.get("injury_status", "") or "",
                    "titular": pid in starters,
                }
            )

    rosters_path = f"{out_prefix}_rosters.csv"
    with open(rosters_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Rosters guardados en {rosters_path} ({len(rows)} jugadores)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", help="Tu username de Sleeper, para listar tus ligas")
    parser.add_argument("--league_id", help="El league_id de tu liga")
    parser.add_argument("--out", default="sleeper", help="Prefijo de los archivos de salida")
    args = parser.parse_args()

    if not args.username and not args.league_id:
        parser.error("Pasá --username o --league_id")

    season = current_season()

    if args.username:
        list_leagues(args.username, season)
        return

    fetch_league(args.league_id, args.out)


if __name__ == "__main__":
    main()
