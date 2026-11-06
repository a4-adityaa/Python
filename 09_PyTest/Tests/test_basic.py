
import pytest
import Functions.basic as fctns

def test_add():
    result = fctns.add(10,5)
    assert result == 15

def test_divide():
    result = fctns.divide(10,5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        fctns.divide(10,0)