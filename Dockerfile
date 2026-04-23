FROM python:3.11-slim

LABEL maintainer="Firas <contact@example.com>"
LABEL description="WhatsApp Automation Tool"
LABEL version="1.0.0"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    wget \
    git \
    unzip \
    xvfb \
    x11-utils \
    x11-xserver-utils \
    xauth \
    xdg-utils \
    xdotool \
    scrot \
    fluxbox \
    x11vnc \
    novnc \
    websockify \
    chromium \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements-dev.txt

COPY web_ui/ ./web_ui/
COPY src/ ./src/
COPY config/ ./config/
COPY templates/ ./templates/
COPY main.py .
COPY setup.py .

RUN mkdir -p logs data output

# Install web UI dependencies
RUN pip install --no-cache-dir -r web_ui/requirements.txt

ENV DISPLAY=:99

RUN echo '#!/bin/bash\n\
set -e\n\
export DISPLAY=:99\n\
mkdir -p /root\n\
touch /root/.Xauthority\n\
# Start Xvfb\n\
Xvfb :99 -screen 0 1280x720x24 -ac +extension GLX +render -noreset &\n\
sleep 2\n\
# Start Fluxbox\n\
fluxbox &\n\
sleep 1\n\
# Start x11vnc\n\
x11vnc -display :99 -forever -shared -rfbport 5900 -nopw &\n\
sleep 1\n\
# Start websockify for noVNC\n\
websockify --web=/usr/share/novnc 6080 localhost:5900 &\n\
sleep 1\n\
# Start Flask Web UI\n\
cd /app/web_ui && python app.py &\n\
sleep 2\n\
# Start Chromium to WhatsApp Web\n\
chromium --no-sandbox --disable-dev-shm-usage --disable-gpu --window-size=1280,720 --window-position=0,0 https://web.whatsapp.com &\n\
sleep 2\n\
# Keep container running\n\
exec "$@"' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 5000 8000 6080 5900

CMD ["python", "main.py", "--help"]
