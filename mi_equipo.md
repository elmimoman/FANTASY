# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada. Una vez pasado, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real — confirmado que conecta sin problema desde una sesión local de Claude Code (el entorno cloud del agente programado sigue bloqueado, 403 confirmado semana tras semana).
- **⚠️ Problema de sincronización activo:** el agente semanal clona la rama `claude/fantasy-premier-league-values-bp1obf` de GitHub, no `main` — el "default branch" del repo nunca se cambió en la configuración de GitHub (paso manual pendiente de David, ver nota en el repo). Mientras no se cambie, cualquier edición de este archivo hecha en `main` **no la ve el agente** hasta que alguien la mergee a la otra rama. Ver sección de historial del 2026-10-30 para el caso real donde esto causó un informe con datos de hace 2 meses.
- **Zona horaria de David:** Panamá (UTC-5, sin horario de verano). Reportar deadlines siempre en hora de Panamá.
- **Preferencias de David:** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). Sin límite propio de jugadores por club (eliminado 2026-10-23), solo el límite de FPL (máx. 3). Exclusión de Spurs sigue vigente salvo el portero suplente (Dubravka, por mérito).
- **Transfers gratis:** FPL permite bancar hasta 4 extra (5 en total). Revisar `event_transfers`/`event_transfers_cost` en `.../history/` antes de asumir que solo hay 1 disponible.
- **Chips:** **Wildcard #1 usado el 2026-10-30/31, previo al deadline de GW9.** Quedan: Free Hit, Bench Boost, Triple Captain (1ra mitad, hasta GW19) + el set completo de 4 para la 2da mitad (GW20-38).
- **Última actualización:** 2026-10-30 (pre-Gameweek 9) — Wildcard jugado, 5 cambios (ver historial). Plantilla sincronizada vía API real (picks de GW8).

## Plantilla (15) — post-Wildcard, a jugar para GW9

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Raya | Arsenal | £6.2m | Titular |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Calafiori | Arsenal | £5.9m | Titular (doubt 75% — confirmar sábado) |
| DEF | Guéhi | Man City | £6.0m | Titular |
| DEF | De Cuyper | Brighton | £5.3m | Titular (NUEVO, por Hall) |
| DEF | Diop | Ipswich Town | £3.9m | Suplente |
| DEF | Ballard | Sunderland | £4.8m | Suplente (lesionado, sin fecha) |
| MID | Mbeumo | Man Utd | £7.9m | Titular |
| MID | Groß | Brighton | £6.2m | Titular |
| MID | Rice | Arsenal | £7.4m | Titular (NUEVO, por Anderson; doubt 75% — confirmar sábado) |
| MID | Tavernier | Bournemouth | £6.5m | Titular (NUEVO, por Yarmoliuk) |
| MID | Ampadu | Leeds | £5.3m | Suplente |
| FWD | Haaland | Man City | £15.8m | Titular — **Capitán** |
| FWD | Evanilson | Bournemouth | £6.3m | Titular (NUEVO, por Wissa) |
| FWD | Kostoulas | Brighton | £5.8m | Titular (NUEVO, por João Pedro) |

**Once inicial (3-4-3):** Raya; Calafiori, Guéhi, De Cuyper; Mbeumo, Groß, Rice, Tavernier; Haaland, Evanilson, Kostoulas
**Banco:** Dubravka (GK), Diop, Ballard, Ampadu
**Capitán:** Haaland | **Vice-capitán:** Mbeumo
**Valor plantilla:** £97.3m usados de £102.3m disponibles (£5.0m en banco — queda margen a propósito, no hace falta gastarlo todo)

**⚠️ Verificar el sábado antes del deadline (06:00 Panamá):** Calafiori y Rice están al 75% de jugar (dudas menores, no lesiones serias) — confirmar en la alineación oficial. Si alguno no juega, hay bench cover razonable (Diop/Ampadu) aunque no son reemplazos ideales.

## Por qué cada cambio (datos reales GW1-8, no proyección de pretemporada)

| Sale | Entra | Razón |
|---|---|---|
| Hall (£5.3m, 40pts, forma3.0) | De Cuyper (£5.3m, 60pts, forma7.3) | Mismo precio exacto, 20 pts más en la temporada. Upgrade gratis. |
| Anderson (£6.3m, 23pts, forma2.7) | Rice (£7.4m, 39pts, forma6.3) | Anderson nunca rindió lo que prometía el hype pre-temporada. |
| Yarmoliuk (suspendido hasta 8 nov) | Tavernier (£6.5m, 52pts, forma7.0) | Slot muerto en banca → 2do mejor mediocampista por puntos reales de toda la liga a ese precio. |
| Wissa (£6.1m, 19pts, forma1.3) | Evanilson (£6.3m, 43pts, forma8.3) | Wissa nunca despegó; Evanilson está en la mejor racha de su posición. |
| João Pedro (£7.9m, 47pts) | Kostoulas (£5.8m, 43pts, forma5.0) | João Pedro salió lesionado (muslo, **sin fecha de regreso confirmada**) — no es que rindiera mal, es que ya no puede jugar. Kostoulas es la mejor opción real disponible a su precio. |

**Resultado:** Brighton queda con 3 jugadores (Groß, De Cuyper, Kostoulas — los tres entre los mejores de su posición ahora mismo) y Arsenal con 3 (Raya, Calafiori, Rice). Ambos al límite de FPL (3), permitido desde que se sacó el límite propio de 2.

## Otros chips — plan

- **Bench Boost:** no todavía, banca sigue floja (Dubravka 0pts, Diop bench fodder, Ballard lesionado, Ampadu suplente). Esperar a que el banco tenga 4 titulares de verdad.
- **Triple Captain:** guardar para doble jornada o fixture soñado de Haaland — nada identificado aún.
- **Free Hit:** guardar para blank gameweek — nada anunciado aún.

## Metodología

Ver `criterio.md` para el modelo completo y las reglas de desempate/exclusión.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API, £100.0m exactos.
- **2026-08-20 (rebuilds 1-2, GK):** Reconstrucción con `criterio.md`; se saca Spurs, entra Tzolis; sale Raya por Lammens (Saliba lesionado).
- **2026-09-04 a 2026-10-10 (reconstruido vía API el 2026-10-23, no registrado en su momento):** David hizo 5 transfers reales en la app sin anotar — entre otros, Calafiori por Gabriel, entraron Hall, Yarmoliuk, Groß, João Pedro, Wissa.
- **2026-10-23 (pre-GW8):** Lammens → Raya, Bruno Fernandes → Mbeumo (datos reales mostraban a Bruno en forma 1.0). Se elimina el límite propio de 2 por club.
- **2026-10-30/31 (pre-GW9, Wildcard):** Diagnóstico integral con datos reales de 8 jornadas detectó 5 problemas (incluyendo a João Pedro, lesionado esta misma semana — no estaba en el radar antes). Se jugó el Wildcard: Hall→De Cuyper, Anderson→Rice, Yarmoliuk→Tavernier, Wissa→Evanilson, João Pedro→Kostoulas. **Se detectó y documentó el problema de sincronización de ramas** (el informe automático del 29 oct seguía hablando de Ballard/Bruno Fernandes, datos de hace semanas) — pendiente que David cambie el default branch en GitHub a `main`, o que el agente apunte explícitamente a `main`.
