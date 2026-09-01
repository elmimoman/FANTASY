#!/usr/bin/env python3
"""
Descarga TODOS los jugadores de la NFL desde la API pública de Sleeper y los deja
filtrados a los que sirven para fantasy (ofensiva + pateadores + defensas).

La API de Sleeper es pública: no necesita cuenta, ni login, ni token.

Uso:
    python3 fetch_nfl_players.py

Genera dos archivos:
  - nfl_jugadores.csv   → para mirarlo vos en Excel/Numbers
  - nfl_jugadores.json  → para pasárselo a Claude y que lo cargue en el tablero

No requiere instalar nada: solo Python 3 (librería estándar).
"""
import csv
import json
import urllib.request

URL = "https://api.sleeper.app/v1/players/nfl"

# Posiciones que importan en fantasy. El resto (linieros, etc.) no suma puntos.
POSICIONES = {"QB", "RB", "WR", "TE", "K", "DEF"}


def descargar():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    print("Descargando la base de jugadores de la NFL (~5 MB, puede tardar unos segundos)...")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def filtrar(data):
    jugadores = []
    for pid, p in data.items():
        pos = p.get("position")
        if pos not in POSICIONES:
            continue
        # Sin equipo = agente libre sin contrato, no sirve para el draft
        equipo = p.get("team")
        if not equipo:
            continue
        # Solo jugadores activos
        if p.get("status") not in (None, "Active"):
            continue

        nombre = p.get("full_name") or p.get("last_name") or pid
        jugadores.append(
            {
                "nombre": nombre,
                "posicion": pos,
                "equipo": equipo,
                "numero": p.get("number"),
                "anios_experiencia": p.get("years_exp"),
                "lesion": p.get("injury_status") or "",
            }
        )

    # Ordenar por posición y después por nombre, para que sea fácil de leer
    orden_pos = {"QB": 0, "RB": 1, "WR": 2, "TE": 3, "K": 4, "DEF": 5}
    jugadores.sort(key=lambda j: (orden_pos.get(j["posicion"], 9), j["nombre"]))
    return jugadores


def main():
    data = descargar()
    jugadores = filtrar(data)

    with open("nfl_jugadores.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(jugadores[0].keys()))
        writer.writeheader()
        writer.writerows(jugadores)

    with open("nfl_jugadores.json", "w", encoding="utf-8") as f:
        json.dump(jugadores, f, ensure_ascii=False, indent=1)

    por_pos = {}
    for j in jugadores:
        por_pos[j["posicion"]] = por_pos.get(j["posicion"], 0) + 1

    print(f"\nListo: {len(jugadores)} jugadores guardados.")
    print("Desglose: " + ", ".join(f"{k} {v}" for k, v in sorted(por_pos.items())))
    print("\nArchivos generados:")
    print("  nfl_jugadores.csv   (para mirarlo vos)")
    print("  nfl_jugadores.json  (pasáselo a Claude para cargarlo en el tablero)")


if __name__ == "__main__":
    main()
