def is_palindrome(s):
    """Check whether a string reads the same forwards and backwards."""
    return s == s[::-1]


def count_words(text):
    """Count the number of words in a text string."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32
