#!/usr/bin/env python3
"""
Tablero de draft NFL con filtro de disponibilidad real (ADP).

El problema que resuelve: recomendar un jugador que jamás va a llegar a tu turno.
Si drafteas en el pick 9 y alguien te sugiere a Ja'Marr Chase (ADP ~2), esa
recomendación es inútil: se lo llevan 7 picks antes. Este script nunca sugiere a
un jugador sin antes calcular la probabilidad de que siga libre en TU pick.

Fuentes de datos (en orden de preferencia):
  1. nfl_ranking.csv — ranking de consenso (ECR) de FantasyPros con su desviación
     estándar, ya versionado en el repo. Lo regenera scripts/fetch_nfl_ranking.py.
  2. FantasyFootballCalculator (--api) — ADP real medido en drafts reales del
     formato exacto de tu liga. Es mejor dato que el ECR, pero necesita internet
     sin filtros: si tu conexión lo bloquea, se usa el CSV.

Uso tipico:
    python3 draft_nfl.py --equipos 12 --pick 9

Durante el draft, para recalcular con lo que ya se fueron:
    python3 draft_nfl.py --equipos 12 --pick 9 --tomados tomados.txt

Con ADP real en vez del ranking (necesita internet abierto):
    python3 draft_nfl.py --equipos 12 --pick 9 --api

No requiere instalar nada: solo Python 3 (libreria estandar).
"""
import argparse
import csv
import json
import math
import os
import sys
import unicodedata
import urllib.request

RANKING = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "nfl_ranking.csv")
API = "https://fantasyfootballcalculator.com/api/v1/adp/{scoring}?teams={teams}&year={year}&position=all"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nfl_adp.json")

ETIQUETA = "ADP"   # se cambia a "ECR" cuando la fuente es el ranking de consenso

# Avisos de último momento (contrato, lesión, rol) que el ADP/ECR no siempre refleja
# a tiempo. Se revisan a mano vía búsqueda web — fecha de la última revisión abajo.
# Clave: nombre normalizado (sin tildes, minúsculas, sin espacios).
AVISOS_FECHA = "2026-09-01"
AVISOS = {
    "jamescookiii": "Standoff de contrato con Buffalo (hold-in, sin acuerdo cerca, rumores de trade). Explica por qué su rango de ECR es tan ancho (mejor 7º, peor 34º) - no es solo talento, es incertidumbre de si termina la temporada en ese equipo.",
    "jamescook": "Standoff de contrato con Buffalo (hold-in, sin acuerdo cerca, rumores de trade). Explica por qué su rango de ECR es tan ancho (mejor 7º, peor 34º) - no es solo talento, es incertidumbre de si termina la temporada en ese equipo.",
    "ashtonjeanty": "Lesión de tobillo. El mercado ya lo empujó al final de la ronda 2 - no lo pagues como si fuera ronda 1.",
    "kylemonangai": "Rodilla hiperextendida en práctica, semana a semana. Duda seria para la fecha 1.",
    "malikinabers": "Vuelve de rotura de cruzado y menisco (segunda cirugía en mayo). Apunta a la fecha 1, pero el mercado lo está regalando por el miedo - si te llega, es valor real.",
    "georgekittle": "Vuelve de rotura de Aquiles. El mercado ya compró el descuento: subió ~8 puestos.",
    "camskattebo": "Vuelve de lesión seria de pierna/tobillo. Comparte la cima del depth chart con Tracy Jr.",
    "buckyirving": "Operado del hombro, arrancó la pretemporada a tope. Sigue como RB principal de Tampa.",
    "tylerwarren": "Molestia en el aductor. Los Colts van con cautela, pero debería llegar a la fecha 1.",
    "joshjacobs": "NO LO AGARRES pase lo que pase con su ranking. Está en la lista de exentos del comisionado (cargos por incidente domestico de mayo) - no puede practicar ni jugar mientras siga ahi, sin fecha de regreso. Ademas venia de una lesion de ingle. Su ECR esta desactualizado y no refleja nada de esto. Backfield de GB mientras tanto: MarShawn Lloyd es el favorito, despues Chris Brooks y Kaleb Johnson.",
}

# Umbrales de probabilidad de seguir libre en tu pick.
P_OBJETIVO = 0.60   # muy probable que este ahi: se puede planificar con el
P_REALISTA = 0.25   # posible: vale la pena tenerlo en el radar
# Debajo de P_REALISTA no se recomienda. Punto. Sin excepciones "por talento".


# ---------------------------------------------------------------- datos

def descargar_adp(scoring, equipos, anio):
    url = API.format(scoring=scoring, teams=equipos, year=anio)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    print(f"Descargando ADP real ({scoring}, {equipos} equipos, {anio})...", file=sys.stderr)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    jugadores = data.get("players") or []
    if not jugadores:
        raise SystemExit("La API respondio sin jugadores. Probá otro --anio (quizá el ADP de esta temporada aún no está publicado).")
    return jugadores


def cargar_ranking_csv(ruta):
    """Lee nfl_ranking.csv (ECR de FantasyPros). El ECR ocupa el lugar del ADP:
    es un rango de consenso, comparable en escala al número de pick."""
    with open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    if not filas:
        raise SystemExit(f"{ruta} está vacío. Regeneralo con scripts/fetch_nfl_ranking.py")
    global ETIQUETA
    ETIQUETA = "ECR"
    fecha = filas[0].get("fecha", "?")
    print(f"Fuente: ranking de consenso FantasyPros del {fecha} ({len(filas)} jugadores).", file=sys.stderr)
    return [{"name": r["nombre"], "position": r["posicion"], "team": r["equipo"],
             "adp": float(r["ecr"]), "stdev": float(r["sd"] or 0)} for r in filas]


def cargar_adp(args):
    """Devuelve la lista de jugadores con ADP, de internet o de un JSON guardado."""
    if args.adp_json:
        with open(args.adp_json, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("players", data)

    try:
        jugadores = descargar_adp(args.scoring, args.equipos, args.anio)
    except Exception as e:
        if os.path.exists(CACHE):
            print(f"No se pudo bajar el ADP ({e}). Uso la copia guardada {CACHE}.", file=sys.stderr)
            with open(CACHE, encoding="utf-8") as f:
                return json.load(f).get("players", [])
        raise SystemExit(
            f"No se pudo bajar el ADP: {e}\n"
            "Si estás sin internet, corré el script una vez con conexión (guarda scripts/nfl_adp.json)\n"
            "o pasale --adp-json con un archivo ya descargado."
        )

    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump({"scoring": args.scoring, "equipos": args.equipos,
                   "anio": args.anio, "players": jugadores}, f, ensure_ascii=False, indent=1)
    return jugadores


# ---------------------------------------------------------------- draft

def mis_picks(equipos, pick, rondas):
    """Numeros de pick globales en un draft serpiente (snake)."""
    picks = []
    for r in range(1, rondas + 1):
        if r % 2 == 1:
            picks.append((r - 1) * equipos + pick)
        else:
            picks.append(r * equipos - pick + 1)
    return picks


def prob_disponible(adp, stdev, pick):
    """P(el jugador siga libre cuando llegue el pick N).

    Modela el pick real de un jugador como una normal centrada en su ADP con la
    desviación medida en drafts reales. Sigue libre en el pick N si su pick real
    cae en N o después:  P = 1 - Phi((N - ADP)/sigma).
    """
    sigma = max(float(stdev or 0), 1.5)          # piso: ni el consenso mas ferreo es exacto
    z = (pick - adp) / (sigma * math.sqrt(2))
    return max(0.0, min(1.0, 0.5 * (1 - math.erf(z))))


def normalizar(nombre):
    s = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode().lower()
    return "".join(c for c in s if c.isalnum())


def leer_tomados(ruta):
    if not ruta:
        return set()
    with open(ruta, encoding="utf-8") as f:
        return {normalizar(l) for l in f if l.strip() and not l.startswith("#")}


# ---------------------------------------------------------------- salida

def aviso_de(j):
    return AVISOS.get(normalizar(j["name"]))


def fmt(j, p=None, vistos_aviso=None):
    linea = f"  {j['adp']:>5.1f} {ETIQUETA}  {j['position']:<3} {j['name']:<24} {j.get('team') or '--':<3}"
    if p is not None:
        linea += f"  libre en tu pick: {p*100:>3.0f}%"
    if aviso_de(j):
        linea += "  ⚠"
        if vistos_aviso is not None and j["name"] not in [v["name"] for v in vistos_aviso]:
            vistos_aviso.append(j)
    return linea


def informe(jugadores, args):
    tomados = leer_tomados(args.tomados)
    libres = [j for j in jugadores if normalizar(j["name"]) not in tomados]
    libres.sort(key=lambda j: j["adp"])

    picks = mis_picks(args.equipos, args.pick, args.rondas)
    print(f"\nDraft snake de {args.equipos} equipos, vos elegís {args.pick}º ({args.scoring.upper()}, {args.anio}).")
    print(f"Tus picks: {', '.join(str(p) for p in picks)}")
    if tomados:
        print(f"Descontados {len(tomados)} jugadores ya tomados.")
    print(f"Avisos de contrato/lesión revisados a mano el {AVISOS_FECHA} — marcados con ⚠ abajo.")

    vistos_aviso = []

    primero = picks[0]

    # 1) Lo primero es lo que NO va a pasar. Es el error que este script existe para evitar.
    inalcanzables = [j for j in libres[:20] if prob_disponible(j["adp"], j.get("stdev"), primero) < P_REALISTA]
    if inalcanzables:
        print(f"\n=== NO los vas a alcanzar en el pick {primero} (se van antes) ===")
        for j in inalcanzables:
            print(fmt(j, prob_disponible(j["adp"], j.get("stdev"), primero), vistos_aviso))

    # 2) Ronda por ronda, solo gente que puede estar ahi de verdad.
    for r, pick in enumerate(picks, 1):
        cands = []
        for j in libres:
            p = prob_disponible(j["adp"], j.get("stdev"), pick)
            if p >= P_REALISTA:
                cands.append((p, j))
            if j["adp"] > pick + 60:      # la lista viene ordenada: mas alla no hay nada util
                break
        cands.sort(key=lambda t: t[1]["adp"])

        print(f"\n=== Ronda {r} — pick global {pick} ===")
        if not cands:
            print("  (sin candidatos con ADP en este rango)")
            continue

        seguros = [c for c in cands if c[0] >= P_OBJETIVO]
        apuestas = [c for c in cands if c[0] < P_OBJETIVO]

        if apuestas:
            print(f"  Se te pueden escapar (libre <{P_OBJETIVO*100:.0f}%), pero si están, son el mejor valor:")
            for p, j in apuestas[:args.top]:
                print(fmt(j, p, vistos_aviso))
        if seguros:
            print(f"  Objetivos realistas (libre >={P_OBJETIVO*100:.0f}%):")
            for p, j in seguros[:args.top]:
                print(fmt(j, p, vistos_aviso))

        # Mejor disponible por posicion, para no quedarte con un hueco
        print("  Mejor por posición:")
        vistos = set()
        for p, j in cands:
            pos = j["position"]
            if pos in vistos or p < P_OBJETIVO:
                continue
            vistos.add(pos)
            print(fmt(j, p, vistos_aviso))

    if vistos_aviso:
        print(f"\n=== ⚠ Avisos de contrato/lesión (revisados a mano el {AVISOS_FECHA}) ===")
        for j in vistos_aviso:
            print(f"  {j['name']}: {aviso_de(j)}")

    print(f"\nRegla: nunca planificar con un jugador por debajo de {P_REALISTA*100:.0f}% de estar libre.")
    print("Durante el draft, anotá los que se van en un .txt (uno por línea) y volvé a correr con --tomados.")


def main():
    ap = argparse.ArgumentParser(description="Tablero de draft NFL filtrado por disponibilidad real (ADP).")
    ap.add_argument("--equipos", type=int, default=12, help="equipos en la liga (default 12)")
    ap.add_argument("--pick", type=int, required=True, help="tu posición de draft en la ronda 1")
    ap.add_argument("--rondas", type=int, default=16, help="rondas del draft (default 16)")
    ap.add_argument("--scoring", default="ppr", choices=["ppr", "half-ppr", "standard", "2qb", "dynasty"],
                    help="formato de puntuación (default ppr)")
    ap.add_argument("--anio", type=int, default=2026, help="temporada del ADP (default 2026)")
    ap.add_argument("--top", type=int, default=6, help="cuántos candidatos mostrar por bloque")
    ap.add_argument("--tomados", help="archivo .txt con los jugadores ya drafteados, uno por línea")
    ap.add_argument("--adp-json", dest="adp_json", help="usar un JSON de ADP ya descargado en vez de la API")
    ap.add_argument("--api", action="store_true",
                    help="usar el ADP real de FantasyFootballCalculator en vez del ranking del repo")
    ap.add_argument("--ranking", default=RANKING, help="ruta del CSV de ranking (default: nfl_ranking.csv)")
    args = ap.parse_args()

    if not 1 <= args.pick <= args.equipos:
        raise SystemExit(f"--pick debe estar entre 1 y {args.equipos}")

    if args.api or args.adp_json:
        jugadores = cargar_adp(args)
    elif os.path.exists(args.ranking):
        jugadores = cargar_ranking_csv(args.ranking)
    else:
        raise SystemExit(
            f"No encuentro {args.ranking}. Generalo con:\n"
            "    python3 scripts/fetch_nfl_ranking.py\n"
            "o usá --api para bajar el ADP real de FantasyFootballCalculator.")

    limpios = [
        {"name": j["name"], "position": j["position"], "team": j.get("team"),
         "adp": float(j["adp"]), "stdev": float(j.get("stdev") or 0)}
        for j in jugadores if j.get("adp")
    ]
    informe(limpios, args)


if __name__ == "__main__":
    main()
