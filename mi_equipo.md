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

## Discusión abierta / pendiente

- **Revisión integral pendiente (iniciada 2026-10-23):** diagnóstico con datos reales de 7 jornadas detectó 5 problemas: Lammens (resuelto → Raya), Bruno Fernandes (resuelto → Mbeumo), y quedan **3 sin resolver**:
  - **Wissa** (FWD, Newcastle, £6.1m): 18 pts/7 jornadas, ppg 2.6, forma 1.5. No rinde.
  - **Anderson** (MID, Man City, £6.3m): 22 pts, ppg 3.1, forma 3.5. Flojo para el precio.
  - **Yarmoliuk** (MID, Brentford, £4.8m): suspendido hasta 8 nov, slot muerto en banca hasta entonces.
  Sin transfers gratis disponibles tras los 2 de esta semana. Opciones sobre la mesa: (a) ir de a uno con transfers normales las próximas semanas, (b) usar el **Wildcard** (ninguno usado, disponible hasta GW19) para resolver los 3 de una vez sin costo. Decisión pendiente — David prefirió no decidirlo apurado antes del deadline de GW8, sesión aparte con calma.

## Metodología

Ver `criterio.md` para el modelo completo y las reglas de desempate/exclusión.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API (595 jugadores), optimizada dentro de £100.0m exactos.
- **2026-08-20 (rebuilds 1-2):** Reconstrucción aplicando `criterio.md`; se saca Spurs, entra Tzolis a pedido de David.
- **2026-08-20 (GK + optimización):** Sale Raya por dudas de Saliba lesionado, entra Lammens. Sale Diarra, entra Anderson.
- **2026-09-04 a 2026-10-10 (sin registrar en su momento, reconstruido vía API el 2026-10-23):** David hizo 5 transfers reales en la app que no quedaron anotados acá — entre otros, volvió a cambiar la portería y metió a Calafiori por Gabriel en defensa, entraron Hall, Yarmoliuk, Groß, João Pedro y Wissa. **Lección: si el agente semanal no tiene forma de confirmar la plantilla real (API bloqueada en su entorno), este archivo se desactualiza silenciosamente.** A partir de ahora, cuando haya sesión local con acceso a la API, sincronizar `mi_equipo.md` contra `/api/entry/4682544/event/{ultimo_gw}/picks/` en vez de confiar en el historial manual.
- **2026-10-23 (pre-GW8):** Yarmoliuk suspendido sacado del XI (entra Ampadu). Lammens → Raya, Bruno Fernandes → Mbeumo (ver arriba). Se elimina la regla de "máx. 2 por club" a pedido de David. Quedan 3 problemas identificados sin resolver (Wissa, Anderson, Yarmoliuk) — ver "Discusión abierta".
