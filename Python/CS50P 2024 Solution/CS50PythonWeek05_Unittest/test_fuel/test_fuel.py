from fuel import convert, gauge
import pytest
def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    with pytest.raises(ValueError):
        convert('3/2')
def test_outputs():
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
def test_convert():
    assert convert('1/5') == 20
    assert convert('1/2') == 50
    assert convert('0/10') == 0
    assert convert('1/4') == 25
# conftest.py


