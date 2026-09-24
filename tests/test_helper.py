import helper
import pytest


@pytest.mark.parametrize("input_string, expected", [
    ("1994-08-01", "19940801"),
    ("08/01/1994", "08011994"),
    ("08011994", "08011994"),
    ("1994 08 01", "19940801"),
    ("hello", ""),
    ("", "")
])
def test_extract_numeric(input_string, expected):
    assert helper.extract_numeric(input_string) == expected

@pytest.mark.parametrize("date_string, expected", [
    ("Sept 1, 1995", True),
    ("September 1 1995", True),
    ("1 jan 1990", True),
    ("1995-09-01", False),
    ("19950901", False),
    ("hello", False),
    ("", False)
])
def test_has_written_month(date_string, expected):
    assert helper.has_written_month(date_string) == expected

@pytest.mark.parametrize("number, expected", [
    ("19950901", "7"),
    ("199001012", "5"),
    ("12345678", "9"),
])
def test_add_digits(number, expected):
    assert helper.add_digits(number) == expected

@pytest.mark.parametrize("number, expected", [
    ("20090909", "11"),
    ("20000929", "22"),
    ("19991103", "33"),
])
def test_add_digits_master_number(number, expected):
    assert helper.add_digits(number) == expected

@pytest.mark.parametrize("number, expected", [
    ("0", "0"),
    ("7", "7"),
    ("9", "9")
])
def test_add_digits_single_digit(number, expected):
    assert helper.add_digits(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, "Leader"),
    (9, "Humanitarian"),
    (11, "Master Intuitive"),
    (22, "Master Builder"),
    (33, "Master Teacher"),
    (0, None),
    (10, None)
])
def test_get_number_meaning(number, expected):
    assert helper.get_number_meaning(number) == expected

@pytest.mark.parametrize("input_string, expected", [
    ("Jane Doe", "Jane Doe"),
    ("Mary-Jane O'Brien", "MaryJane OBrien"),
    ("Jane123", "Jane"),
    ("José", "Jos"),
    ("Jane  Doe", "Jane  Doe"),
    ("123", ""),
    ("", "")
])
def test_extract_characters(input_string, expected):
    assert helper.extract_characters(input_string) == expected

@pytest.mark.parametrize("word, expected", [
    ("jane", [1, 1, 5, 5]),
    ("JANE", [1, 1, 5, 5]),
    ("abcdefghi", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ("jrs", [1, 9, 1]),
    ("z", [8]),
    ("", [])
])
def test_convert_word_to_number(word, expected):
    assert helper.convert_word_to_number(word) == expected

@pytest.mark.parametrize("word, expected", [
    ("jane", [1, 5]),
    ("DOE", [6, 5]),
    ("lynn", [7]),
    ("brr", []),
    ("", [])
])
def test_convert_word_to_number_only_vowels(word, expected):
    assert helper.convert_word_to_number(word, only_vowels=True) == expected
