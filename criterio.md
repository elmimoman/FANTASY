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

**Regla obligatoria: nunca mostrar solo el total sumado.** Un total de 3 fechas puede
esconder un bache real (ej: una fecha muy fácil compensando dos difíciles seguidas).
Siempre desglosar jornada por jornada al presentar una comparación o al revisar la
plantilla — el promedio/suma es útil para ordenar candidatos, pero la decisión real
se toma mirando el detalle semana a semana. (Aprendido el 2026-08-20: se presentó el
total de Gabriel/Raya sin desglosar y se escondió que GW2 y GW3 caen a la mitad por
Aston Villa fuera y Chelsea en casa, ambos FDR4 — David lo detectó, no el análisis.)

## 3. Preferencia por track record

Ante proyecciones similares, preferimos jugadores con puntos reales de la temporada
anterior (`puntos_totales`, `puntos_por_partido` en `fpl_precios.csv`) sobre jugadores
sin historial en la Premier — el hype de pretemporada no garantiza rendimiento.

## 4. Desempate: Arsenal

Si dos jugadores están en condiciones similares (misma posición, precio parecido,
proyección de puntos comparable), preferimos al jugador del Arsenal. Es una preferencia
explícita de David, no un criterio de rendimiento — solo aplica como desempate, nunca
por encima de una diferencia real de proyección.

## 5. Exclusiones temporales por desconfianza de equipo

David puede marcar un equipo como "no confiable para empezar" (ej: incertidumbre por
cambio de entrenador, fichajes tardíos, pretemporada floja) sin importar lo que
proyecte el modelo — es una decisión de riesgo, no de rendimiento esperado. Se
documenta en `mi_equipo.md` con la razón y una fecha de revisión (normalmente tras
2-3 jornadas de evidencia real), para no dejarla como regla permanente por accidente.

## 6. Pedidos explícitos de un jugador puntual

Si David pide un jugador específico, se mete — pero siempre mostrando qué jugador
sale y cuál era su proyección vs. la del jugador pedido, para que la decisión sea
informada y quede clara en el historial de `mi_equipo.md`. El modelo no bloquea
preferencias personales, solo las hace transparentes.

## Archivos de datos (se regeneran con los scripts en `scripts/`)

- `fpl_precios.csv` — precios y estadísticas de los 595 jugadores (`scripts/fetch_fpl_prices.py`)
- `fpl_fixtures.csv` — dificultad de fixtures (FDR) por equipo, próximas N jornadas (`scripts/fetch_fpl_fixtures.py`)
- `mi_equipo.md` — plantilla actual de David y su Team ID
