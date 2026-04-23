#!/usr/bin/env python3

import os
from pathlib import Path
required_files = [
    'app.py',
    'templates/base.html',
    'templates/index.html',
    'templates/vnc_view.html',
    'requirements.txt',
    '__init__.py'
]

print("Checking web UI structure...")
for file in required_files:
    path = Path(file)
    if path.exists():
        print(f"{file} ({path.stat().st_size})")
    else:
        print(f"{file}")
templates_dir = Path('../templates')
if templates_dir.exists():
    lang_dirs = [d for d in templates_dir.iterdir() if d.is_dir()]
    print(f"\n{len(lang_dirs)}")
    for lang_dir in lang_dirs:
        print(f"  - {lang_dir.name}/")
        if (lang_dir / 'it').exists():
            print(f"    - it/")
        if (lang_dir / 'accounting').exists():
            print(f"    - accounting/")
        if (lang_dir / 'work').exists():
            print(f"    - work/")
        if (lang_dir / 'life').exists():
            print(f"    - life/")

print("\nChecking Docker setup...")
dockerfile = Path('../Dockerfile')
if dockerfile.exists():
    print("Dockerfile")
    content = dockerfile.read_text()
    if 'web_ui' in content and 'Flask' in content:
        print("web UI")
        print("✓ web UI")
    else:
        print("✗ web UI")

docker_compose = Path('../docker-compose.yml')
if docker_compose.exists():
    print("✓ docker-compose.yml")
    content = docker_compose.read_text()
    if '5000:5000' in content:
        print("✓ Port 5000")
    else:
        print("✗ Port 5000")

print("\n✅")
print("\nTo run in Docker:")
print("1. docker compose build")
print("2. docker compose up -d")
print("3. http://localhost:5000")
print("4. http://localhost:6080/vnc.html")
