
__version__ = "1.0.0"
__author__ = "Firas"
__email__ = "contact@example.com"

from .whatsapp_automation import WhatsAppAutomation
from .phone_validator import PhoneValidator
from .message_templates import MessageTemplateManager

__all__ = [
    "WhatsAppAutomation",
    "PhoneValidator",
    "MessageTemplateManager"
]
