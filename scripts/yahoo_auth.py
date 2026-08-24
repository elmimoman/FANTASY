#!/usr/bin/env python3
"""
Login de una sola vez contra la API de Yahoo Fantasy Sports (OAuth2).

ANTES de correr esto, registrá una app en Yahoo:
  1. Andá a https://developer.yahoo.com/apps/create/
  2. Nombre: lo que quieras (ej. "Mi Fantasy NFL")
  3. Homepage URL: cualquiera, ej. https://example.com
  4. Redirect URI(s): oob
  5. API Permissions: marcá "Fantasy Sports" con acceso "Read"
  6. Creá la app y copiá el "Client ID (Consumer Key)" y "Client Secret (Consumer Secret)"

Uso:
    python3 yahoo_auth.py --client_id TU_CLIENT_ID --client_secret TU_CLIENT_SECRET

El script te da una URL para abrir en el navegador, hacés login con tu cuenta de
Yahoo, autorizás la app, y Yahoo te muestra un código para pegar de vuelta acá.
Guarda el token (incluido el refresh_token) en scripts/.yahoo_tokens.json —
ese archivo NO se sube al repo (está en .gitignore), es solo para tu máquina.

No requiere instalar nada: solo Python 3 (librería estándar).
"""
import argparse
import base64
import json
import os
import urllib.parse
import urllib.request

AUTH_URL = "https://api.login.yahoo.com/oauth2/request_auth"
TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"
REDIRECT_URI = "oob"  # out-of-band: Yahoo muestra el código en pantalla, no necesita servidor local

TOKENS_PATH = os.path.join(os.path.dirname(__file__), ".yahoo_tokens.json")


def get_authorization_code(client_id):
    params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "language": "en-us",
    }
    url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    print("\n1. Abrí esta URL en tu navegador y logueate con tu cuenta de Yahoo:\n")
    print(f"   {url}\n")
    print("2. Autorizá la app cuando te lo pida.")
    print("3. Yahoo te va a mostrar un código en pantalla — pegalo acá abajo.\n")
    return input("Código: ").strip()


def exchange_code_for_tokens(client_id, client_secret, code):
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    data = urllib.parse.urlencode(
        {
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "code": code,
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
        return json.load(r)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client_id", required=True, help="Client ID (Consumer Key) de tu app de Yahoo")
    parser.add_argument("--client_secret", required=True, help="Client Secret (Consumer Secret) de tu app de Yahoo")
    args = parser.parse_args()

    code = get_authorization_code(args.client_id)
    tokens = exchange_code_for_tokens(args.client_id, args.client_secret, code)

    tokens["client_id"] = args.client_id
    tokens["client_secret"] = args.client_secret

    with open(TOKENS_PATH, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2)

    print(f"\nListo. Token guardado en {TOKENS_PATH} (no se sube al repo).")
    print("Ahora podés correr fetch_yahoo_league.py.")


if __name__ == "__main__":
    main()
