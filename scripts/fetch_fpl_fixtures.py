#!/usr/bin/env python3
"""
Descarga la dificultad de fixtures (FDR) de cada equipo para las próximas N
jornadas y la guarda en un CSV, en formato ancho: una fila por equipo,
una columna por jornada con "Rival(local/visita) FDR".

Uso:
    python3 fetch_fpl_fixtures.py
    python3 fetch_fpl_fixtures.py --gws 6 --out fpl_fixtures.csv
"""
import argparse
import csv
import json
import urllib.request
from collections import defaultdict

BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
FIXTURES_URL = "https://fantasy.premierleague.com/api/fixtures/"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gws", type=int, default=6, help="Cuantas jornadas hacia adelante")
    parser.add_argument("--out", default="fpl_fixtures.csv")
    args = parser.parse_args()

    bootstrap = fetch_json(BOOTSTRAP_URL)
    fixtures = fetch_json(FIXTURES_URL)

    teams = {t["id"]: t["name"] for t in bootstrap["teams"]}

    # find the next unfinished gameweek to anchor the window
    next_event = next((e["id"] for e in bootstrap["events"] if e.get("is_next")), 1)
    last_gw = next_event + args.gws - 1

    team_fixtures = defaultdict(dict)
    for f in fixtures:
        ev = f.get("event")
        if ev is None or ev < next_event or ev > last_gw:
            continue
        h, a = f["team_h"], f["team_a"]
        team_fixtures[h][ev] = f'{teams[a]} (H) FDR{f["team_h_difficulty"]}'
        team_fixtures[a][ev] = f'{teams[h]} (A) FDR{f["team_a_difficulty"]}'

    gw_cols = list(range(next_event, last_gw + 1))
    rows = []
    for tid, name in teams.items():
        difficulties = []
        row = {"equipo": name}
        for gw in gw_cols:
            entry = team_fixtures[tid].get(gw, "")
            row[f"GW{gw}"] = entry
            if entry:
                difficulties.append(int(entry.rsplit("FDR", 1)[1]))
        row["fdr_promedio"] = round(sum(difficulties) / len(difficulties), 2) if difficulties else ""
        rows.append(row)

    rows.sort(key=lambda r: r["fdr_promedio"] if r["fdr_promedio"] != "" else 999)

    fieldnames = ["equipo"] + [f"GW{gw}" for gw in gw_cols] + ["fdr_promedio"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Listo: fixtures de GW{next_event} a GW{last_gw} guardados en {args.out}")


if __name__ == "__main__":
    main()
