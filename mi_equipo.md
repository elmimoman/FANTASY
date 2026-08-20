# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada (regla anti-copia). Desde GW2 en adelante, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real ya congelada de la jornada N una vez pasado su deadline — se puede consultar en vivo desde una máquina con internet normal (el entorno cloud de Claude tiene el dominio bloqueado, pero la sesión local de Claude Code sí conecta).
- **Presupuesto usado:** £100.0m / £100.0m
- **Última actualización:** 2026-08-20 (pre-Gameweek 1)

## Plantilla (15)

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Verbruggen | Brighton | £4.5m | Titular |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Gabriel | Arsenal | £8.0m | Titular |
| DEF | Guéhi | Man City | £6.0m | Titular |
| DEF | Cash | Aston Villa | £4.5m | Titular |
| DEF | Mitchell | Crystal Palace | £4.5m | Titular |
| DEF | Diop | Ipswich Town | £4.0m | Suplente |
| MID | Bruno Fernandes | Man Utd | £12.0m | Titular |
| MID | Rice | Arsenal | £7.5m | Titular |
| MID | Wilson | Leeds | £6.5m | Titular |
| MID | Gomez | Brighton | £5.0m | Titular |
| MID | Hughes | Crystal Palace | £4.5m | Suplente |
| FWD | Haaland | Man City | £15.5m | Titular — **Capitán** |
| FWD | João Pedro | Chelsea | £7.5m | Titular |
| FWD | Calvert-Lewin | Leeds | £6.0m | Suplente/rotación |

**Once inicial (4-4-2):** Verbruggen; Gabriel, Guéhi, Cash, Mitchell; B.Fernandes, Rice, Wilson, Gomez; Haaland, João Pedro
**Banco:** Dubravka, Diop, Hughes, Calvert-Lewin
**Capitán:** Haaland | **Vice-capitán:** Bruno Fernandes (sugerido)

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API (595 jugadores), optimizada dentro de £100.0m exactos, máx. 3 jugadores por equipo real. Ver `fpl_precios.csv` para el dataset completo usado.
