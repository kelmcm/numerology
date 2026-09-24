import lifepath
import pytest


@pytest.mark.parametrize("number, expected", [
    ("19950901", "7"),
    ("199001012", "5"),
    ("12345678", "9"),
])
def test_add_digits(number, expected):
    assert lifepath.add_digits(number) == expected


@pytest.mark.parametrize("number, expected", [
    ("20090909", "11"),
    ("20000929", "22"),
    ("19991103", "33"),
])
def test_add_digits_master_number(number, expected):
    assert lifepath.add_digits(number) == expected


@pytest.mark.parametrize("number, expected", [
    ("0", "0"),
    ("7", "7"),
    ("9", "9")
])
def test_add_digits_single_digit(number, expected):
    assert lifepath.add_digits(number) == expected


