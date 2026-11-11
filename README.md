# Vincent en Discord

El ingeniero de VINCENT dentro del servidor de Discord:

- **Bienvenida fija**: el primer mensaje de cada persona recibe siempre el mismo saludo (en su idioma), con la descarga, la guía y dónde pedir ayuda.
- **Contesta de verdad**: en `#setup-help` y `#bug-reports` responde a quien abre el post; en el resto de canales, cuando le mencionan o le responden; y por mensaje privado. Si alguien del equipo entra en un hilo, se aparta.
- **Sabe lo que dice**: su conocimiento es la guía oficial y la FAQ de vincent-ai.app (`vincentbot/knowledge.md`). Lo que no sabe, lo deriva al equipo.
- **Protege**: si alguien pega una clave de API, borra el mensaje y le avisa.
- **No te arruina**: máximo 15 respuestas por persona y hora y 600 al día (se cambia con `LIMIT_USER_HOUR` y `LIMIT_DAY`).

Cerebro: Gemini Flash en Vertex AI, pagado con los créditos de Google Cloud (décimas de céntimo por respuesta). Respaldo opcional: Groq gratis.

## Ponerlo en marcha (una vez)

1. **Discord** (developer portal → tu app "Vincent" → *Bot*):
   - Activa **Message Content Intent** y guarda.
   - Copia el **token** del bot. Si ya lo tienes puesto en el conector de Claude, usa ese mismo; si pulsas *Reset Token*, tendrás que actualizarlo también allí.
   - En el servidor, el rol del bot necesita: Ver canales, Enviar mensajes, Enviar mensajes en hilos, Leer el historial y **Gestionar mensajes** (para borrar claves filtradas).
2. **Google Cloud**: abre [Cloud Shell](https://shell.cloud.google.com) con el proyecto que tiene los créditos y pega:
   ```
   bash <(curl -sL https://raw.githubusercontent.com/franzaragoza1/vincent-discord-bot/main/deploy/setup_gcp.sh)
   ```
   Te pedirá el token (y, si quieres, una clave de Groq). En 2–3 minutos Vincent sale en línea.

## Día a día

- **Actualizar** (después de cambiar el código o la guía): `gcloud compute instances reset vincent-bot --zone us-central1-a`
- **Ver qué hace**: `gcloud compute ssh vincent-bot --zone us-central1-a --command 'sudo journalctl -u vincentbot -f'`
- **Regenerar el conocimiento** cuando cambie la guía: `python tools_build_knowledge.py <carpeta vincent-ai-web> vincentbot/knowledge.md`
- **Pruebas**: `pip install -r requirements.txt pytest && pytest -q`
