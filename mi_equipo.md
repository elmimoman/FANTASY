# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada (regla anti-copia). Desde GW2 en adelante, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real ya congelada de la jornada N una vez pasado su deadline — se puede consultar en vivo desde una máquina con internet normal (el entorno cloud de Claude tiene el dominio bloqueado, pero la sesión local de Claude Code sí conecta).
- **Presupuesto usado:** £99.5m / £100.0m (£0.5m libre en el banco)
- **Última actualización:** 2026-08-20 (pre-Gameweek 1) — sale Georginio, entra Brobbey; sale Amad de la banca (caro para banca), entra Yarmoliuk; sale Furo, entra Kusi-Asare
- **Preferencias de David (además del modelo):** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). No confía en el arranque de temporada del Spurs por ahora ("no sé cómo va a venir ese equipo") — se evitan jugadores del Spurs hasta que haya evidencia de cómo empiezan (revisar después de GW1-2, esto no es una regla permanente).

## Plantilla (15)

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Lammens | Man Utd | £5.0m | Titular |
| GK  | Steele | Brighton | £4.0m | Suplente |
| DEF | Gabriel | Arsenal | £8.0m | Titular |
| DEF | Guéhi | Man City | £6.0m | Titular |
| DEF | Ballard | Sunderland | £5.0m | Titular |
| DEF | Collins | Brentford | £5.5m | Titular |
| DEF | Ajer | Brentford | £4.5m | Suplente |
| MID | Bruno Fernandes | Man Utd | £12.0m | Titular |
| MID | Anderson | Man City | £6.5m | Titular |
| MID | Xhaka | Sunderland | £5.5m | Titular |
| MID | Tzolis | Arsenal | £6.5m | Titular |
| MID | Yarmoliuk | Brentford | £5.0m | Suplente |
| FWD | Haaland | Man City | £15.5m | Titular |
| FWD | Brobbey | Sunderland | £6.0m | Titular |
| FWD | Kusi-Asare | Fulham | £4.5m | Suplente |

**Once inicial (4-4-2):** Lammens; Gabriel, Guéhi, Ballard, Collins; B.Fernandes, Anderson, Xhaka, Tzolis; Haaland, Brobbey
**Banco:** Steele (GK), Ajer, Yarmoliuk, Kusi-Asare
**Capitán por jornada (no es fijo — ver metodología en `criterio.md`):**
- GW1: **Bruno Fernandes** (vs Hull City, FDR2) sobre Haaland (vs Bournemouth, FDR3)
- GW2: **Bruno Fernandes** (vs Ipswich, FDR2) sobre Haaland (fuera vs Crystal Palace, FDR3)
- GW3: **Haaland** (vs Coventry City, FDR2) sobre Bruno (fuera vs Everton, FDR3)

Vice-capitán: el que no sea capitán esa semana, entre Bruno Fernandes y Haaland.

## Metodología

Ver `criterio.md` para el modelo completo y las reglas de desempate/exclusión.

## Discusión abierta (sin decidir todavía)

- **Gabriel, bache GW2-3:** Arsenal juega Aston Villa (fuera) y Chelsea (casa)
  en GW2 y GW3, ambos FDR4 (esto ya no afecta a la portería — Raya salió, entró Lammens,
  que tiene su propio calendario independiente del Arsenal). Desglose real de Gabriel:
  - GW1 vs Coventry (H) FDR2 → 6.0 pts proyectados
  - GW2 vs Aston Villa (A) FDR4 → 3.0 pts proyectados
  - GW3 vs Chelsea (H) FDR4 → 3.0 pts proyectados
  Mirando SOLO GW2+GW3, Guéhi (Man City, ya está en la plantilla) proyecta mejor para ese
  par de fechas específico. Para GW4-6 Arsenal vuelve a fixtures normales (Sunderland,
  Brighton, Leeds), así que es un bache de 2 fechas, no una tendencia. Con 1 solo transfer
  gratis por semana, rotar y volver cuesta caro (-4 o dos transfers "gastados" en un mes).
  **No se decidió nada** — David lo está pensando, opciones sobre la mesa: (a) aguantar el
  bache, (b) rotar a Gabriel afuera para esas 2 fechas y su costo en transfers, (c) esperar
  a ver GW1 real antes de decidir.

- **Calafiori como alternativa a Gabriel:** David mencionó que le tienta meter a Calafiori
  (Arsenal DEF, £5.5m, ep_next=2.5, pts_last=109) en vez de Gabriel (£8.0m, ep_next=4.0,
  pts_last=209). Con el modelo, Calafiori proyecta bastante menos en GW1-3 (7.5 vs 12.0 de
  Gabriel) — Gabriel sigue siendo superior por proyección aún en el bache de fixtures, así
  que el atractivo de Calafiori es más "más barato + libera presupuesto" que rendimiento
  esperado mayor. Sin decidir, queda anotado para la próxima conversación.

- **Lección de proceso:** ver la regla nueva en `criterio.md` sección 2 — nunca presentar
  solo el total de 2-3 fechas sin el desglose semana por semana, porque esconde baches
  reales como este.

## Historial de decisiones

- **2026-08-20:** Plantilla inicial armada con datos reales de la API (595 jugadores), optimizada dentro de £100.0m exactos, máx. 3 jugadores por equipo real.
- **2026-08-20 (rebuild 1):** Plantilla reconstruida de cero aplicando `criterio.md` — proyección propia a 3 jornadas en vez de opiniones de webs.
- **2026-08-20 (rebuild 2):** A pedido de David: (1) se saca a todo jugador del Spurs (Dubravka, Senesi, Richarlison) por desconfianza en su arranque de temporada — no es una exclusión permanente, revisar tras GW1-2; (2) entra Tzolis (Arsenal MID, £6.5m) por pedido directo, aunque el modelo lo proyecta ligeramente por debajo de la opción que salió (Lewis-Potter) — se documenta la diferencia (-0.2 pts proyectados en 3 fechas) para que quede claro que es una decisión de preferencia, no del modelo puro. Entraron también Guéhi (Man City DEF), Ajer y Collins (Brentford DEF), Georginio (Brighton FWD) para reemplazar a los del Spurs con opciones de proyección similar o mejor.
- **2026-08-20 (GK + optimización £1.0m):** A pedido de David, sale Raya (£6.0m) por dudas sobre la defensa del Arsenal sin Saliba (lesionado, 2-3 meses fuera) — entra Lammens (Man Utd, £5.0m), titular confirmado, "Transfer of the Season" de la Premier, fixture GW1 favorable (fuera vs Hull City, recién ascendido). Libera £1.0m. Con ese margen se detectó que Diarra (Sunderland MID, £5.5m, banca, solo 65 pts la temporada pasada) era el eslabón más débil de la plantilla — sale, entra Anderson (Man City MID, £6.5m, 180 pts). Como Anderson (180 pts) supera ampliamente a Amad Diallo (Man Utd MID, £6.0m, 91 pts) que era titular, se invierte el orden: Anderson pasa al 11 titular, Amad al banco. Presupuesto se mantiene exacto en £100.0m.
- **2026-08-20 (Georginio→Brobbey + limpieza de banca):** A David no le convencía Georginio (Brighton FWD, £5.5m, 87 pts) — sale, entra Brobbey (Sunderland FWD, £6.0m, 92 pts en total pero calendario GW1-3 mucho más fácil: Ipswich A FDR2, Fulham H FDR2, Brentford A FDR3; ya venía anotado como candidato desde el rebuild 1). Costo: +£0.5m. Por separado, David marcó que Amad Diallo en la banca (£6.0m) era caro para un suplente — sale, entra Yarmoliuk (Brentford MID, £5.0m, 104 pts — supera a Amad con 91 pts y cuesta £1.0m menos). También sale Furo (Brentford FWD, £4.5m, 1 pt, 19 años, solo 1 aparición en toda la Premier — casi sin chance real de jugar) y entra Kusi-Asare (Fulham FWD, £4.5m, 6 pts, 7.4% de selección — mismo precio, mejor "parking" de emergencia). Los tres cambios calzan con el límite de 3 por equipo: al sacar a Furo (Brentford) se libera el cupo para meter a Yarmoliuk (también Brentford) sin pasarse, junto con Collins y Ajer. Neto: -£0.5m → presupuesto queda en £99.5m/£100.0m, con £0.5m libre en el banco.
