#!/usr/bin/env bash
# Se ejecuta en la máquina cada vez que arranca: instala o actualiza el bot y lo deja corriendo.
set -euo pipefail
MD="http://metadata.google.internal/computeMetadata/v1"
REPO="$(curl -s -H 'Metadata-Flavor: Google' "$MD/instance/attributes/repo")"
PROJECT="$(curl -s -H 'Metadata-Flavor: Google' "$MD/project/project-id")"
DIR=/opt/vincentbot

apt-get update -qq
apt-get install -y -qq git python3-venv >/dev/null

# memoria de intercambio: la e2-micro solo tiene 1 GB
if [ ! -f /swapfile ]; then
  fallocate -l 1G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi

id vincent >/dev/null 2>&1 || useradd --system --home /var/lib/vincentbot --create-home vincent
if [ -d "$DIR/.git" ]; then git -C "$DIR" fetch -q origin main && git -C "$DIR" reset -q --hard origin/main
else git clone -q "$REPO" "$DIR"; fi
[ -d "$DIR/.venv" ] || python3 -m venv "$DIR/.venv"
"$DIR/.venv/bin/pip" install -q --upgrade pip
"$DIR/.venv/bin/pip" install -q -r "$DIR/requirements.txt"

cat > /usr/local/bin/vincentbot-env <<EOF
#!/usr/bin/env bash
# Lee los secretos de Secret Manager al arrancar el servicio (no se guardan en el disco del repo).
set -e
{
  echo "DISCORD_TOKEN=\$(gcloud secrets versions access latest --secret=vincent-discord-token)"
  echo "GROQ_API_KEY=\$(gcloud secrets versions access latest --secret=vincent-groq-key 2>/dev/null || true)"
  echo "GCP_PROJECT=$PROJECT"
  echo "DB_PATH=/var/lib/vincentbot/vincentbot.sqlite3"
} > /run/vincentbot.env
chmod 600 /run/vincentbot.env
EOF
chmod 755 /usr/local/bin/vincentbot-env

cat > /etc/systemd/system/vincentbot.service <<EOF
[Unit]
Description=Vincent Discord bot
After=network-online.target
Wants=network-online.target

[Service]
ExecStartPre=+/usr/local/bin/vincentbot-env
EnvironmentFile=-/run/vincentbot.env
User=vincent
WorkingDirectory=$DIR
ExecStart=$DIR/.venv/bin/python -m vincentbot
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable vincentbot >/dev/null
systemctl restart vincentbot
