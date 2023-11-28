from src.check_number import check_number
import pytest

def test_check_number():
    assert check_number("-22") == "Negative"
    assert check_number("0") == "Zero"
    assert check_number("10") == "Positive"