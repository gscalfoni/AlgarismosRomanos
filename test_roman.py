import pytest
from main import int_to_roman

def test_single_digits():
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"

def test_double_digits():
    assert int_to_roman(10) == "X"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(90) == "XC"

def test_triple_digits():
    assert int_to_roman(100) == "C"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(900) == "CM"

def test_large_numbers():
    assert int_to_roman(1987) == "MCMLXXXVII"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_out_of_range():
    with pytest.raises(ValueError):
        int_to_roman(0)  # Números romanos começam em 1
    with pytest.raises(ValueError):
        int_to_roman(4000)  # Máximo representável em números romanos é 3999
