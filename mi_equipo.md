# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada. Una vez pasado, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real — confirmado que conecta sin problema desde una sesión local de Claude Code (el entorno cloud del agente programado sigue bloqueado, 403 confirmado semana tras semana).
- **⚠️ Problema de sincronización activo:** el agente semanal clona la rama `claude/fantasy-premier-league-values-bp1obf` de GitHub, no `main` — el "default branch" del repo nunca se cambió en la configuración de GitHub (paso manual pendiente de David). Mientras no se cambie, cualquier edición hecha en `main` no la ve el agente hasta que alguien la mergee a la otra rama (se viene haciendo manualmente cada sesión).
- **Zona horaria de David:** Panamá (UTC-5, sin horario de verano). Reportar deadlines siempre en hora de Panamá.
- **Preferencias de David:** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). Sin límite propio de jugadores por club, solo el límite de FPL (máx. 3). Exclusión de Spurs sigue vigente salvo el portero suplente (Dubravka, por mérito).
- **Transfers gratis:** FPL permite bancar hasta 4 extra (5 en total). Revisar `event_transfers`/`event_transfers_cost` en `.../history/` antes de asumir que solo hay 1 disponible.
- **Chips:** **Wildcard #1 usado el 2026-10-31, previo al deadline de GW9.** Quedan: Free Hit, Bench Boost, Triple Captain (1ra mitad, hasta GW19) + el set completo de 4 para la 2da mitad (GW20-38).
- **⚠️ La "forma" es señal débil, no la sobre-pesar** (validado con datos reales el 2026-10-31, r≈0.1-0.16 de correlación con el siguiente partido — ver `criterio.md` sección 11). Priorizar puntos de temporada, minutos garantizados y proyección ajustada por fixture.
- **Última actualización:** 2026-10-31 (pre-Gameweek 9) — Wildcard jugado + ajustes post-wildcard el mismo día (ver historial).

## Plantilla (15) — final para GW9

| Pos | Jugador | Equipo | Precio | Rol GW9 |
|-----|---------|--------|--------|---------|
| GK  | Raya | Arsenal | £6.2m | Titular (Calafiori/Rice 75% — ver abajo) |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Calafiori | Arsenal | £5.9m | Titular (doubt 75%) |
| DEF | Bogle | Leeds | £4.8m | Titular |
| DEF | De Cuyper | Brighton | £5.3m | Titular |
| DEF | Diop | Ipswich Town | £3.9m | Suplente |
| DEF | Hill | Bournemouth | £5.5m | Suplente |
| MID | Mbeumo | Man Utd | £7.9m | Titular — **Vice-capitán** |
| MID | Rice | Arsenal | £7.4m | Suplente (doubt 75% + fixture duro) |
| MID | Tavernier | Bournemouth | £6.5m | Titular |
| MID | Belloumi | Hull City | £5.2m | Titular |
| MID | Groß | Brighton | £6.2m | Titular (David lo prefiere — patea penales) |
| FWD | Haaland | Man City | £15.8m | Titular — **Capitán** |
| FWD | Evanilson | Bournemouth | £6.3m | Titular |
| FWD | Jackson | Aston Villa | £6.9m | Titular |

**Once GW9 final (3-4-3):** Raya; Calafiori, Bogle, De Cuyper; Mbeumo, Tavernier, Belloumi, Groß; Haaland, Evanilson, Jackson
**Banco GW9:** Dubravka (GK), Diop, Hill, **Rice**
**Capitán:** Haaland | **Vice-capitán:** Mbeumo (Man Utd visita Chelsea — defensa confirmada como la más floja de la liga, ver análisis abajo)
**Valor plantilla:** ≈£97.8m usados de ≈£102.3m disponibles (≈£4.5m en banco)
**Jugadores por club (máx. FPL = 3):** Arsenal 3 (Raya, Calafiori, Rice) · Bournemouth 3 (Hill, Tavernier, Evanilson) · Brighton 2 (De Cuyper, Groß) · Leeds 2 (Bogle + banca) · resto 1

**⚠️ Verificar el sábado antes del deadline (06:00 Panamá):** Calafiori al 75% de jugar, titular igual — Arsenal juega DOMINGO 1 nov, no hay forma de tener confirmación 100% antes del deadline de hoy. Riesgo irreducible, no falta de investigación. Rice (también 75% + fixture duro vs Liverpool) se bajó al banco por esto mismo, prefiriendo a Belloumi (más puntos, sin duda, mejor fixture) en su lugar.

**Nota sobre Groß titular:** a pedido de David (es el pateador de penales del Brighton) — pese al fixture duro (Man City fuera, FDR5). Es defendible: 58 pts, el mejor mediocampista de la plantilla por puntos reales, y patea penales es una fuente de puntos real que el modelo de fixture no captura bien.

**Chelsea confirmado como la peor defensa medida hasta ahora** (análisis de goles recibidos ajustado por calidad de rival, ver tabla abajo): 1.88 goles recibidos/partido (el peor crudo) y +3.12 de ajuste (el peor de los tres equipos medidos: Fulham 0.0, Man City -0.4, Chelsea +3.12) — conceden incluso contra ataques flojos (Fulham, Hull). Por eso Mbeumo (Man Utd visita Chelsea) pasa a vice-capitán.

## Por qué cada cambio (datos reales de la temporada, no forma ni proyección de pretemporada)

**Wildcard — titulares:**

| Sale | Entra | Razón |
|---|---|---|
| Hall (£5.3m, 40pts) | De Cuyper (£5.3m, 60pts) | Mismo precio exacto, 20 pts más en la temporada. |
| Anderson (£6.3m, 23pts) | Rice (£7.4m, 39pts) | Anderson nunca rindió lo que prometía el hype pre-temporada. |
| Yarmoliuk (suspendido hasta 8 nov) | Tavernier (£6.5m, 52pts) | Slot muerto en banca → 2do mejor mediocampista real de la liga a ese precio. |
| Wissa (£6.1m, 19pts) | Evanilson (£6.3m, 43pts) | Wissa nunca despegó. |
| João Pedro (£7.9m, 47pts) | Kostoulas (£5.8m, 43pts) | João Pedro se lesionó (muslo, sin fecha de regreso) — no es rendimiento, es que ya no puede jugar. |

**Wildcard — banca:**

| Sale | Entra | Razón |
|---|---|---|
| Diop (£3.9m, 18pts) | Justin (Leeds, £4.5m, 40pts) | +£0.6m por más del doble de puntos. |
| Ballard (lesionado, sin fecha) | Bogle (Leeds, £4.8m, 50pts) | Mismo precio, roster muerto → uno de los defensas más puntudos de la liga a ese precio. |
| Ampadu (£5.3m, 25pts) | Belloumi (Hull City, £5.2m, 43pts) | Casi el doble de puntos, más barato. |

**Post-wildcard, mismo día (31 oct), tras revisión con David:**

| Sale | Entra | Razón |
|---|---|---|
| Guéhi (£6.0m, 37pts) | Hill (£5.5m, 32pts) | A pedido de David. Ojo: con los puntos reales, Hill es el MENOS productivo de los 4 candidatos evaluados (Tarkowski 48, Gvardiol 42, Guéhi 37, Hill 32) — se sostiene solo porque David no quería a Guéhi específicamente, no porque sea la mejor opción por datos. |
| Justin (£4.5m, banca) → **revertido**: Hill pasa a banca, **Bogle entra al XI** | — | Bogle (50 pts) tiene más puntos reales que Hill (32) y que Tarkowski (48) — mejor que comprar un nuevo jugador, con lo que ya se tenía alcanzaba. Gratis, sin transfer. |
| Kostoulas (£5.8m, 43pts) | **Jackson** (Aston Villa, £6.9m, 34pts) | A pedido explícito de David. Por puntos/precio, Kostoulas era mejor (más puntos, más barato) — se documenta la diferencia. Se validó el fixture con un análisis de goles recibidos ajustado por calidad de rival: Man City (rival de Kostoulas) y Fulham (rival de Jackson) resultaron casi iguales en defensa ajustada (Man City ≈-0.4, Fulham ≈0.0) — el FDR5 de Man City exagera la dificultad real, pero no cambia que Jackson entra por preferencia de David, no por ventaja estadística clara. |

**Hallazgo nuevo (2026-10-31): defensa ajustada por calidad de rival.** Mirar solo goles recibidos por un equipo no alcanza — hay que ver CONTRA QUIÉN se los metieron. Ejemplo real: Man City recibió 9 goles en 8 partidos (parece sólido), pero 3 de esos se los metió Sunderland, el ataque más débil de la liga (0.75 goles/partido) — eso es una grieta real que el número crudo esconde. Fórmula casera: para cada partido, `goles_recibidos - goles_por_partido_del_rival`, sumado en la temporada. Positivo = defensa más floja de lo que aparenta; negativo = mejor de lo que aparenta. Pendiente: decidir si esto se formaliza como script reusable (`scripts/analyze_defense_adjusted.py`) o se calcula puntual cuando haga falta.

## Otros chips — plan

- **Bench Boost:** banca con puntos reales ahora (Diop 18, Hill 32, Groß 58 esta semana) pero depende de qué 4 queden en banco cada jornada — evaluar semana a semana, no hay fecha fija todavía.
- **Triple Captain:** guardar para doble jornada o fixture soñado de Haaland — nada identificado aún.
- **Free Hit:** guardar para blank gameweek — nada anunciado aún.

## Metodología

Ver `criterio.md` para el modelo completo, reglas de desempate/exclusión, y la validación de que la forma es señal débil (sección 11).

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API, £100.0m exactos.
- **2026-08-20 (rebuilds 1-2, GK):** Reconstrucción con `criterio.md`; se saca Spurs, entra Tzolis; sale Raya por Lammens (Saliba lesionado).
- **2026-09-04 a 2026-10-10 (reconstruido vía API el 2026-10-23, no registrado en su momento):** David hizo 5 transfers reales en la app sin anotar — entre otros, Calafiori por Gabriel, entraron Hall, Yarmoliuk, Groß, João Pedro, Wissa.
- **2026-10-23 (pre-GW8):** Lammens → Raya, Bruno Fernandes → Mbeumo. Se elimina el límite propio de 2 por club.
- **2026-10-31 (pre-GW9, Wildcard + ajustes):** Wildcard con 8 cambios (Hall→De Cuyper, Anderson→Rice, Yarmoliuk→Tavernier, Wissa→Evanilson, João Pedro→Kostoulas, Diop→Justin, Ballard→Bogle, Ampadu→Belloumi) + Guéhi→Hill a pedido de David. Mismo día, revisión post-wildcard con David: Bogle sube al XI por Hill (gratis, Bogle tiene más puntos), y Kostoulas sale por Jackson a pedido explícito. **Se validó que la "forma" correlaciona débil (r≈0.1-0.16) con el siguiente partido** — downweighted en el criterio desde ahora. **Se construyó un análisis de defensa ajustada por calidad de rival** (goles recibidos vs. lo esperado según el ataque rival) para no guiarse solo por el FDR crudo. **Se detectó el problema de sincronización de ramas** — pendiente que David cambie el default branch en GitHub a `main`.
