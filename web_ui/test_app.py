#!/usr/bin/env python3

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from src.message_templates import MessageTemplateManager
    from src.phone_validator import PhoneValidator
    print("✓")
except ImportError as e:
    print(f"✗ {e}")
    sys.exit(1)

try:
    template_manager = MessageTemplateManager()
    templates = template_manager.list_templates()
    print(f"✓ {len(templates)}")
    
    for i, (id, name) in enumerate(list(templates.items())[:3]):
        print(f"  - {id}: {name}")
except Exception as e:
    print(f"✗ {e}")

try:
    phone_validator = PhoneValidator()
    test_phone = "+1234567890"
    formatted = phone_validator.validate_and_format(test_phone)
    print(f"✓ {test_phone} → {formatted}")
except Exception as e:
    print(f"✗ {e}")

try:
    from app import app
    with app.test_client() as client:
        response = client.get('/')
        print(f"✓ {response.status_code}")
        
        response = client.get('/api/templates')
        if response.status_code == 200:
            print(f"✓ {len(response.json)}")
        else:
            print(f"✗ {response.status_code}")
except Exception as e:
    print(f"✗ {e}")

print("\n✅")
