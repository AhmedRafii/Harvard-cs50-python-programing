import pytest
from um import count

def test_count_basic():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_count_with_punctuation():
    assert count("um,") == 1
    assert count("um.") == 1
    assert count("um!") == 1
    assert count("hello, um, world") == 1

def test_count_as_substring():
    assert count("yummy") == 0
    assert count("aluminum") == 0

def test_count_multiple_occurrences():
    assert count("um um") == 2
    assert count("Um um UM") == 3

def test_count_with_other_words():
    assert count("hello um world") == 1
    assert count("um hello um world um") == 3

if __name__ == "__main__":
    pytest.main()
