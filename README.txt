WhatsApp Automation Tool - How It Works
======================================

1) OVERVIEW
-----------
This tool sends WhatsApp messages automatically using WhatsApp Web inside a Docker container.
You provide a CSV file with leads (business name, phone number) and choose a message template.
The tool opens WhatsApp Web in a GUI (noVNC), logs in, and sends messages.

2) SETUP
-------
- Install Docker
- Pull the image from GHCR or build locally
- Run with docker-compose to expose the GUI (ports 6080/5900)
- Open http://localhost:6080/vnc.html in your browser
- Scan the QR code with your phone to log into WhatsApp Web

3) LEADS CSV
------------
Create a CSV file with these columns:
  Category,Business Name,Phone Number
  Test,Test Recipient,+97431013551

Place it in the data/ folder (mounted into the container).

4) TEMPLATES
-----------
Templates are stored in templates/messages.yaml (YAML format).
Each template has:
  - name: Display name
  - subject: Subject (optional)
  - template: Message text with {variable} placeholders
  - variables: List of variables used
  - language: en or ar

You can edit templates/messages.yaml to add/modify templates.

5) SENDING MESSAGES
------------------
From your host terminal (not inside noVNC):
  docker exec -it whatsapp-automation-tool python main.py --leads data/one_lead.csv --template business_proposal

Options:
  --dry-run        Test without sending
  --list-templates Show available templates
  --validate-leads Check phone numbers
  --rate-limit N   Seconds between messages (default 20)

6) TROUBLESHOOTING
-----------------
- If no message arrives: ensure WhatsApp Web is fully logged in and shows chats
- Keep noVNC tab open and Chromium active
- Try sending a manual message inside noVNC first
- Verify the phone number is on WhatsApp

7) DOCKER DETAILS
-----------------
- GUI: noVNC on port 6080 (web), VNC on 5900 (optional)
- Container runs Xvfb + Fluxbox + Chromium + x11vnc + websockify
- Data/logs/output folders are mounted as volumes
- WhatsApp Web auto-opens to https://web.whatsapp.com

8) GHCR (GitHub Container Registry)
----------------------------------
Images are published to ghcr.io/yourusername/whatsapp-automation-tool
Pull with:
  docker pull ghcr.io/yourusername/whatsapp-automation-tool:latest

9) LICENSE
----------
MIT License - see LICENSE file.

10) SUPPORT
-----------
For issues, check the logs in the logs/ folder or container output.
