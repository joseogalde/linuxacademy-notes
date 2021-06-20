def extract_upper(phrase):
    """
    extract_upper takes a string and return a list containing
    only upper-case characters

    >>> extract_upper("Hello There, Bob")
    ['H', 'T', 'B']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    """
    extract_upper takes a string and return a list containing
    only lower-case characters
    
    >>> extract_lower("Hello There, Bob")
    ['e', 'l', 'l', 'o', 'h', 'e', 'r', 'e', 'o', 'b']
    """
    return list(filter(str.islower, phrase))

