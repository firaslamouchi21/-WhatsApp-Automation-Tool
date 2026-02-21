"""Tests for phone validator module."""

import pytest
from src.phone_validator import PhoneValidator, PhoneValidationError


class TestPhoneValidator:
    """Test cases for PhoneValidator class."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.validator = PhoneValidator()
    
    def test_valid_phone_numbers(self):
        """Test validation of valid phone numbers."""
        valid_numbers = [
            "+97431691362",  # Qatar
            "+441234567890",  # UK
            "+4915123456789",  # Germany
            "97431691362",    # Qatar without +
            97431691362       # Qatar without + (int)
        ]
        
        for phone in valid_numbers:
            result = self.validator.validate_and_format(phone)
            assert result is not None
            assert result.startswith("+")
    
    def test_invalid_phone_numbers(self):
        """Test validation of invalid phone numbers."""
        invalid_numbers = [
            "",
            "123",
            "abc",
            "+123",
            None,
            "+",
            "123abc456"
        ]
        
        for phone in invalid_numbers:
            result = self.validator.validate_and_format(phone)
            assert result is None
    
    def test_is_valid_number(self):
        """Test is_valid_number method."""
        assert self.validator.is_valid_number("+97431691362")
        assert not self.validator.is_valid_number("invalid")
        assert not self.validator.is_valid_number("")
    
    def test_get_country_code(self):
        """Test country code extraction."""
        assert self.validator.get_country_code("+97431691362") == "974"
        assert self.validator.get_country_code("+441234567890") == "44"
        assert self.validator.get_country_code("+4915123456789") == "49"
        assert self.validator.get_country_code("invalid") is None
    
    def test_phone_number_formatting(self):
        """Test phone number formatting to E.164."""
        result = self.validator.validate_and_format("97431691362")
        assert result == "+97431691362"
        
        result = self.validator.validate_and_format("+97431691362")
        assert result == "+97431691362"
        
        result = self.validator.validate_and_format(" 97431691362 ")
        assert result == "+97431691362"
