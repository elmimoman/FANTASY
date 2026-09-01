# Nuestro criterio para el draft de NFL

Mismo espíritu que `criterio.md` (FPL): nada de recomendaciones de memoria ni copiadas
de artículos. Datos reales, modelo simple y documentado, y reglas que se cumplen aunque
el jugador sea buenísimo.

## 0. Regla cero: una recomendación que no llega a tu pick no es una recomendación

**Nunca se sugiere un jugador sin calcular antes la probabilidad de que siga libre en TU
turno.** Draft snake de 12 equipos, pick 9: entre tu turno y el inicio hay 8 selecciones
ajenas. Cualquiera con ADP por debajo de ~6 ya no existe para vos, por más que sea el
mejor jugador del tablero.

*Aprendido el 2026-09-01:* se recomendó a Ja'Marr Chase (ADP ~2) para el pick 9. David lo
detectó, no el análisis. La causa real: no había ninguna herramienta de draft en el repo —
la sugerencia salió de charla, sin ningún dato de ADP de por medio. De ahí sale
`scripts/draft_nfl.py`, que aplica esta regla automáticamente.

## 1. Fuente de datos: ADP real, del formato exacto de tu liga

`scripts/draft_nfl.py` baja el ADP de FantasyFootballCalculator (API pública, sin login),
pidiendo el mismo formato que tu liga: cantidad de equipos, puntuación (PPR / half-PPR /
standard) y temporada. El ADP de un draft de 10 equipos standard no sirve para una liga de
12 PPR — la posición de cada jugador cambia.

## 2. Modelo de disponibilidad

```
P(libre en el pick N) = 1 - Phi( (N - ADP) / sigma )
```

- `ADP` = pick promedio del jugador en drafts reales.
- `sigma` = desviación estándar real que publica la misma fuente, con piso de 1.5
  (ningún consenso es exacto).
- `Phi` = normal acumulada. En castellano: se modela el pick real del jugador como una
  campana centrada en su ADP, y se mide cuánta de esa campana cae en tu turno o después.

Umbrales que usamos:

| P(libre) | Qué significa |
|---|---|
| ≥ 60% | **Objetivo realista.** Se puede planificar la ronda con él. |
| 25–60% | **Se te puede escapar.** Vale tenerlo en el radar como mejor valor si cae. |
| < 25% | **No se recomienda.** Ni se menciona como plan. |

## 3. El draft es snake, así que se planifica de a pares de rondas

Con 12 equipos y pick 9, tus turnos son 9, 16, 33, 40, 57... Entre el 16 y el 33 pasan 16
picks ajenos: es el hueco más grande del draft y es donde se define la temporada. Toda
recomendación de la ronda 2 se hace mirando qué va a quedar en la 3, no solo qué es lo
mejor ahora.

## 4. Durante el draft se recalcula, no se improvisa

Los jugadores que se van se anotan en un `.txt` (uno por línea) y se vuelve a correr con
`--tomados`. Cada corrida rearma el tablero con lo que queda de verdad.

Limitación conocida y aceptada: el modelo compara ADP contra el número de pick, así que no
reajusta el ADP del resto cuando el draft se desvía mucho del consenso (una corrida de QBs
temprana, por ejemplo). Sirve para ordenar candidatos, no como predicción exacta. Si el
draft se sale de guion, mandan los jugadores que efectivamente quedan en la lista.

## 5. Cómo se corre

```bash
# Antes del draft: tablero completo desde tu pick
python3 scripts/draft_nfl.py --equipos 12 --pick 9 --scoring ppr

# En vivo, descontando lo que ya se fueron
python3 scripts/draft_nfl.py --equipos 12 --pick 9 --tomados tomados.txt
```

La primera corrida con internet guarda `scripts/nfl_adp.json`, así que después funciona
aunque se caiga la conexión (o con `--adp-json`).
