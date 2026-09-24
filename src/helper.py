from calendar import month_abbr
import constants
import re


def get_number_meaning(number) -> str | None:
    """
    Looks up the meaning of a numerology number.
    :param number: A single digit (1-9) or a master number (11, 22, 33).
    :return: The meaning, e.g. "Leader", or None if the number has no meaning.
    """
    return constants.NUMBER_MEANING.get(number)

def extract_numeric(input_string: str) -> str:
    """
    Removes any non-numeric characters from a string.
    :param input_string: The string to clean, e.g. "1995-09-01".
    :return: Only the digits, e.g. "19950901".
    """
    return re.sub("\\D+", "", input_string)

def extract_characters(input_string: str) -> str:
    """
    Removes any characters that are not letters or spaces from a string.
    Spaces are kept so that a full name can still be split into separate names.
    :param input_string: The string to clean, e.g. "Mary-Jane O'Brien".
    :return: Only the letters and spaces, e.g. "MaryJane OBrien".
    """
    return re.sub(r"[^a-zA-Z ]+", "", input_string)

def has_written_month(date_string: str) -> bool:
    """
    Checks whether a string contains a written month of the year, e.g. "Sep" or "September".
    :param date_string: The date to check.
    :return: True if the string contains a month abbreviation, otherwise False.
    """
    return any(m.lower() in date_string.lower() for m in month_abbr[1:])

def add_digits(string_number: str) -> str:
    """
    Recursively adds the digits of a number together until the result is a single digit or a master number.
    :param string_number: The number to reduce, as a string of digits, e.g. "19950901".
    :return: The reduced number as a string, e.g. "7".
    """
    # If number is down to a single digit or master number, exit
    if len(string_number) <= 1 or int(string_number) in constants.MASTER_NUMBERS:
        return string_number
    # Else, split digits and add
    else:
        digits = list(string_number)

        total = 0
        for d in digits:
            total += int(d)

        return add_digits(str(total))

def convert_word_to_number(word, only_vowels=False) -> list[int]:
    """
    Converts each letter of a word to its number on the Pythagorean chart.
    :param word: A single name containing only letters, e.g. "Jane".
    :param only_vowels: If True, only vowels are converted and other letters are skipped.
    :return: The number for each letter, e.g. [1, 1, 5, 5] for "Jane".
    """
    letters = list(word.lower())

    letters_to_numbers = []
    for l in letters:
        if only_vowels and l not in constants.VOWELS:
            continue
        letters_to_numbers.append(constants.PYTHAGOREAN_CHART.get(l))

    return letters_to_numbers




