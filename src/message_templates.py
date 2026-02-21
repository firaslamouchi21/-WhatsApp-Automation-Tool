import json
import yaml
from pathlib import Path
from typing import Dict, Any, Optional


class TemplateError(Exception):
    pass


class MessageTemplateManager:
    
    def __init__(self, templates_dir: Optional[Path] = None):
        self.templates_dir = templates_dir or Path("config/templates")
        self.templates: Dict[str, Dict[str, Any]] = {}
        self._load_default_templates()
    
    def _load_default_templates(self):
        templates_file = Path(__file__).parent.parent / "templates" / "messages.yaml"
        self.load_templates_from_file(templates_file)
    
    def load_templates_from_file(self, file_path: Path) -> None:
        if not file_path.exists():
            raise TemplateError(f"Template file not found: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                if file_path.suffix.lower() in ['.yaml', '.yml']:
                    templates = yaml.safe_load(f)
                else:
                    templates = json.load(f)
            
            self.templates.update(templates)
            
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            raise TemplateError(f"Error parsing template file: {e}")
        except Exception as e:
            raise TemplateError(f"Error loading template file: {e}")
    
    def get_template(self, template_name: str) -> Optional[Dict[str, Any]]:
        return self.templates.get(template_name)
    
    def render_template(self, template_name: str, variables: Dict[str, Any]) -> str:
        template_data = self.get_template(template_name)
        if not template_data:
            raise TemplateError(f"Template not found: {template_name}")

        template_text = template_data["template"]
        try:
            return template_text.format_map(variables)
        except KeyError as e:
            raise TemplateError(f"Missing variable in template: {e}")
    
    def list_templates(self) -> Dict[str, str]:
        return {name: data.get("name", name) for name, data in self.templates.items()}
    
    def validate_template(self, template_name: str) -> bool:
        template = self.get_template(template_name)
        if not template:
            return False
        
        required_fields = ["name", "template", "variables", "language"]
        return all(field in template for field in required_fields)
