from calendar import month_abbr
import re


def extract_numeric(input_string: str):
    """
    Removes any non-numeric characters from a string.
    """
    return re.sub("\\D+", "", input_string)


def has_written_month(date_string: str):
    """
    Checks whether a string contains a substring for a written month of the year.
    :return: Returns true or false if the string contains a month abbreviation.
    """
    return any(m.lower() in date_string.lower() for m in month_abbr[1:])




