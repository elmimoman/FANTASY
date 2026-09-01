#!/usr/bin/env python3
"""
Baja el ranking de consenso (ECR) de FantasyPros para draft de redraft y lo deja
en nfl_ranking.csv, que es lo que consume scripts/draft_nfl.py.

Fuente: el espejo público de DynastyProcess en GitHub, que scrapea FantasyPros
todas las semanas. Se usa el .parquet, no el .csv.gz: el csv.gz dejó de
actualizarse en agosto 2025, el parquet sigue al día.

  https://github.com/dynastyprocess/data

De cada jugador salen dos números que importan:
  - ecr = rango de consenso (promedio de los rankings de los expertos)
  - sd  = desviación estándar de ese consenso (cuánto se pelean entre ellos)

Uso:
    python3 fetch_nfl_ranking.py                 # temporada actual
    python3 fetch_nfl_ranking.py --tipo best-overall   # para ligas best ball

Requiere pyarrow para leer el parquet:  pip install pyarrow
"""
import argparse
import csv
import os
import sys
import urllib.request

URL = "https://raw.githubusercontent.com/dynastyprocess/data/master/files/db_fpecr.parquet"
DESTINO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "nfl_ranking.csv")


def main():
    ap = argparse.ArgumentParser(description="Baja el ranking de consenso de FantasyPros (vía DynastyProcess).")
    ap.add_argument("--tipo", default="redraft-overall",
                    help="redraft-overall (default), best-overall, dynasty-overall...")
    ap.add_argument("--fecha", help="usar un scrape_date concreto (default: el más reciente)")
    ap.add_argument("--salida", default=DESTINO)
    args = ap.parse_args()

    try:
        import pyarrow.parquet as pq
    except ImportError:
        raise SystemExit("Falta pyarrow para leer el archivo. Instalalo con:  pip install pyarrow")

    tmp = args.salida + ".parquet.tmp"
    print("Descargando el ranking de FantasyPros (~37 MB, tarda un poco)...", file=sys.stderr)
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(tmp, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)

    try:
        cols = ["page_type", "player", "pos", "team", "ecr", "sd", "best", "worst", "scrape_date"]
        datos = pq.read_table(tmp, columns=cols).to_pydict()
        filas = [dict(zip(cols, r)) for r in zip(*[datos[c] for c in cols]) ]
    finally:
        os.remove(tmp)

    filas = [f for f in filas if f["page_type"] == args.tipo]
    if not filas:
        raise SystemExit(f"No hay filas para --tipo {args.tipo}")

    fecha = args.fecha or max(str(f["scrape_date"]) for f in filas)
    filas = [f for f in filas if str(f["scrape_date"]) == fecha and f["ecr"] is not None]
    filas.sort(key=lambda f: f["ecr"])

    with open(args.salida, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nombre", "posicion", "equipo", "ecr", "sd", "mejor", "peor", "fecha"])
        for r in filas:
            w.writerow([r["player"], r["pos"], r["team"], round(float(r["ecr"]), 1),
                        round(float(r["sd"] or 0), 1), r["best"], r["worst"], fecha])

    print(f"Listo: {len(filas)} jugadores ({args.tipo}, scrape del {fecha}) -> {args.salida}")


if __name__ == "__main__":
    main()
