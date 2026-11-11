# SETUP GUIDE (English UI names)


## Before you start
- A Windows PC with iRacing .

- Headphones or speakers and a microphone .

- An internet connection. VINCENT's brain, voice and ears run in the cloud.

- A Discord or Google account to sign in, and a Twitch account: VINCENT is free in exchange for following the channel (https://www.twitch.tv/franky_franchicha) .

- An OpenRouter account with a little credit. About $5 is plenty to start. VINCENT itself is free and charges nothing: you pay OpenRouter directly for what you use.

- Optional: a button on your wheel for the radio. Without a wheel you can talk with the Mic button in the app.


## Download and install
- Go to account.vincent-ai.app/download (https://account.vincent-ai.app/download) and sign in with Discord or Google.

- Connect your Twitch account and follow the channel ( twitch.tv/franky_franchicha (https://www.twitch.tv/franky_franchicha) ). If you weren’t following yet, follow on Twitch and press I follow now — check again .

- Download the installer and run it.

- The first time, Windows may show “Windows protected your PC” (SmartScreen). Click More info → Run anyway . It only happens once.

Updates are automatic.
 VINCENT downloads new versions when it opens and installs them when you close it. If you see 
Update to x.x.x
 at the top, click it to update right away.


## Sign in
VINCENT asks you to sign in the first time you open it.

- Click Sign in . Your browser opens.

- Sign in with the same Discord or Google account.

- Check that the code in the browser matches the one in the app and confirm. VINCENT carries on by itself.

Each account works on up to 
3 PCs
. You can manage them at 
account.vincent-ai.app (https://account.vincent-ai.app/)
. If your internet drops, VINCENT keeps working for a few days with your last sign-in.


## Get your OpenRouter key
One key powers everything: the engineer's brain, his voice and his ears.

- Create an account at openrouter.ai (https://openrouter.ai) .

- Open Credits and add some credit. Around $5 lasts a good while.

- Open Keys → Create key . Name it VINCENT and set a credit limit (for example $10).

- Copy the key. It starts with sk-or- . You'll paste it in the next step.

Treat the key like a password.
 Never share it or post it in a screenshot. VINCENT stores it in the Windows Credential Manager and only ever sends it to OpenRouter. With a credit limit, a leaked key can never cost you more than that limit.


## The setup wizard
The first time, VINCENT walks you through these screens. You can change everything later from 
Settings
 at the top of the app.

### General

- Language: English or Spanish, for both the app and the engineer: how he talks, his voice and how he understands you.

- Personality: Classic is dry and direct. Veteran is old school, warm and full of war stories. Same engineer and same strategy; only the character changes.

- Mic button: Hold to talk : hold the button while you speak. Press to toggle : press once to open, press again to close. If you forget, it closes itself after 20 seconds.

### Keys

- Paste your OpenRouter key and press Test . You should see Valid key · balance $… .

- Fish Audio and Deepgram are optional. Only use them if you already have an account there; everything works without them.

### Model

The model decides how smart, and how expensive, your engineer is. These are estimates per hour of racing:

Model | Cost / race hour | Notes

Claude Haiku 5.5 | ≈ $0.08 | Cheapest. A bit flatter and makes more mistakes in unusual situations.

Gemini 3.8 Flash | ≈ $0.47 | Recommended. Quick, witty, varied. The best choice for most people.

GPT 6.1 Terra | ≈ $0.50 | Very fast and careful; says little. Still being tested.

Claude Sonnet 5.5 | ≈ $1.00 | The most powerful, for those who want the very best.

The real cost depends on how much you talk to him and how long the race is. What you've spent shows live at the top of the app. 
Custom
 lets you use any OpenRouter model that supports tool calling.

### Voice

- Press Listen to hear each voice with the radio effect, and pick one. English voices: Vincent , Adrian and Slax . Spanish voices: Antonio and Florencio .

- Listening to a voice for the first time costs a fraction of a cent.

- Advanced: Another Fish voice lets you paste the ID of any voice from fish.audio.

### Listening

How what you say on the radio is turned into text for the engineer:

- In the cloud, with your OpenRouter key (recommended): the most accurate and the fastest. Text is ready about 0.3 s after you let go of the button, for about 2 cents per race hour.

- On your PC : free and offline, but less accurate with racing slang and slower (~1.5 s). It needs a one-off model download and uses some CPU while transcribing.

- Deepgram : real-time, with racing vocabulary. Only if you added a Deepgram key.

### Audio

- Output: where VINCENT speaks (your headphones). Press Test output : you should hear two beeps.

- Input: your microphone. Press Test microphone and talk normally for two seconds. Sounds good means you're done. Very quiet means you should turn up the mic gain in Windows. Nothing coming through means the wrong mic is selected or it's muted.

### Wheel

- Press Detect button , then press the wheel button you want for the radio. You'll see ✓ your wheel · button N .

- No wheel? Skip it and use the Mic button in the app.

### Done

You'll see a summary of everything you chose. Now open iRacing.


## Start a session
- Open iRacing and join a session (practice, qualifying or race). Being in the menus isn't enough.

- In VINCENT, on the Session setup screen, check the options and press START .

### What's on

Turn on whatever you need today. VINCENT remembers your last choice.

Engineer | Vincent reads the race and talks.

Voice | He speaks on the radio. Off: he answers in writing only.

Listening | Mic and wheel button.

Spotter | Instant car left / car right and flag calls.

Tools | Lets him look up standings, manuals and the web.

Twitch chat | Your stream can talk to him (see Streaming ).

Record session | Saves the telemetry so the session can be replayed.

### Team briefing (optional)

For endurance or team events, write him a briefing in plain words: the plan, stint lengths, who drives when, fuel targets. Lines starting with 
//
 are notes for you only. You can edit the briefing during a session and he picks it up on his next turn.

### Radio overlay (optional)

A small label over iRacing that shows when VINCENT is listening, thinking or on air. Pick the screen and position. It only shows if iRacing runs in 
borderless window
 mode, not exclusive full screen.


## Talking to Vincent
Press your radio button, speak, and let go (or press again in toggle mode). You can also type to him in 
Write to Vincent
. Talk to him the way you'd talk to an engineer:

“How's the gap behind?”
“How many laps of fuel have I got?”
“When do I box?”
“Who's quicker, me or the car ahead?”
“Where am I in class?”

### Standing orders

Ask him to remember something and he'll stick to it: 
“remind me to box in three laps”
, 
“don't talk to me in the last two laps”
, 
“tell me if the car behind gets within a second”
. Change or cancel an order the same way.

### How much he talks

Say 
“Vincent, competition mode”
, 
“normal mode”
 or 
“direct mode”
 at any time. In Spanish, “Vicen, modo competición”.

Direct | More colour in quiet spells, more banter. Made for streaming.

Normal | What matters, when it matters.

Competition | Only the essentials. Critical calls always get through.

Set the default in Settings → Advanced → 
How much Vincent talks
.

### The cockpit buttons

Mic | Talk without a wheel.

Mute | Silences the radio until you press it again.

Repeat | Says the last message again.

Bad call | Flags his last message as wrong, with everything he saw at that moment. It helps a lot when you report a bug .

The 
Timing
 tab shows the full timing wall, with sectors, stints and the last five laps of every car. The 
Log
 tab shows what's going on behind the scenes, and has a button to open the logs folder.


## Streaming
### Vincent's voice in OBS

In OBS, add an 
Application Audio Capture
 source and pick the 
VINCENT
 window. If you use Voicemeeter, you can instead send VINCENT's output to one of its inputs (for example 
Voicemeeter In 3
) and route it to the bus OBS captures.

### Stream ticker

A scrolling ticker for your scene. Set a port in Settings → Advanced → 
Stream ticker
, then add a 
Browser source
 in OBS pointing to 
http://localhost:PORT/ticker.html
. Change its message from the cockpit.

### Twitch chat

Your viewers can ask Vincent things in chat, and he can moderate it and run your channel. In 
Settings → Advanced → Twitch chat
, open 
How to set it up, step by step
 for the full walkthrough. In short:

- Create a Twitch account for the bot and make it a moderator: type /mod yourbot in your chat.

- At twitchtokengenerator.com (https://twitchtokengenerator.com) , choose Custom Scope Token . Tick chat:read and chat:edit , plus the moderation scopes if you want him to moderate. Log in with the bot account and copy the Access Token .

- Paste the token, your channel and the bot's username, then enable chat.

- Optional: a second token from your account lets him change the title and category, run predictions and polls, and thank follows, subs and raids.

Viewers talk to him with 
!vincent
. With 
Read the whole chat
 on, he reads every message. He never bans, starts or stops the stream on his own.

### Controlling OBS

In OBS: 
Tools → WebSocket Server Settings → Enable
. Copy the password into Settings → Advanced → OBS and turn on 
Control OBS
. After that, 
“Vincent, go live”
 checks your scene and starts the stream, and 
“Vincent, stop the stream”
 ends it.


## Costs and credit
- VINCENT is free in exchange for following the Twitch channel while you use it. The only cost is AI and voice usage, which you pay straight to OpenRouter.

- What you've spent this session shows live at the top of the app.

- If your credit runs out, the app shows No credit on OpenRouter , the overlay shows NO CREDIT , and Vincent tells you on the radio. Top up at openrouter.ai/credits (https://openrouter.ai/credits) and he's back, with no restart needed.

- A credit limit on your key is the best safety net.


## Troubleshooting
Q: Vincent doesn't answer
A: 
Check the lights at the top of the app. If the LLM light is off or you see 
No credit on OpenRouter
, add credit or raise the key's limit. Also check that 
Engineer
 is on in Session setup.

Q: I can't hear him
A: 
Make sure 
Mute
 isn't on and 
Voice
 is enabled. In Settings → Audio, pick the right output and press 
Test output
.

Q: He doesn't hear me
A: 
In Settings → Audio, pick your mic and press 
Test microphone
. If it says 
Very quiet
, raise the mic gain in Windows. Also check that 
Listening
 is on in Session setup and that your wheel button is set.

Q: The wheel button isn't detected
A: 
Stop the session first: while it runs, the engine is reading the wheel. Then go to Settings → Wheel → 
Detect button
 and press the button.

Q: The timing says “Waiting for iRacing…”
A: 
Join a session in iRacing. The menus aren't enough, and the data only flows once you're in the car or the garage of a session.

Q: I can't see the overlay
A: 
Set iRacing's display to 
borderless window
. Exclusive full screen hides anything drawn on top. Also check the overlay screen in Session setup isn't set to 
Off
.

Q: Sign-in problems
A: 
The code expired
: press Retry and confirm faster. 
Can't reach the account server
: check your connection; VINCENT keeps working offline for a few days. 
This version no longer works
: the new one is downloading by itself.


## Get help and report bugs
Join the 
VINCENT Discord (https://discord.gg/QKNpvAFxPN)
:

- #setup-help for anything about installing or configuring. Include your app version and a screenshot.

- #bug-reports when something's wrong. Press Bad call at the moment it happens, then open the Log tab → Open logs folder and attach the latest log. Blur any keys first.

- #feature-requests for ideas. Vote on the ones you want with 👍.


# GUÍA DE CONFIGURACIÓN (nombres de la interfaz en español)


## Antes de empezar
- Un PC con Windows e iRacing .

- Auriculares o altavoces y un micrófono .

- Conexión a internet: el cerebro, la voz y el oído de Vicen funcionan en la nube.

- Una cuenta de Discord o Google para iniciar sesión y una de Twitch : VINCENT es gratis a cambio de seguir el canal (https://www.twitch.tv/franky_franchicha) .

- Una cuenta de OpenRouter con algo de saldo; con unos 5 $ vas sobrado para empezar. VINCENT es gratis y no cobra nada: lo que uses se lo pagas directamente a OpenRouter.

- Opcional: un botón del volante para la radio. Sin volante, hablas con el botón Micro de la app.


## Descargar e instalar
- Entra en account.vincent-ai.app/download (https://account.vincent-ai.app/download) e inicia sesión con Discord o Google.

- Conecta tu cuenta de Twitch y sigue el canal ( twitch.tv/franky_franchicha (https://www.twitch.tv/franky_franchicha) ). Si aún no lo seguías, síguelo en Twitch y pulsa Ya le sigo, comprobar .

- Descarga el instalador y ábrelo.

- La primera vez Windows puede decir «Windows protegió su PC» (SmartScreen). Pulsa Más información → Ejecutar de todas formas . Solo pasa una vez.

Se actualiza solo.
 VINCENT descarga las versiones nuevas al abrirse y las instala al cerrarlo. Si arriba ves 
Actualizar a x.x.x
, púlsalo para hacerlo al momento.


## Iniciar sesión
La primera vez que abres VINCENT te pide entrar.

- Pulsa Iniciar sesión : se abre el navegador.

- Entra con la misma cuenta de Discord o Google.

- Comprueba que el código del navegador es el mismo que el de la app y confirma. VINCENT sigue solo.

Cada cuenta funciona en hasta 
3 PCs
, que gestionas en 
account.vincent-ai.app (https://account.vincent-ai.app/)
. Si se te cae internet, sigue funcionando unos días con tu último inicio de sesión.


## Saca tu clave de OpenRouter
Con una sola clave funciona todo: el cerebro del ingeniero, su voz y su oído.

- Crea una cuenta en openrouter.ai (https://openrouter.ai) .

- Entra en Credits y añade saldo; con unos 5 $ tienes para rato.

- Entra en Keys → Create key , llámala VINCENT y ponle un límite de crédito (por ejemplo 10 $).

- Copia la clave (empieza por sk-or- ). La pegarás en el siguiente paso.

Trátala como una contraseña.
 No la compartas ni la enseñes en capturas. VINCENT la guarda en el Administrador de credenciales de Windows y solo se la envía a OpenRouter. Con el límite de crédito, una clave filtrada nunca te costará más que ese límite.


## El asistente de configuración
La primera vez, VINCENT te lleva por estas pantallas. Todo se puede cambiar después desde 
Ajustes
, arriba en la app.

### General

- Idioma: español o inglés, de la app y del ingeniero: cómo habla, su voz y cómo te entiende.

- Personalidad: Clásico , seco y directo; Veterano , de la vieja escuela, cálido y con batallitas. Mismo ingeniero y misma estrategia; solo cambia el carácter.

- Botón del micro: Mantener pulsado (hablas mientras lo aprietas) o Pulsar y otra vez para cerrar . Si se te olvida cerrarlo, se cierra solo a los 20 segundos.

### Claves

- Pega tu clave de OpenRouter y pulsa Probar . Debe salir Clave válida · saldo $… .

- Fish Audio y Deepgram son opcionales: úsalas solo si ya tienes cuenta. Sin ellas funciona todo.

### Modelo

Decide cómo de listo (y de caro) es tu ingeniero. Estimaciones por hora de carrera:

Modelo | Coste / hora | Notas

Claude Haiku 5.5 | ≈ 0,08 $ | El más barato. Algo más plano y se equivoca más en situaciones raras.

Gemini 3.8 Flash | ≈ 0,47 $ | Recomendado. Rápido, con chispa y variedad. La mejor opción para casi todos.

GPT 6.1 Terra | ≈ 0,50 $ | Muy rápido y prudente; habla poco. Aún en pruebas.

Claude Sonnet 5.5 | ≈ 1,00 $ | El más potente, para quien quiere lo máximo.

El coste real depende de cuánto hables con él y de lo larga que sea la carrera; lo que llevas gastado se ve en directo arriba en la app. 
Personalizado
 admite cualquier modelo de OpenRouter compatible con herramientas.

### Voz

- Pulsa Escuchar para oír cada voz con el efecto de radio y elige. En español: Antonio y Florencio . En inglés: Vincent , Adrian y Slax .

- Escuchar una voz por primera vez gasta una fracción de céntimo.

- Avanzado: Otra voz de Fish te deja pegar el ID de cualquier voz de fish.audio.

### Escucha

Cómo se convierte en texto lo que dices por radio:

- En la nube, con tu clave de OpenRouter (recomendado): la más precisa y rápida, texto listo unos 0,3 s después de soltar el botón, por unos 2 céntimos por hora de carrera.

- En tu PC : gratis y sin conexión, pero menos precisa con la jerga y más lenta (~1,5 s). Hay que descargar un modelo una vez y usa algo de CPU al transcribir.

- Deepgram : en tiempo real y con vocabulario de carrera. Solo si añadiste clave de Deepgram.

### Audio

- Salida: por dónde habla VINCENT (tus auriculares). Pulsa Probar salida : tienes que oír dos pitidos.

- Entrada: tu micrófono. Pulsa Probar micrófono y habla normal dos segundos. Se oye bien : listo. Se oye muy bajo : sube la ganancia del micro en Windows. No se oye nada : micro equivocado o silenciado.

### Volante

- Pulsa Detectar botón y aprieta el botón del volante que quieres para la radio. Verás ✓ tu volante · botón N .

- ¿Sin volante? Sáltalo y usa el botón Micro de la app.

### Listo

Verás un resumen de todo lo que has elegido. Ahora abre iRacing.


## Arrancar una sesión
- Abre iRacing y entra en una sesión (entreno, clasificación o carrera). Estar en los menús no basta.

- En VINCENT, en Preparar sesión , revisa las opciones y pulsa ARRANCAR .

### Qué se enciende

Activa lo que necesites hoy; se recuerda lo último que usaste.

Ingeniero | Vicen analiza la carrera y habla.

Voz | Habla por la radio. Apagado: contesta solo por escrito.

Escucha | Micro y botón del volante.

Spotter | Avisos al momento de coche a la izquierda/derecha y banderas.

Herramientas | Le deja consultar clasificaciones, manuales y la web.

Chat de Twitch | Tu directo puede hablarle (mira Directos ).

Grabar sesión | Guarda la telemetría para poder reproducirla.

### Briefing de equipo (opcional)

Para resistencias o carreras por equipos, escríbele un briefing con tus palabras: el plan, la duración de los stints, quién conduce cuándo, objetivos de gasolina. Las líneas que empiezan por 
//
 son notas tuyas. Puedes editarlo con la sesión en marcha y lo lee en su siguiente turno.

### Overlay de radio (opcional)

Una etiqueta pequeña encima de iRacing que indica cuándo VINCENT te escucha, piensa o está en el aire. Elige pantalla y posición. Solo se ve si iRacing va en 
ventana sin bordes
, no en pantalla completa exclusiva.


## Hablar con Vicen
Pulsa el botón de radio, habla y suelta (o vuelve a pulsar si usas el modo de pulsar y cerrar). También puedes escribirle en 
Escribir a Vicen
. Háblale como a un ingeniero:

«¿Cómo va el de detrás?»
«¿Cuántas vueltas de gasolina me quedan?»
«¿Cuándo paro?»
«¿Quién va más rápido, yo o el de delante?»
«¿Cómo voy en mi clase?»

### Órdenes

Pídele que recuerde algo y lo cumplirá: 
«avísame para entrar dentro de tres vueltas»
, 
«no me hables en las dos últimas vueltas»
, 
«dime si el de detrás se pone a menos de un segundo»
. Para cambiarla o anularla, díselo igual.

### Cuánto habla

Di 
«Vicen, modo competición»
, 
«modo normal»
 o 
«modo directo»
 cuando quieras. En inglés también vale: «Vincent, competition mode».

Directo | Más color en los tramos tranquilos y más juego. Pensado para directos.

Normal | Lo importante, cuando importa.

Competición | Solo lo esencial. Los avisos críticos siempre llegan.

El modo por defecto se elige en Ajustes → Avanzado → 
Cuánto habla Vicen
.

### Los botones de la cabina

Micro | Hablar sin volante.

Silenciar | Silencia la radio hasta que lo vuelvas a pulsar.

Repetir | Repite el último mensaje.

Fallo | Marca su último mensaje como erróneo, con todo lo que veía en ese momento. Ayuda mucho para reportar un fallo .

La pestaña 
Timing
 es el muro de tiempos completo (sectores, stints, últimas cinco vueltas de cada coche). La pestaña 
Registro
 muestra lo que pasa por dentro y tiene un botón para abrir la carpeta de logs.


## Directos
### La voz de Vicen en OBS

En OBS añade una fuente 
Captura de audio de aplicación
 y elige la ventana 
VINCENT
. Si usas Voicemeeter, también puedes mandar la salida de VINCENT a una de sus entradas (p. ej. 
Voicemeeter In 3
) y llevarla al bus que captura OBS.

### Letrero para el stream

Un rótulo que se desplaza para tu escena. Pon un puerto en Ajustes → Avanzado → 
Letrero para el stream
 y en OBS añade una 
Fuente de navegador
 con 
http://localhost:PUERTO/ticker.html
. El mensaje se cambia desde la cabina.

### Chat de Twitch

Tus espectadores pueden preguntarle cosas a Vicen por el chat, y él puede moderarlo y manejar tu canal. En 
Ajustes → Avanzado → Chat de Twitch
 abre 
Cómo se configura, paso a paso
 para la guía completa. Resumido:

- Crea una cuenta de Twitch para el bot y hazla moderadora: escribe /mod tubot en tu chat.

- En twitchtokengenerator.com (https://twitchtokengenerator.com) elige Custom Scope Token , marca chat:read y chat:edit (y los de moderar si quieres que modere), entra con la cuenta del bot y copia el Access Token .

- Pega el token, tu canal y el usuario del bot, y activa el chat.

- Opcional: un segundo token de tu cuenta le deja cambiar título y categoría, hacer predicciones y encuestas y agradecer follows, subs y raids.

Los espectadores le hablan con 
!vicen
; con 
Leer todo el chat
, lee todos los mensajes. Nunca banea, arranca ni para el directo por su cuenta.

### Controlar OBS

En OBS: 
Herramientas → Ajustes del servidor WebSocket → Activar
. Copia la contraseña en Ajustes → Avanzado → OBS y activa 
Controlar OBS
. Después, 
«Vicen, arranca directo»
 revisa tu escena y empieza a emitir, y 
«Vicen, para el directo»
 lo corta.


## Costes y saldo
- VINCENT es gratis a cambio de seguir el canal de Twitch mientras lo uses. El único gasto es el uso de IA y voz, que pagas directamente a OpenRouter.

- Lo que llevas gastado en la sesión se ve en directo arriba en la app.

- Si se acaba el saldo, la app muestra Sin saldo en OpenRouter , el overlay pone SIN SALDO y Vicen te lo dice por radio. Recarga en openrouter.ai/credits (https://openrouter.ai/credits) y vuelve sin reiniciar nada.

- Un límite de crédito en la clave es tu mejor red de seguridad.


## Problemas frecuentes
Q: Vicen no contesta
A: 
Mira los indicadores de arriba en la app. Si el de LLM está apagado o ves 
Sin saldo en OpenRouter
, añade saldo o sube el límite de la clave. Comprueba también que 
Ingeniero
 está activado en Preparar sesión.

Q: No le oigo
A: 
Comprueba que 
Silenciar
 no está puesto y que 
Voz
 está activada. En Ajustes → Audio, elige la salida correcta y pulsa 
Probar salida
.

Q: No me oye
A: 
En Ajustes → Audio, elige tu micro y pulsa 
Probar micrófono
. Si dice 
muy bajo
, sube la ganancia en Windows. Comprueba que 
Escucha
 está activada y que el botón del volante está configurado.

Q: No detecta el botón del volante
A: 
Detén antes la sesión: mientras está en marcha, el motor está leyendo el volante. Luego Ajustes → Volante → 
Detectar botón
 y aprieta el botón.

Q: El timing dice «Esperando a iRacing…»
A: 
Entra en una sesión en iRacing. En los menús no hay datos: solo llegan cuando estás en el coche o en el garaje de una sesión.

Q: No veo el overlay
A: 
Pon iRacing en 
ventana sin bordes
; la pantalla completa exclusiva tapa todo lo que se dibuja encima. Revisa también que la pantalla del overlay no esté en 
Apagado
.

Q: Problemas al iniciar sesión
A: 
El código ha caducado
: pulsa Reintentar y confirma antes. 
Sin conexión con el servidor de cuentas
: revisa internet; sigue funcionando unos días sin conexión. 
Esta versión ya no funciona
: la nueva se está descargando sola.


## Ayuda y reportar fallos
Entra en el 
Discord de VINCENT (https://discord.gg/QKNpvAFxPN)
:

- #setup-help para todo lo de instalar y configurar. Indica tu versión y añade una captura.

- #bug-reports si algo va mal. Pulsa Fallo en el momento, abre la pestaña Registro → Abrir carpeta de logs y adjunta el último log (tapa antes cualquier clave).

- #feature-requests para ideas; vota con 👍 las que quieras.

Para escribir en español tienes el canal #general-es: elige «Español» al entrar.


# WEBSITE FAQ (English)
Q: Can I use it in official races?
A: Yes — that’s what it’s built for. VINCENT works like the spotter and overlay apps drivers already use in official races: it only reads the telemetry iRacing exposes to every app, and talks to you. It never touches the car or the sim.

Q: Is it really free?
A: Yes. VINCENT costs nothing and has no paid version — all I ask is that you follow my Twitch channel, and you keep following while you use it. The only cost is the AI and voice usage, which you pay straight to OpenRouter — I don’t get a cent of it.

Q: How much does a race cost to run?
A: It depends on the AI model you pick in settings: cheaper models cost cents per race, the best ones a bit more. The app shows your spend live, so there are no surprises.

Q: What do I need?
A: A Windows PC, iRacing, a microphone, an internet connection and a Discord or Google account to sign in. Plus one OpenRouter API key — the setup wizard walks you through it.

Q: Why do I need to sign in?
A: To download VINCENT and to use it. It tells us who’s using it, stops anyone reselling it, and lets us switch off a broken version fast. Each account works on up to 3 PCs, which you can manage from your account. If your internet drops mid-race, it keeps working.

Q: Where does my API key go?
A: It’s stored in the Windows Credential Manager on your PC and only ever sent to OpenRouter. It never reaches us. Tip: create a key just for VINCENT and give it a credit limit in OpenRouter, so a lost key can never cost you more than that.

Q: Which sims does it support?
A: iRacing only, for now.

Q: Windows says “unknown publisher”
A: The first time, SmartScreen may warn you. Click More info → Run anyway. After that VINCENT updates itself: it downloads new versions when it opens and installs them when it closes.

# FAQ DE LA WEB (español)
P: ¿Se puede usar en carreras oficiales?
R: Sí, para eso está hecho. VINCENT funciona como las apps de spotter y overlays que los pilotos ya usan en oficiales: solo lee la telemetría que iRacing ofrece a cualquier aplicación y te habla. Nunca toca el coche ni el simulador.

P: ¿De verdad es gratis?
R: Sí. VINCENT no cuesta nada y no tiene versión de pago: solo te pido que sigas mi canal de Twitch mientras lo uses. El único gasto es el uso de IA y voz, que pagas directamente a OpenRouter; a mí no me llega ni un céntimo.

P: ¿Cuánto cuesta cada carrera?
R: Depende del modelo de IA que elijas en ajustes: los más baratos cuestan céntimos por carrera y los mejores algo más. La app te enseña el gasto en directo, así que no hay sorpresas.

P: ¿Qué necesito?
R: Un PC con Windows, iRacing, un micrófono, conexión a internet y una cuenta de Discord o Google para entrar. Y una clave de OpenRouter: el asistente te guía para sacarla.

P: ¿Por qué hay que iniciar sesión?
R: Para descargar VINCENT y para usarlo. Así sabemos quién lo usa, evitamos que alguien lo revenda y podemos retirar rápido una versión con fallos. Cada cuenta funciona en hasta 3 PCs, que gestionas desde tu cuenta. Si se te cae internet en plena carrera, sigue funcionando.

P: ¿Dónde va mi clave de API?
R: Se guarda en el Administrador de credenciales de Windows de tu PC y solo se envía a OpenRouter. Nunca nos llega. Consejo: crea una clave solo para VINCENT y ponle un límite de crédito en OpenRouter; así una clave perdida nunca te costará más que eso.

P: ¿Qué simuladores soporta?
R: Solo iRacing, de momento.

P: Windows dice «editor desconocido»
R: La primera vez, SmartScreen puede avisarte. Pulsa Más información → Ejecutar de todas formas. Después VINCENT se actualiza solo: descarga la versión nueva al abrirse y la instala al cerrarse.
