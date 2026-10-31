#!/usr/bin/env python3
"""
Valida si la 'forma' de FPL (o una aproximacion casera: promedio de puntos de
los ultimos N partidos) correlaciona con los puntos del SIGUIENTE partido.

Usa /api/element-summary/{id}/ para el historial real jornada a jornada de
cada jugador con minutos significativos, construye pares
(forma_antes_de_la_jornada, puntos_en_la_jornada) y calcula la correlacion
de Pearson. Compara tambien contra otros predictores simples (puntos del
partido anterior solo, puntos/partido de toda la temporada hasta ese punto)
para ver cual predice mejor.

Uso:
    python3 analyze_form_correlation.py --min-minutes 300 --window 3
"""
import argparse
import json
import math
import time
import urllib.request

BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
SUMMARY_URL = "https://fantasy.premierleague.com/api/element-summary/{}/"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx == 0 or vy == 0:
        return None
    return cov / math.sqrt(vx * vy)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-minutes", type=int, default=300)
    parser.add_argument("--window", type=int, default=3, help="Partidos para calcular la forma")
    parser.add_argument("--limit", type=int, default=250, help="Max jugadores a analizar (por minutos)")
    args = parser.parse_args()

    bootstrap = fetch_json(BOOTSTRAP_URL)
    players = [p for p in bootstrap["elements"] if p["minutes"] >= args.min_minutes]
    players.sort(key=lambda p: -p["minutes"])
    players = players[: args.limit]
    print(f"Analizando {len(players)} jugadores con >= {args.min_minutes} minutos jugados...")

    form_pairs = []        # (forma_rolling_N, puntos_siguiente)
    last_game_pairs = []   # (puntos_partido_anterior_solo, puntos_siguiente)
    season_ppg_pairs = []  # (ppg_acumulado_hasta_ahora, puntos_siguiente)

    for i, p in enumerate(players):
        try:
            summary = fetch_json(SUMMARY_URL.format(p["id"]))
        except Exception as e:
            continue
        history = summary.get("history", [])
        history.sort(key=lambda h: h["round"])
        points_seq = [h["total_points"] for h in history]

        for k in range(args.window, len(points_seq)):
            window_pts = points_seq[k - args.window : k]
            form_rolling = sum(window_pts) / args.window
            next_pts = points_seq[k]
            form_pairs.append((form_rolling, next_pts))
            last_game_pairs.append((points_seq[k - 1], next_pts))
            season_ppg_pairs.append((sum(points_seq[:k]) / k, next_pts))

        if (i + 1) % 50 == 0:
            print(f"  ...{i+1}/{len(players)}")

    print(f"\nTotal de observaciones (jugador x jornada): {len(form_pairs)}")

    def report(name, pairs):
        xs = [x for x, y in pairs]
        ys = [y for x, y in pairs]
        r = pearson(xs, ys)
        print(f"{name}: r = {r:.3f}  (n={len(pairs)})" if r is not None else f"{name}: sin datos suficientes")

    print(f"\n=== Correlacion con los puntos del SIGUIENTE partido ===")
    report(f"Forma (promedio ultimos {args.window} partidos)", form_pairs)
    report("Solo el partido anterior", last_game_pairs)
    report("Puntos/partido de toda la temporada hasta ese punto", season_ppg_pairs)


if __name__ == "__main__":
    main()
