# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada (regla anti-copia). Una vez pasado el deadline de una jornada, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real de esa jornada — confirmado que conecta sin problema desde una sesión local de Claude Code (el entorno cloud del agente programado sigue bloqueado).
- **Zona horaria de David:** Panamá (UTC-5, sin horario de verano). Reportar deadlines siempre en hora de Panamá.
- **Preferencias de David:** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). Ya NO hay límite propio de "máx. 2 por club" — se eliminó el 2026-10-23, solo aplica el límite de FPL (máx. 3). La exclusión de jugadores del Spurs sigue vigente salvo el portero suplente (Dubravka, elegido por mérito puro ya que casi no juega).
- **Transfers gratis:** FPL permite bancar hasta 4 extra (5 en total). Antes de recomendar una compra, calcular cuántos FT tiene David revisando `event_transfers`/`event_transfers_cost` en `https://fantasy.premierleague.com/api/entry/4682544/history/` — no asumir que es solo 1.
- **Chips:** ninguno usado todavía (Wildcard, Free Hit, Bench Boost, Triple Captain — 1 de cada uno disponible en la primera mitad de temporada, GW2-19; otro juego de 4 para la segunda mitad, GW20-38).
- **Última actualización:** 2026-10-23 (pre-Gameweek 8) — se sincronizó el archivo con la plantilla REAL vía API (llevaba desde el 12 de sep desactualizado; David había hecho varios cambios en la app que no se habían anotado acá). Esta sesión: sale Yarmoliuk del XI titular (suspendido hasta 8 nov) por Ampadu — cambio de alineación, no transfer. Transfers de esta semana: **Lammens → Raya** (GK, rendía muy por debajo: 16 pts/7 jornadas vs los 42 de Raya) y **Bruno Fernandes → Mbeumo** (MID, Bruno en forma 1.0 y carísimo £11.8m; Mbeumo ya lo supera en puntos reales por £3.9m menos). Ambos gratis (David tenía 2 FT bancados).

## Plantilla (15) — post-transfers GW8

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Raya | Arsenal | £6.1m | Titular |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Calafiori | Arsenal | £6.0m | Titular |
| DEF | Guéhi | Man City | £6.0m | Titular |
| DEF | Hall | Newcastle | £5.3m | Titular |
| DEF | Diop | Ipswich Town | £3.9m | Suplente |
| DEF | Ballard | Sunderland | £4.8m | Suplente (lesionado) |
| MID | Mbeumo | Man Utd | £7.9m | Titular |
| MID | Anderson | Man City | £6.3m | Titular |
| MID | Groß | Brighton | £6.2m | Titular |
| MID | Yarmoliuk | Brentford | £4.8m | Suplente (suspendido hasta 8 nov) |
| MID | Ampadu | Leeds | £5.3m | Titular (entra por Yarmoliuk) |
| FWD | Haaland | Man City | £15.7m | Titular — **Capitán** |
| FWD | João Pedro | Chelsea | £7.9m | Titular |
| FWD | Wissa | Newcastle | £6.1m | Titular |

**Vice-capitán:** revisar cada semana con el modelo (ver `criterio.md`) — no asumir que sigue siendo Bruno Fernandes, ya no está en el equipo.

## Plan decidido: Wildcard en GW9 (deadline 2026-10-31)

**Decisión tomada 2026-10-23:** en vez de arreglar Wissa/Anderson/Yarmoliuk de a uno
con transfers normales (2+ semanas sangrando puntos), se usa el **Wildcard** (ninguno
gastado todavía) para la GW9, resolviendo todo de una vez sin costo.

**Candidatos identificados (con datos reales de 7 jornadas, a confirmar/refrescar
justo antes del deadline):**
- Wissa (FWD, £6.1m, 18pts, forma1.5) → **Kostoulas** (Brighton, £5.7m, 41pts,
  forma6.5, más consistente) o **Evanilson** (Bournemouth, £6.1m, 37pts, forma9.5,
  más caliente ahora mismo pero debuta GW9... revisar fixture exacto al refrescar).
- Anderson (MID, £6.3m, 22pts, forma3.5) → **Rice** (Arsenal, £7.3m, 36pts, forma8.0
  — mejor forma de todos los candidatos evaluados; ya no hay límite de 2 por Arsenal).
- Yarmoliuk (MID, suspendido hasta 8 nov) → por definir, cualquier opción decente lo
  mejora.
- Revisar también con el wildcard (no urgente pero vale la pena aprovechar): Guéhi y
  Hall, marcados como "bien pero bajando" en el diagnóstico del 23 de octubre.

**Próximo paso:** 2-3 días antes del deadline de GW9 (31 oct), refrescar
`fpl_precios.csv`/`fpl_fixtures.csv` con datos en vivo y confirmar los reemplazos
finales antes de jugar el chip — los números de arriba son del 23 de octubre, pueden
moverse.

**Otros chips:** ninguno más por ahora. Bench Boost necesita banca fuerte (la actual
está floja — Dubravka, Diop, Ballard lesionado, Yarmoliuk suspendido). Triple Captain
se guarda para doble jornada o fixture soñado de Haaland. Free Hit se guarda para una
blank gameweek. Ninguno de los tres tiene una ventana identificada todavía.

## Metodología

Ver `criterio.md` para el modelo completo y las reglas de desempate/exclusión.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API (595 jugadores), optimizada dentro de £100.0m exactos.
- **2026-08-20 (rebuilds 1-2):** Reconstrucción aplicando `criterio.md`; se saca Spurs, entra Tzolis a pedido de David.
- **2026-08-20 (GK + optimización):** Sale Raya por dudas de Saliba lesionado, entra Lammens. Sale Diarra, entra Anderson.
- **2026-09-04 a 2026-10-10 (sin registrar en su momento, reconstruido vía API el 2026-10-23):** David hizo 5 transfers reales en la app que no quedaron anotados acá — entre otros, volvió a cambiar la portería y metió a Calafiori por Gabriel en defensa, entraron Hall, Yarmoliuk, Groß, João Pedro y Wissa. **Lección: si el agente semanal no tiene forma de confirmar la plantilla real (API bloqueada en su entorno), este archivo se desactualiza silenciosamente.** A partir de ahora, cuando haya sesión local con acceso a la API, sincronizar `mi_equipo.md` contra `/api/entry/4682544/event/{ultimo_gw}/picks/` en vez de confiar en el historial manual.
- **2026-10-23 (pre-GW8):** Yarmoliuk suspendido sacado del XI (entra Ampadu). Lammens → Raya, Bruno Fernandes → Mbeumo (ver arriba). Se elimina la regla de "máx. 2 por club" a pedido de David. Quedan 3 problemas identificados sin resolver (Wissa, Anderson, Yarmoliuk) — ver "Discusión abierta".
