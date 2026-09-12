# Mi equipo — Fantasy Premier League 2026/27

> Este archivo lo mantiene el agente semanal (y David) al día. Cada vez que hagas un cambio real en la app de FPL, actualiza esta lista para que las recomendaciones futuras partan del estado correcto.

- **Team ID en FPL:** 4682544 (equipo "Los Mimomanes")
- **Nota API:** FPL oculta los picks de cualquier equipo hasta que pasa el deadline de esa jornada (regla anti-copia). Desde GW2 en adelante, `https://fantasy.premierleague.com/api/entry/4682544/event/{N}/picks/` devuelve la alineación real ya congelada de la jornada N una vez pasado su deadline — se puede consultar en vivo desde una máquina con internet normal (el entorno cloud de Claude tiene el dominio bloqueado, pero la sesión local de Claude Code sí conecta).
- **Presupuesto usado:** £99.5m / £100.0m (£0.5m libre en el banco)
- **Zona horaria de David:** Panamá (UTC-5, sin horario de verano). A partir de ahora reportar horarios de deadlines en hora de Panamá. El deadline de GW1 (viernes 21 de agosto, 18:30 BST) equivale a **12:30 hora de Panamá** — confirmado con la app real de David, no es un cambio real, solo la conversión.
- **Preferencias de David (además del modelo):** le gusta el Arsenal (desempate solo en igualdad real de condiciones — ver `criterio.md`). No confía en el arranque de temporada del Spurs por ahora ("no sé cómo va a venir ese equipo") — se evitan jugadores del Spurs que vayan a jugar minutos reales, hasta que haya evidencia de cómo empiezan (revisar después de GW1-2, esto no es una regla permanente). **Excepción confirmada:** no aplica al portero suplente — un suplente casi nunca juega, así que ahí se elige por mérito puro. Dubravka (Spurs, £4.0m) es el portero suplente objetivamente mejor a ese precio (96 pts, 21.2% de selección — el resto de opciones a £4.0m tiene 0-6 pts), se queda en la plantilla.
- **Última actualización:** 2026-09-12 (pre-Gameweek 4) — sale Collins (Brentford, fascitis/calf, confirmado fuera hasta después de la fecha FIFA de septiembre por Keith Andrews), entra Muñoz (Nott'm Forest, £5.5m, mismo precio). Ojo: `fpl_precios.csv` tenía a Muñoz con equipo desactualizado (Crystal Palace) — se fue a Nott'm Forest el 30 de agosto (£22m, se reencuentra con Glasner) y el dato ya se corrigió en el CSV.
- 2026-08-20 (pre-Gameweek 1) — sale Xhaka, entra Ampadu (Leeds) para bajar concentración de Sunderland (era 3, ahora 2: Ballard + Brobbey). Confirmado Tzolis titular vs Coventry.
- **Concentración por equipo:** David prefiere no tener 3 jugadores del mismo club aunque el límite de FPL lo permita — si a ese equipo le va mal una semana, pega en varias posiciones a la vez. Revisar cada vez que se arme/ajuste la plantilla.

## Plantilla (15)

| Pos | Jugador | Equipo | Precio | Rol |
|-----|---------|--------|--------|-----|
| GK  | Lammens | Man Utd | £5.0m | Titular |
| GK  | Dubravka | Spurs | £4.0m | Suplente |
| DEF | Gabriel | Arsenal | £8.0m | Titular |
| DEF | Guéhi | Man City | £6.0m | Titular |
| DEF | Ballard | Sunderland | £5.0m | Titular |
| DEF | Muñoz | Nott'm Forest | £5.5m | Titular |
| DEF | Diop | Ipswich Town | £4.0m | Suplente |
| MID | Bruno Fernandes | Man Utd | £12.0m | Titular |
| MID | Anderson | Man City | £6.5m | Titular |
| MID | Ampadu | Leeds | £5.5m | Titular |
| MID | Tzolis | Arsenal | £6.5m | Titular |
| MID | Lewis-Potter | Brentford | £5.5m | Suplente |
| FWD | Haaland | Man City | £15.5m | Titular |
| FWD | Brobbey | Sunderland | £6.0m | Titular |
| FWD | Neave | Newcastle | £4.5m | Suplente |

**Once inicial (4-4-2):** Lammens; Gabriel, Guéhi, Ballard, Muñoz; B.Fernandes, Anderson, Ampadu, Tzolis; Haaland, Brobbey
**Banco:** Dubravka (GK), Diop, Lewis-Potter, Neave
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
- **2026-08-20 (Georginio→Brobbey + limpieza de banca):** A David no le convencía Georginio (Brighton FWD, £5.5m, 87 pts) — sale, entra Brobbey (Sunderland FWD, £6.0m, 92 pts en total pero calendario GW1-3 mucho más fácil: Ipswich A FDR2, Fulham H FDR2, Brentford A FDR3; ya venía anotado como candidato desde el rebuild 1). Costo: +£0.5m. Por separado, David marcó que Amad Diallo en la banca (£6.0m) era caro para un suplente — sale, entra Yarmoliuk (Brentford MID, £5.0m, 104 pts — supera a Amad con 91 pts y cuesta £1.0m menos). También sale Furo (Brentford FWD, £4.5m, 1 pt, 19 años, solo 1 aparición en toda la Premier — casi sin chance real de jugar); entra primero Kusi-Asare (Fulham FWD, £4.5m) pero David lo vetó al enterarse de que está recuperándose de una lesión de rodilla y no fue ni a los amistosos — se reemplaza por **Neave** (Newcastle FWD, £4.5m, sin lesión, ya sumó minutos reales con el primer equipo en Champions League y sigue entrenando con el plantel senior — mejor señal real que el resto de opciones al mismo precio). Los tres cambios calzan con el límite de 3 por equipo: al sacar a Furo (Brentford) se libera el cupo para meter a Yarmoliuk (también Brentford) sin pasarse, junto con Collins y Ajer. Neto: -£0.5m → presupuesto queda en £99.5m/£100.0m, con £0.5m libre en el banco.
- **2026-08-20 (sincronización con la app real):** David compartió captura de su equipo real en la app de FPL y aparecieron dos diferencias con este archivo: (1) el portero suplente era **Dubravka** (Spurs, £4.0m), no Steele — se evaluó si convenía cambiarlo por la regla de "nada de Spurs", pero esa regla aplica a jugadores que suman puntos jugando, no a un suplente que casi nunca entra a la cancha; Dubravka es además objetivamente el mejor portero de £4.0m disponible (96 pts, 21.2% de selección, muy por encima de cualquier alternativa) — se queda, y se documenta la excepción a la regla. (2) el defensa suplente era **Diop** (Ipswich Town, £4.0m) en vez de Ajer (£4.5m) — coincide con lo que ya habíamos identificado como la mejor opción al precio mínimo de defensa; David ya lo había aplicado en la app. Con ambos cambios (Dubravka, misma £4.0m; Diop, -£0.5m vs Ajer) el presupuesto real baja a £99.0m/£100.0m, £1.0m libre. También se confirmó Neave en la banca de delanteros. El archivo queda sincronizado con la app real de David.
- **2026-08-20 (Yarmoliuk→Lewis-Potter):** El informe semanal automático detectó que Brentford fichó a Sangaré (£39-41m, récord del club) para el doble pivote junto a Janelt, dejando a Yarmoliuk fuera de esa posición en pretemporada — plaza de banca "muerta". David pidió confirmar antes de aplicar. Se verificó con dos fuentes: (1) Sangaré+Janelt es el pivote confirmado en los dos amistosos de pretemporada bajo Keith Andrews; (2) Lewis-Potter SÍ aparece en el XI previsto de Brentford para GW1 vs Spurs — juega de lateral izquierdo, pero está clasificado como MID en FPL (£5.5m, 115 pts la temporada pasada), lo que le da acceso a puntos de mediocampista jugando de defensa. Sale Yarmoliuk, entra Lewis-Potter. Costo: +£0.5m (usa el margen libre que quedaba). Presupuesto queda en £99.5m/£100.0m, £0.5m libre.
- **2026-08-20 (Xhaka→Ampadu, reducir concentración de Sunderland):** David marcó que tenía demasiada concentración en Sunderland (Ballard, Xhaka, Brobbey = 3, el máximo permitido) — riesgo real: Sunderland tiene un tramo durísimo en GW4-5 (Arsenal en casa FDR4, Man City de visita FDR5) que pegaría en 3 posiciones a la vez. Xhaka ya venía marcado con duda por el informe de la mañana (no jugó nada de pretemporada). Sale Xhaka, entra **Ampadu** (Leeds, £5.5m, mismo precio — sin impacto en presupuesto) — capitán del Leeds, titular confirmado sin dudas, 134 pts la temporada pasada (supera a Xhaka con 124). Sunderland baja de 3 a 2 jugadores (Ballard + Brobbey). Se confirmó además que Tzolis arranca titular vs Coventry (destacó en la Community Shield con 2 asistencias, sin desgaste de Mundial a diferencia de otros atacantes del Arsenal) — sin cambios ahí. Se agrega regla nueva: David prefiere no superar 2 jugadores del mismo club aunque el límite de FPL sea 3.
