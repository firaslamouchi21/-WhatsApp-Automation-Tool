
import pytest
from pathlib import Path
from src.message_templates import MessageTemplateManager, TemplateError


class TestMessageTemplateManager:
    
    def setup_method(self):
        self.manager = MessageTemplateManager()
    
    def test_default_templates_loaded(self):
        templates = self.manager.list_templates()
        assert "business_proposal" in templates
        assert "business_proposal_arabic" in templates
    
    def test_get_template(self):
        template = self.manager.get_template("business_proposal")
        assert template is not None
        assert "template" in template
        assert "variables" in template
        assert "language" in template
    
    def test_get_nonexistent_template(self):
        template = self.manager.get_template("nonexistent")
        assert template is None
    
    def test_render_template(self):
        message = self.manager.render_template(
            "business_proposal",
            {"business_name": "Test Business"}
        )
        assert "Test Business" in message
        assert "I'm Firas" in message
    
    def test_render_template_missing_variable(self):
        with pytest.raises(TemplateError):
            self.manager.render_template(
                "business_proposal",
                {}
            )
    
    def test_validate_template(self):
        assert self.manager.validate_template("business_proposal")
        assert not self.manager.validate_template("nonexistent")
    
    def test_load_templates_from_file(self, tmp_path):
        templates_file = tmp_path / "templates.json"
        templates_file.write_text("""
        {
            "test_template": {
                "name": "Test Template",
                "template": "Hello {name}",
                "variables": ["name"],
                "language": "en"
            }
        }
        """)
        
        self.manager.load_templates_from_file(templates_file)
        assert "test_template" in self.manager.list_templates()
    
    def test_load_invalid_file(self, tmp_path):
        invalid_file = tmp_path / "invalid.json"
        invalid_file.write_text("invalid json")
        
        with pytest.raises(TemplateError):
            self.manager.load_templates_from_file(invalid_file)
