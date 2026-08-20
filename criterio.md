# Nuestro criterio para elegir jugadores (FPL)

No nos basamos en artículos de terceros. Usamos datos directos de la API oficial
(`fpl_precios.csv`, `fpl_fixtures.csv`) y un modelo casero simple, documentado aquí
para que cualquier recomendación futura sea consistente.

## 1. Horizonte: 2-3 jornadas, no solo la próxima

Los transfers son limitados (1 gratis por semana; usar más cuesta -4 pts cada uno),
así que nunca cambiamos un jugador por un solo partido bueno o malo. Toda comparación
de fichajes se hace sobre la suma proyectada de las próximas 2-3 jornadas como mínimo,
no solo la inmediata.

## 2. Modelo de puntos proyectados por jornada

FPL solo publica `ep_next` (estimado algorítmico propio para la jornada inmediata),
no un proyección multi-jornada. Nuestro modelo casero extiende eso:

```
proyeccion(jugador, jornada) = ep_next(jugador) * (3 / FDR(equipo, jornada))
```

- `FDR` = Fixture Difficulty Rating oficial de FPL (1=fácil, 5=muy difícil), de `fpl_fixtures.csv`.
- 3 es el FDR promedio de referencia, así que un fixture más fácil que el promedio
  sube la proyección, y uno más difícil la baja.
- Es un heurístico simple, no un modelo estadístico complejo — sirve para comparar
  jugadores similares entre sí, no como predicción exacta de puntos.

Sumamos la proyección de las próximas 2-3 (o 6, para ver la tendencia completa) jornadas
para comparar candidatos.

## 3. Preferencia por track record

Ante proyecciones similares, preferimos jugadores con puntos reales de la temporada
anterior (`puntos_totales`, `puntos_por_partido` en `fpl_precios.csv`) sobre jugadores
sin historial en la Premier — el hype de pretemporada no garantiza rendimiento.

## 4. Desempate: Arsenal

Si dos jugadores están en condiciones similares (misma posición, precio parecido,
proyección de puntos comparable), preferimos al jugador del Arsenal. Es una preferencia
explícita de David, no un criterio de rendimiento — solo aplica como desempate, nunca
por encima de una diferencia real de proyección.

## Archivos de datos (se regeneran con los scripts en `scripts/`)

- `fpl_precios.csv` — precios y estadísticas de los 595 jugadores (`scripts/fetch_fpl_prices.py`)
- `fpl_fixtures.csv` — dificultad de fixtures (FDR) por equipo, próximas N jornadas (`scripts/fetch_fpl_fixtures.py`)
- `mi_equipo.md` — plantilla actual de David y su Team ID
