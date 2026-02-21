# WhatsApp Automation Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![GHCR](https://img.shields.io/badge/GHCR-Available-blue)

*Automated WhatsApp messaging with GUI support via Docker*

</div>

## Quick Start

### 1) Pull from GitHub Container Registry (GHCR)

```bash
docker pull ghcr.io/yourusername/whatsapp-automation-tool:latest
```

### 2) Run with Docker Compose (includes noVNC GUI)

```bash
# Save this as docker-compose.yml
version: '3.8'
services:
  whatsapp-automation:
    image: ghcr.io/yourusername/whatsapp-automation-tool:latest
    container_name: whatsapp-automation-tool
    environment:
      - PYTHONUNBUFFERED=1
      - DISPLAY=:99
      - BROWSER=chromium-wrapper
      - WHATSAPP_RATE_LIMIT=20
      - LOG_LEVEL=INFO
    ports:
      - "6080:6080"   # noVNC web interface
      - "5900:5900"   # VNC (optional)
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
      - ./output:/app/output
    command: ["sleep", "infinity"]
    restart: unless-stopped
```

```bash
docker-compose up -d
```

### 3) Open the GUI (noVNC)

Navigate to:
```
http://localhost:6080/vnc.html
```

- Chromium will auto-open to WhatsApp Web
- Scan the QR code with your phone
- Keep the tab open

### 4) Send a Test Message

Prepare a CSV file `data/one_lead.csv`:
```csv
Category,Business Name,Phone Number
Test,Test Recipient,+97431013551
```

Run the campaign:
```bash
docker exec -it whatsapp-automation-tool python main.py --leads data/one_lead.csv --template business_proposal
```

## Features

- 📱 Real WhatsApp message sending via WhatsApp Web automation
- 🖥️ GUI access via noVNC in the browser
- 📋 CSV lead list processing with progress tracking
- 🌍 International phone number validation
- 📝 Message templates with variable substitution
- 🧪 Dry-run mode for testing
- 🐳 Dockerized for consistent environments
- 📦 Published to GitHub Container Registry (GHCR)

## Usage Examples

### Dry Run (no messages sent)
```bash
docker exec -it whatsapp-automation-tool python main.py --leads data/leads.csv --template business_proposal --dry-run
```

### List Available Templates
```bash
docker exec -it whatsapp-automation-tool python main.py --list-templates
```

### Validate Phone Numbers
```bash
docker exec -it whatsapp-automation-tool python main.py --validate-leads data/leads.csv
```

### Custom Rate Limit (seconds between messages)
```bash
docker exec -it whatsapp-automation-tool python main.py --leads data/leads.csv --template business_proposal --rate-limit 30
```

## Configuration

Environment variables (override defaults):
```bash
WHATSAPP_RATE_LIMIT=20    # Delay between messages (seconds)
LOG_LEVEL=INFO           # DEBUG, INFO, WARNING, ERROR
BROWSER=chromium-wrapper # Browser to use
```

## Templates

Default template: `business_proposal`
```text
Hello {business_name},

We offer professional services tailored to your needs in the {category} sector.

Would you be interested in discussing how we can help grow your business?

Best regards
Your Team
```

Variables:
- `{business_name}` — from CSV column
- `{category}` — from CSV column

## Development

### Build locally
```bash
git clone https://github.com/yourusername/whatsapp-automation-tool.git
cd whatsapp-automation-tool
docker build -t whatsapp-automation-tool .
```

### Run tests
```bash
docker run --rm whatsapp-automation-tool pytest tests/
```

## Publishing to GHCR

Tag and push:
```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will automatically build and publish the image to:
```
ghcr.io/yourusername/whatsapp-automation-tool:latest
ghcr.io/yourusername/whatsapp-automation-tool:v1.0.0
```

## License

MIT License — see [LICENSE](LICENSE) file.

---

<div align="center">

**⭐ Star this repository if it helped you!**

</div>
