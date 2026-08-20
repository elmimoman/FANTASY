#!/usr/bin/env python3
"""
Descarga los valores actuales de todos los jugadores de Fantasy Premier League
y los guarda en un CSV.

Uso:
    python3 fetch_fpl_prices.py
    python3 fetch_fpl_prices.py --out mis_precios.csv

No requiere instalar nada: solo usa la librería estándar de Python 3.
"""
import argparse
import csv
import json
import urllib.request

API_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"

POSITION_NAMES = {
    1: "GK",
    2: "DEF",
    3: "MID",
    4: "FWD",
}


def fetch_data():
    req = urllib.request.Request(API_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def build_rows(data):
    teams_by_id = {team["id"]: team["name"] for team in data["teams"]}

    rows = []
    for player in data["elements"]:
        rows.append(
            {
                "nombre": f'{player["first_name"]} {player["second_name"]}'.strip(),
                "nombre_corto": player["web_name"],
                "equipo": teams_by_id.get(player["team"], player["team"]),
                "posicion": POSITION_NAMES.get(player["element_type"], player["element_type"]),
                "precio_millones": player["now_cost"] / 10,
                "puntos_totales": player["total_points"],
                "forma": player["form"],
                "porcentaje_seleccionado": player["selected_by_percent"],
                "lesionado_o_duda": player["status"] != "a",
            }
        )
    rows.sort(key=lambda r: r["precio_millones"], reverse=True)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="fpl_precios.csv", help="Ruta del archivo CSV de salida")
    args = parser.parse_args()

    data = fetch_data()
    rows = build_rows(data)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Listo: {len(rows)} jugadores guardados en {args.out}")


if __name__ == "__main__":
    main()
