# WhatsApp Automation Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Docker](https://img.shields.io/badge/Docker-Only-blue)
![GHCR](https://img.shields.io/badge/GHCR-Available-blue)

Automated WhatsApp messaging with a browser GUI - runs in Docker on Linux VM

</div>

Bonne journée! ness lkol, This is a simple tool to send automated WhatsApp messages to your leads. It runs entirely in Docker (no installation needed!) and gives you a visual browser interface so you can see what's happening originaly built for myself because I was tired of doing it all of the leads messaging manually.now that i found a job i can focus on improving this tool.for community use. ill be able to release full version in few months.if you wanna help me you can mail me at firaslamou@gmail.com et merci!



////Note important dont exceed 100 messages per day otherwise your  whatsapp account will be banned mine got banned after 40 messages sent in one day ////

## Getting Started

This tool runs in a Docker container on a Linux virtual machine. That means you don't need to install anything on your computer - just Docker kahaw!

### Step 1: Pull the image

```bash
docker pull ghcr.io/firaslamouchi21/whatsapp-automation-tool:latest
```

### Step 2: Run it with Docker Compose

```bash
# Save this as docker-compose.yml
version: '3.8'
services:
  whatsapp-automation:
    image: ghcr.io/firaslamouchi21/whatsapp-automation-tool:latest
    container_name: whatsapp-automation-tool
    environment:
      - PYTHONUNBUFFERED=1
      - DISPLAY=:99
      - BROWSER=chromium-wrapper
      - WHATSAPP_RATE_LIMIT=20
      - LOG_LEVEL=INFO
    ports:
      - "5000:5000"   # Web UI (new!)
      - "6080:6080"   # noVNC web interface
      - "5900:5900"   # VNC (optional)
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
      - ./output:/app/output
      - ./templates:/app/templates  # For custom templates
    command: ["sleep", "infinity"]
    restart: unless-stopped
```

Then start it up:

```bash
docker-compose up -d
```

### Step 3: Open the browser GUI

Now open your browser and go to:

```text
http://localhost:6080/vnc.html
```

You'll see a Chromium browser window inside the container. It should automatically open WhatsApp Web. Just scan the QR code with your phone and you're ready to go!

### Step 4: Use the Web UI (New!)

We've built a beautiful web interface to manage your campaigns:

#### Port 5000 - Campaign Manager UI

`http://localhost:5000`

The web interface lets you:

- **Choose Templates**: Select from pre-made templates in English, French, Arabic, or Tunisian
- **Add Templates**: Create custom templates directly in the UI
- **Manage Leads**: Upload CSV files or type leads manually
- **Preview Messages**: See exactly what your message will look like
- **Launch Campaign**: Click to open WhatsApp Web and start messaging

### Workflow

1. Open `http://localhost:5000`

2. Select a template from the grid

3. Add leads (upload CSV or type them in)

4. Click "Confirm" to see a preview

5. Click "Open WhatsApp Web" to launch the browser

6. Scan the QR code and watch your messages go out!

### Step 5: Send your first message

Create a simple CSV file at `data/one_lead.csv`:

```csv
Category,Business Name,Phone Number
Test,Test Recipient,+97431013551
```

Then run the campaign:

```bash
docker exec -it whatsapp-automation-tool python main.py --leads data/one_lead.csv --template business_proposal
```

## What it can do

- 🎨 **Web Dashboard** - Point-and-click interface to manage everything
- 📱 Send real WhatsApp messages through WhatsApp Web
- 🖥️ Visual browser inside Docker so you can see what's happening
- 🌍 Templates in 4 languages: English, French, Arabic, and Tunisian
- � Upload CSVs or type leads directly in the browser
- 📝 Create custom templates right from the UI
- 🧪 Preview messages before sending
- 🐳 Everything runs in Docker - no installation hassle

## How to use it

### Test without sending (dry run)

Want to see what would happen without actually sending anything?

```bash
docker exec -it whatsapp-automation-tool python main.py --leads data/leads.csv --template business_proposal --dry-run
```

### See available templates

```bash
docker exec -it whatsapp-automation-tool python main.py --list-templates
```

### Check if phone numbers are valid

```bash
docker exec -it whatsapp-automation-tool python main.py --validate-leads data/leads.csv
```

### Change the delay between messages

By default it waits 20 seconds between messages. You can change that:

```bash
docker exec -it whatsapp-automation-tool python main.py --leads data/leads.csv --template business_proposal --rate-limit 30
```

## Configuration

You can tweak these settings in your docker-compose.yml:

```bash
WHATSAPP_RATE_LIMIT=20   # Delay between messages in seconds
LOG_LEVEL=INFO           # DEBUG, INFO, WARNING, or ERROR
SECRET_KEY=change-me     # Flask session key
```

## Message Templates

We've got templates ready to go in 4 languages, organized by category 'hata twensa hsebtlekom 7sebkom':

| Language | Code | Categories                          |
|----------|------|-------------------------------------|
| English  | `en` | IT, Accounting, Work, Life          |
| French   | `fr` | IT, Accounting, Work, Life          |
| Arabic   | `ar` | IT, Accounting, Work, Life          |
| Tunisian | `tn` | IT, Accounting, Work, Life          |

A typical template looks like:

```text
Hello {business_name},

We offer professional services tailored to your needs.

Would you be interested in discussing how we can help grow your business?

Best regards
Your Team
```

Placeholders you can use:
- `{business_name}` - pulled from your CSV or lead form

- `{category}` - pulled from your CSV or lead form

## Building it yourself

If you want to build the Docker image locally instead of pulling from GHCR:

```bash
git clone https://github.com/firaslamouchi21/whatsapp-automation-tool.git
cd whatsapp-automation-tool
docker build -t whatsapp-automation-tool .
```

## Running tests

```bash
docker run --rm whatsapp-automation-tool pytest tests/
```

## Publishing to GHCR

When you're ready to share your changes:

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will automatically build and publish the image to:

```text
ghcr.io/firaslamouchi21/whatsapp-automation-tool:latest
ghcr.io/firaslamouchi21/whatsapp-automation-tool:v1.0.0
```

## License

MIT License - see [LICENSE](LICENSE) file.

## Contributing

Want to help make this better? Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See what's changed in [CHANGELOG.md](CHANGELOG.md).

---

**⭐ Star this repo if it helped you!**

Made with ❤️
