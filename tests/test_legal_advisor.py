import pytest
from src.legal_advisor import generate_legal_advice

def test_generate_legal_advice():
    advice = generate_legal_advice("What is the legal age for marriage?", language="en")
    assert isinstance(advice, str)
    assert len(advice) > 0
