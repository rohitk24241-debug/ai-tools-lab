from utils import is_palindrome, count_words, celsius_to_fahrenheit


def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False


def test_count_words():
    assert count_words("Hello AI Tools Lab") == 4
    assert count_words("Python is easy") == 3


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
