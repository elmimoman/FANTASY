# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada. Una vez pasado, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real — confirmado que conecta sin problema desde una sesión local de Claude Code (el entorno cloud del agente programado sigue bloqueado, 403 confirmado semana tras semana).
- **⚠️ Problema de sincronización activo:** el agente semanal clona la rama `claude/fantasy-premier-league-values-bp1obf` de GitHub, no `main` — el "default branch" del repo nunca se cambió en la configuración de GitHub (paso manual pendiente de David, ver nota en el repo). Mientras no se cambie, cualquier edición de este archivo hecha en `main` **no la ve el agente** hasta que alguien la mergee a la otra rama. Ver sección de historial del 2026-10-30 para el caso real donde esto causó un informe con datos de hace 2 meses.
- **Zona horaria de David:** Panamá (UTC-5, sin horario de verano). Reportar deadlines siempre en hora de Panamá.
- **Preferencias de David:** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). Sin límite propio de jugadores por club (eliminado 2026-10-23), solo el límite de FPL (máx. 3). Exclusión de Spurs sigue vigente salvo el portero suplente (Dubravka, por mérito).
- **Transfers gratis:** FPL permite bancar hasta 4 extra (5 en total). Revisar `event_transfers`/`event_transfers_cost` en `.../history/` antes de asumir que solo hay 1 disponible.
- **Chips:** **Wildcard #1 usado el 2026-10-30/31, previo al deadline de GW9.** Quedan: Free Hit, Bench Boost, Triple Captain (1ra mitad, hasta GW19) + el set completo de 4 para la 2da mitad (GW20-38).
- **Última actualización:** 2026-10-31 (pre-Gameweek 9) — Wildcard jugado, 6 cambios (ver historial). Plantilla sincronizada vía API real (picks de GW8).

## Plantilla (15) — post-Wildcard, a jugar para GW9

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Raya | Arsenal | £6.2m | Titular |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Calafiori | Arsenal | £5.9m | Titular (doubt 75% — confirmar sábado) |
| DEF | Hill | Bournemouth | £5.5m | Titular (NUEVO, por Guéhi) |
| DEF | De Cuyper | Brighton | £5.3m | Titular (NUEVO, por Hall) |
| DEF | Justin | Leeds | £4.5m | Suplente (NUEVO, por Diop) |
| DEF | Bogle | Leeds | £4.8m | Suplente (NUEVO, por Ballard) |
| MID | Mbeumo | Man Utd | £7.9m | Titular |
| MID | Groß | Brighton | £6.2m | Titular |
| MID | Rice | Arsenal | £7.4m | Titular (NUEVO, por Anderson; doubt 75% — confirmar sábado) |
| MID | Tavernier | Bournemouth | £6.5m | Titular (NUEVO, por Yarmoliuk) |
| MID | Belloumi | Hull City | £5.2m | Suplente (NUEVO, por Ampadu) |
| FWD | Haaland | Man City | £15.8m | Titular — **Capitán** |
| FWD | Evanilson | Bournemouth | £6.3m | Titular (NUEVO, por Wissa) |
| FWD | Kostoulas | Brighton | £5.8m | Titular (NUEVO, por João Pedro) |

**Once inicial (3-4-3):** Raya; Calafiori, Hill, De Cuyper; Mbeumo, Groß, Rice, Tavernier; Haaland, Evanilson, Kostoulas
**Banco:** Dubravka (GK), Justin, Bogle, Belloumi — banca fuerte a propósito (50/40/43 pts reales), buena para autosubs y deja la puerta abierta a un Bench Boost más adelante
**Capitán:** Haaland | **Vice-capitán:** Mbeumo
**Valor plantilla:** £97.3m usados de £102.3m disponibles (£5.0m en banco)
**Jugadores por club (máx. FPL = 3):** Arsenal 3 (Raya, Calafiori, Rice) · Brighton 3 (Groß, De Cuyper, Kostoulas) · Bournemouth 3 (Hill, Tavernier, Evanilson) · Leeds 2 (Justin, Bogle) · resto 1

**Bournemouth queda con 2 jugadores (Hill + Tavernier + Evanilson = en realidad 3)** — equipo con el mejor arranque de fixtures GW9-12 (avg FDR 2.8) de los candidatos evaluados, por eso aparece 3 veces en la plantilla junto con Brighton (Groß, De Cuyper, Kostoulas) y Arsenal (Raya, Calafiori, Rice).

**⚠️ Verificar el sábado antes del deadline (06:00 Panamá):** Calafiori y Rice están al 75% de jugar (dudas menores, no lesiones serias) — confirmar en la alineación oficial. Si alguno no juega, hay banca de verdad para cubrir ahora (Bogle/Belloumi), no solo bench fodder.

## Por qué cada cambio (datos reales GW1-8, no proyección de pretemporada)

**Titulares:**

| Sale | Entra | Razón |
|---|---|---|
| Hall (£5.3m, 40pts, forma3.0) | De Cuyper (£5.3m, 60pts, forma7.3) | Mismo precio exacto, 20 pts más en la temporada. Upgrade gratis. |
| Guéhi (£6.0m, 37pts, forma2.3) | Hill (£5.5m, 32pts, forma6.7) | A pedido de David — no era un caso tan claro como los demás (Tarkowski/Gvardiol tenían más puntos pero forma igual de fría), pero Hill gana por mejor combo de fixtures (Bournemouth GW9-12, avg FDR 2.8, el mejor de los candidatos) + forma más caliente + más barato. |
| Anderson (£6.3m, 23pts, forma2.7) | Rice (£7.4m, 39pts, forma6.3) | Anderson nunca rindió lo que prometía el hype pre-temporada. |
| Yarmoliuk (suspendido hasta 8 nov) | Tavernier (£6.5m, 52pts, forma7.0) | Slot muerto en banca → 2do mejor mediocampista por puntos reales de toda la liga a ese precio. |
| Wissa (£6.1m, 19pts, forma1.3) | Evanilson (£6.3m, 43pts, forma8.3) | Wissa nunca despegó; Evanilson está en la mejor racha de su posición. |
| João Pedro (£7.9m, 47pts) | Kostoulas (£5.8m, 43pts, forma5.0) | João Pedro salió lesionado (muslo, **sin fecha de regreso confirmada**) — no es que rindiera mal, es que ya no puede jugar. |

**Banca (David preguntó "¿y la banca?" — con el wildcard gratis, no hay razón para dejarla floja):**

| Sale | Entra | Razón |
|---|---|---|
| Diop (£3.9m, 18pts) | Justin (Leeds, £4.5m, 40pts, forma4.7) | +£0.6m por más del doble de puntos. |
| Ballard (lesionado, sin fecha, 14pts) | Bogle (Leeds, £4.8m, 50pts, forma2.7) | Mismo precio, roster muerto → uno de los defensas más puntudos de la liga a ese precio. |
| Ampadu (£5.3m, 25pts, forma1.3) | Belloumi (Hull City, £5.2m, 43pts, forma4.0) | Gomez (Brighton) era mejor opción pero Brighton ya tenía 3 (límite de FPL) — Belloumi es el siguiente mejor sin chocar con el límite. |

**Resultado:** Arsenal, Brighton y Bournemouth quedan con 3 jugadores cada uno (el máximo de FPL) — los tres equipos con mejor rendimiento real entre los candidatos evaluados. Leeds queda con 2 (ambos en banca).

## Otros chips — plan

- **Bench Boost:** ahora sí es viable más adelante — banca real con 50/40/43 pts (Bogle/Justin/Belloumi), ya no es bench fodder. Esperar una jornada donde los 4 titulares de banca tengan buen fixture a la vez.
- **Triple Captain:** guardar para doble jornada o fixture soñado de Haaland — nada identificado aún.
- **Free Hit:** guardar para blank gameweek — nada anunciado aún.

## Metodología

Ver `criterio.md` para el modelo completo y las reglas de desempate/exclusión.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API, £100.0m exactos.
- **2026-08-20 (rebuilds 1-2, GK):** Reconstrucción con `criterio.md`; se saca Spurs, entra Tzolis; sale Raya por Lammens (Saliba lesionado).
- **2026-09-04 a 2026-10-10 (reconstruido vía API el 2026-10-23, no registrado en su momento):** David hizo 5 transfers reales en la app sin anotar — entre otros, Calafiori por Gabriel, entraron Hall, Yarmoliuk, Groß, João Pedro, Wissa.
- **2026-10-23 (pre-GW8):** Lammens → Raya, Bruno Fernandes → Mbeumo (datos reales mostraban a Bruno en forma 1.0). Se elimina el límite propio de 2 por club.
- **2026-10-30/31 (pre-GW9, Wildcard):** Diagnóstico integral con datos reales de 8 jornadas detectó 5 problemas (incluyendo a João Pedro, lesionado esta misma semana). Se jugó el Wildcard, 9 cambios en total: 5 titulares (Hall→De Cuyper, Anderson→Rice, Yarmoliuk→Tavernier, Wissa→Evanilson, João Pedro→Kostoulas), 1 titular más a pedido de David (Guéhi→Hill, caso más parejo), y 3 de banca (Diop→Justin, Ballard→Bogle, Ampadu→Belloumi) tras preguntar "¿y la banca?". **Se detectó y documentó el problema de sincronización de ramas** (el informe automático del 29 oct seguía hablando de Ballard/Bruno Fernandes, datos de hace semanas) — pendiente que David cambie el default branch en GitHub a `main`.
