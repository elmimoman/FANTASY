# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada (regla anti-copia). Desde GW2 en adelante, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real ya congelada de la jornada N una vez pasado su deadline — se puede consultar en vivo desde una máquina con internet normal (el entorno cloud de Claude tiene el dominio bloqueado, pero la sesión local de Claude Code sí conecta).
- **Presupuesto usado:** £100.0m / £100.0m
- **Última actualización:** 2026-08-20 (pre-Gameweek 1) — plantilla reconstruida con `criterio.md` (modelo propio, no artículos de terceros)

## Plantilla (15)

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Raya | Arsenal | £6.0m | Titular |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Gabriel | Arsenal | £8.0m | Titular |
| DEF | Senesi | Spurs | £6.0m | Titular |
| DEF | Ballard | Sunderland | £5.0m | Titular |
| DEF | Dalot | Man Utd | £5.0m | Suplente |
| DEF | Collins | Brentford | £5.5m | Suplente |
| MID | Bruno Fernandes | Man Utd | £12.0m | Titular |
| MID | Amad Diallo | Man Utd | £6.0m | Titular |
| MID | Xhaka | Sunderland | £5.5m | Titular |
| MID | Diarra | Sunderland | £5.5m | Titular |
| MID | Lewis-Potter | Brentford | £5.5m | Titular |
| FWD | Haaland | Man City | £15.5m | Titular |
| FWD | Richarlison | Spurs | £6.0m | Titular |
| FWD | Furo | Brentford | £4.5m | Suplente |

**Once inicial (3-5-2):** Raya; Gabriel, Senesi, Ballard; B.Fernandes, Amad, Xhaka, Diarra, Lewis-Potter; Haaland, Richarlison
**Banco:** Dubravka (GK), Dalot, Collins, Furo
**Capitán por jornada (no es fijo — ver metodología):**
- GW1: **Bruno Fernandes** (Man Utd vs Hull City, FDR2) — proyecta más que Haaland esta fecha (Man City vs Bournemouth, FDR3)
- GW2: **Bruno Fernandes** (vs Ipswich, FDR2) sobre Haaland (fuera vs Crystal Palace, FDR3)
- GW3: **Haaland** (vs Coventry City, FDR2) sobre Bruno (fuera vs Everton, FDR3)

Vice-capitán: el que no sea capitán esa semana, entre Bruno Fernandes y Haaland.

## Metodología

Ver `criterio.md` para el modelo completo. Resumen: proyección propia de puntos por
jornada = `ep_next (FPL) × (3 / FDR del fixture)`, sumada sobre las próximas 2-3
jornadas (nunca solo la inmediata, porque los transfers son limitados). Track
record de la temporada anterior como filtro de riesgo. Arsenal como desempate
solo en igualdad real de condiciones — Gabriel entró porque es objetivamente el
mejor defensa proyectado (no solo por sesgo), Raya quedó prácticamente empatado
en valor con las alternativas.

Datos usados: `fpl_precios.csv` (precios/stats) + `fpl_fixtures.csv` (dificultad
de fixtures). Regenerar ambos con `scripts/fetch_fpl_prices.py` y
`scripts/fetch_fpl_fixtures.py` antes de cada revisión para no decidir con datos
viejos.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API (595 jugadores), optimizada dentro de £100.0m exactos, máx. 3 jugadores por equipo real. Ver `fpl_precios.csv` para el dataset completo usado.
- **2026-08-20 (rebuild):** Plantilla reconstruida de cero aplicando `criterio.md` — proyección propia a 3 jornadas en vez de opiniones de webs. Cambios notables vs. la versión anterior: se sale toda la defensa/mediocampo "de nombre conocido" que no rendía mejor en el modelo (Rice, Wilson, Gomez, Cash, Mitchell, Hughes, João Pedro, Calvert-Lewin, Verbruggen) y entran jugadores con mejor relación proyección/precio aunque sean menos mediáticos (Senesi, Ballard, Amad, Xhaka, Diarra, Lewis-Potter, Richarlison). Se evaluó Tzolis (Arsenal MID, £6.5m) y Brobbey (Sunderland FWD, £6.0m) a pedido de David — Brobbey superó en proyección a Calvert-Lewin pero no entró en esta versión por presupuesto; Tzolis quedó fuera por no tener track record en Premier (0 pts temporada pasada) pese al sesgo Arsenal, hasta ver su debut en GW1.
