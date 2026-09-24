# Numerology

Numerology is the belief that numbers have an impact on our lives.
It outlines ways to compute numbers from characteristics like a birthday or name.

This is a small program around numerology that computes the numbers from your own life.

These algorithms often derive large numbers or words down to a single digit (or a master number), which is a great use case to practice recursion.

## Setup

The program only uses the Python standard library. The setup below installs pytest, which is only needed to run the tests.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Calculating your numbers

Compute your numbers by running:

```bash
cd src && python numerology.py
```

The terminal will prompt for your birthday and full name, then compute your numbers:
```text
Enter your birthday (e.g. YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY):
1968-03-30
Enter your full name:
Celine Dion

Your lifepath number is 3: the Creative.
Your destiny number is 9: the Humanitarian.
Your soul urge number is 7: the Seeker.
```

### Lifepath number

The lifepath number is computed from your birthday and symbolizes your core purpose.

There are different approaches for computing your lifepath number. This program uses the following method:
- Add all digits from your full birthday (year, month, and day)
- Repeat adding digits until you reach either:
  - A single digit number, or
  - A master number

### Destiny number

The destiny number is derived from your name. It represents how you express yourself.

It is computed from your first, middle, and last names:
1. Convert each letter of each name to a number using the [Pythagorean chart](#pythagorean-chart).
2. Add up each name's numbers and reduce the total to a single digit or master number.
3. Add the name totals together and reduce again.

### Soul urge number

The soul urge number represents your inner motivations.
It is computed in a similar way to the destiny number, but only using the _vowels_ of your name.

**Note**: At the moment, "y" is always used as a vowel to compute the soul urge number.
An improvement would be to only count "y" when it is used as a vowel in the name.

### Pythagorean chart

The chart used to convert letters to numbers.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| A | B | C | D | E | F | G | H | I |
| J | K | L | M | N | O | P | Q | R |
| S | T | U | V | W | X | Y | Z |   |

## Input notes

- Birthdays must use numbers only. Written months like "Sept" are rejected.
- Any date format gives the same lifepath number, since the order of the digits does not change their sum.
- Hyphens and apostrophes in names are ignored, so "Mary-Jane" counts as one name.
- Only the letters A to Z are counted, so accented letters (like é or ñ) are dropped.

## Glossary

| Final Number | Meaning          |
|--------------|------------------|
| 1            | Leader           |
| 2            | Diplomat         |
| 3            | Creative         |
| 4            | Builder          |
| 5            | Freedom Seeker   |
| 6            | Nurturer         |
| 7            | Seeker           |
| 8            | Achiever         |
| 9            | Humanitarian     |
| 11           | Master Intuitive |
| 22           | Master Builder   |
| 33           | Master Teacher   |

## Running tests

From the project root:
```bash
pytest
```
