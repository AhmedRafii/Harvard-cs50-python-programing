import pytest
from fuel import convert, gauge

def main():
    test_correct_input()
    test_zero_division()
    test_value()

def test_correct_input():
    assert convert("1/4") == 25
    assert gauge(25) == "25%"

    assert convert("1/100") == 1
    assert gauge(1) == "E"

    assert convert("99/100") == 99
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()
