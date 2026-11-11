#!/usr/bin/env bash
# Monta a Vincent en Google Cloud. Ejecútalo UNA vez desde Cloud Shell (shell.cloud.google.com):
#   bash <(curl -sL https://raw.githubusercontent.com/franzaragoza1/vincent-discord-bot/main/deploy/setup_gcp.sh)
# Para actualizar el bot más adelante, basta con reiniciar la máquina (se baja la última versión al arrancar):
#   gcloud compute instances reset vincent-bot --zone us-central1-a
set -euo pipefail

REPO="https://github.com/franzaragoza1/vincent-discord-bot"
ZONE="us-central1-a"      # e2-micro en us-central1 entra en el nivel gratuito de Google Cloud
VM="vincent-bot"
SA_NAME="vincent-bot"

PROJECT="$(gcloud config get-value project 2>/dev/null || true)"
if [ -z "$PROJECT" ]; then
  echo "Proyectos disponibles:"; gcloud projects list --format="value(projectId,name)"
  read -rp "ID del proyecto de Google Cloud a usar: " PROJECT
  gcloud config set project "$PROJECT" >/dev/null
fi
echo "==> Proyecto: $PROJECT"

read -rsp "Pega el token del bot de Discord (no se verá al escribir): " DISCORD_TOKEN; echo
read -rsp "Clave de Groq de respaldo (opcional, Enter para saltar): " GROQ_KEY; echo

echo "==> Activando servicios (tarda un minuto la primera vez)"
gcloud services enable compute.googleapis.com aiplatform.googleapis.com secretmanager.googleapis.com

put_secret() {  # nombre valor
  if gcloud secrets describe "$1" >/dev/null 2>&1; then
    printf '%s' "$2" | gcloud secrets versions add "$1" --data-file=- >/dev/null
  else
    printf '%s' "$2" | gcloud secrets create "$1" --replication-policy=automatic --data-file=- >/dev/null
  fi
}
echo "==> Guardando secretos"
put_secret vincent-discord-token "$DISCORD_TOKEN"
[ -n "$GROQ_KEY" ] && put_secret vincent-groq-key "$GROQ_KEY"

SA="$SA_NAME@$PROJECT.iam.gserviceaccount.com"
echo "==> Cuenta de servicio $SA"
gcloud iam service-accounts describe "$SA" >/dev/null 2>&1 || \
  gcloud iam service-accounts create "$SA_NAME" --display-name="Vincent Discord bot"
for role in roles/aiplatform.user roles/secretmanager.secretAccessor roles/logging.logWriter; do
  gcloud projects add-iam-policy-binding "$PROJECT" --member="serviceAccount:$SA" --role="$role" \
    --condition=None >/dev/null
done

echo "==> Máquina $VM"
STARTUP="$(mktemp)"; curl -sL "$REPO/raw/main/deploy/startup.sh" -o "$STARTUP"
if gcloud compute instances describe "$VM" --zone "$ZONE" >/dev/null 2>&1; then
  gcloud compute instances add-metadata "$VM" --zone "$ZONE" --metadata-from-file startup-script="$STARTUP" \
    --metadata repo="$REPO"
  gcloud compute instances reset "$VM" --zone "$ZONE"
else
  gcloud compute instances create "$VM" --zone "$ZONE" --machine-type e2-micro \
    --image-family debian-12 --image-project debian-cloud --boot-disk-size 10GB --boot-disk-type pd-standard \
    --service-account "$SA" --scopes cloud-platform \
    --metadata-from-file startup-script="$STARTUP" --metadata repo="$REPO"
fi

echo
echo "Listo. En 2-3 minutos Vincent aparecerá en línea en Discord."
echo "Ver lo que hace:   gcloud compute ssh $VM --zone $ZONE --command 'sudo journalctl -u vincentbot -f'"
echo "Actualizar:        gcloud compute instances reset $VM --zone $ZONE"
