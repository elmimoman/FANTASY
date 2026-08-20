# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada (regla anti-copia). Desde GW2 en adelante, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real ya congelada de la jornada N una vez pasado su deadline — se puede consultar en vivo desde una máquina con internet normal (el entorno cloud de Claude tiene el dominio bloqueado, pero la sesión local de Claude Code sí conecta).
- **Presupuesto usado:** £100.0m / £100.0m
- **Última actualización:** 2026-08-20 (pre-Gameweek 1)
- **Preferencias de David (además del modelo):** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). No confía en el arranque de temporada del Spurs por ahora ("no sé cómo va a venir ese equipo") — se evitan jugadores del Spurs hasta que haya evidencia de cómo empiezan (revisar después de GW1-2, esto no es una regla permanente).

## Plantilla (15)

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Raya | Arsenal | £6.0m | Titular |
| GK  | Steele | Brighton | £4.0m | Suplente |
| DEF | Gabriel | Arsenal | £8.0m | Titular |
| DEF | Guéhi | Man City | £6.0m | Titular |
| DEF | Ballard | Sunderland | £5.0m | Titular |
| DEF | Collins | Brentford | £5.5m | Titular |
| DEF | Ajer | Brentford | £4.5m | Suplente |
| MID | Bruno Fernandes | Man Utd | £12.0m | Titular |
| MID | Amad Diallo | Man Utd | £6.0m | Titular |
| MID | Xhaka | Sunderland | £5.5m | Titular |
| MID | Tzolis | Arsenal | £6.5m | Titular |
| MID | Diarra | Sunderland | £5.5m | Suplente |
| FWD | Haaland | Man City | £15.5m | Titular |
| FWD | Georginio | Brighton | £5.5m | Titular |
| FWD | Furo | Brentford | £4.5m | Suplente |

**Once inicial (4-4-2):** Raya; Gabriel, Guéhi, Ballard, Collins; B.Fernandes, Amad, Xhaka, Tzolis; Haaland, Georginio
**Banco:** Steele (GK), Ajer, Diarra, Furo
**Capitán por jornada (no es fijo — ver metodología en `criterio.md`):**
- GW1: **Bruno Fernandes** (vs Hull City, FDR2) sobre Haaland (vs Bournemouth, FDR3)
- GW2: **Bruno Fernandes** (vs Ipswich, FDR2) sobre Haaland (fuera vs Crystal Palace, FDR3)
- GW3: **Haaland** (vs Coventry City, FDR2) sobre Bruno (fuera vs Everton, FDR3)

Vice-capitán: el que no sea capitán esa semana, entre Bruno Fernandes y Haaland.

## Metodología

Ver `criterio.md` para el modelo completo y las reglas de desempate/exclusión.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API (595 jugadores), optimizada dentro de £100.0m exactos, máx. 3 jugadores por equipo real.
- **2026-08-20 (rebuild 1):** Plantilla reconstruida de cero aplicando `criterio.md` — proyección propia a 3 jornadas en vez de opiniones de webs.
- **2026-08-20 (rebuild 2):** A pedido de David: (1) se saca a todo jugador del Spurs (Dubravka, Senesi, Richarlison) por desconfianza en su arranque de temporada — no es una exclusión permanente, revisar tras GW1-2; (2) entra Tzolis (Arsenal MID, £6.5m) por pedido directo, aunque el modelo lo proyecta ligeramente por debajo de la opción que salió (Lewis-Potter) — se documenta la diferencia (-0.2 pts proyectados en 3 fechas) para que quede claro que es una decisión de preferencia, no del modelo puro. Entraron también Guéhi (Man City DEF), Ajer y Collins (Brentford DEF), Georginio (Brighton FWD) para reemplazar a los del Spurs con opciones de proyección similar o mejor.
