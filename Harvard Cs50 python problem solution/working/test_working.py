from working import convert
import pytest

# Test the convert function
def test_convert():
    # Valid conversions
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    assert convert("1:00 AM to 1:00 PM") == "01:00 to 13:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

    # Test for Value Errors
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Missing AM/PM
    with pytest.raises(ValueError):
        convert(" to ")  # Empty times
    with pytest.raises(ValueError):
        convert("14:00 AM to 13:00 PM")  # Invalid hours in 12-hour format
    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")  # Invalid 12-hour time
    with pytest.raises(ValueError):
        convert("13 AM to 15 PM")  # Invalid hours without minutes
    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")  # Invalid 12-hour time
    with pytest.raises(ValueError):
        convert("13:67 AM to 7:61 PM")  # Invalid minutes
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")  # Invalid minute values
    with pytest.raises(ValueError):
        convert("9AM to 5PM")  # Missing spaces
    with pytest.raises(ValueError):
        convert("6:19 AM 4:20 PM")  # Missing 'to'

if __name__ == "__main__":
    pytest.main()
