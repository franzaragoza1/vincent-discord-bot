"""Textos fijos: la bienvenida (siempre la misma) y los avisos."""

GUIDE = "https://vincent-ai.app/guide.html"
SITE = "https://vincent-ai.app"
SETUP = "<#1569619571470504117>"
BUGS = "<#1569619713787428864>"
GEN_ES = "<#1569618799886606356>"

WELCOME = {
    "en": (
        "Radio check, {name} — welcome to the pit wall. 🏁\n"
        f"I'm **Vincent**, the engineer. Download: {SITE} · step-by-step setup: {GUIDE}\n"
        f"Stuck setting up? Open a post in {SETUP} and I'll jump in. Something broken? {BUGS}.\n"
        "You can also just mention me and ask."
    ),
    "es": (
        "Radio check, {name}: bienvenido al muro. 🏁\n"
        f"Soy **Vicen**, el ingeniero. Descarga: {SITE} · guía paso a paso: {GUIDE}\n"
        f"¿Atascado configurándolo? Abre un post en {SETUP} y te echo una mano. ¿Algo roto? {BUGS}.\n"
        f"Para hablar en español tienes {GEN_ES}, y puedes mencionarme cuando quieras."
    ),
}
WELCOME["both"] = WELCOME["en"] + "\n\n🇪🇸 " + WELCOME["es"].split("\n", 1)[1]

LIMIT_USER = {
    "en": "Box box — you've hit my limit for this hour. Back on the radio in a bit; meanwhile the guide has most answers: " + GUIDE,
    "es": "Box box: has llegado a mi límite de esta hora. Vuelvo en un rato; mientras, la guía tiene casi todas las respuestas: " + GUIDE,
}
LIMIT_GLOBAL = {
    "en": "I'm off the radio for today (daily limit). The team will pick this up — and the guide is here: " + GUIDE,
    "es": "Por hoy me quedo sin radio (límite diario). El equipo lo verá, y aquí tienes la guía: " + GUIDE,
}
BRAIN_DOWN = {
    "en": "Lost the radio for a moment — can't think right now. Try again in a minute, or check the guide: " + GUIDE,
    "es": "Se me ha caído la radio un momento. Prueba en un minuto o mira la guía: " + GUIDE,
}
KEY_LEAK = {
    "en": "⚠️ {mention}, that looked like an **API key**, so I removed your message. Treat keys like passwords — "
          "if it was real, revoke it and create a new one (OpenRouter → Keys).",
    "es": "⚠️ {mention}, eso parecía una **clave de API**, así que he borrado tu mensaje. Las claves son como contraseñas: "
          "si era real, revócala y crea otra (OpenRouter → Keys).",
}
KEY_LEAK_NODELETE = {
    "en": "⚠️ {mention}, that looks like an **API key** — please delete your message now, and revoke the key if it was real.",
    "es": "⚠️ {mention}, eso parece una **clave de API**: borra tu mensaje ya y revoca la clave si era real.",
}
