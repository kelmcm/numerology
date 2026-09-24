# Numerology

Numerology is the belief that numbers have an impact on our lives. 
It outlines ways to compute numbers from characteristics like a birthday or name.

This is a collection of small programs around numerology that help compute the numbers in your own life.

These algorithms often derive large numbers or words down to a single digit, which is a great use case to practice recursion. 

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Calculating your numbers

### Lifepath number

A lifepath number is computed from your birthday and symbolizes your core purpose. 

There are different approaches for computing your lifepath number, but in this program we take the approach: 
- Add all digits from your full birthday (year, month, and day)
- Repeat adding digits until you reach either:
  - A single digit number, or
  - A master number

Run by: 
```bash
cd src && python lifepath.py
```

The terminal will prompt for your birthday and compute your lifepath number:
```text
What is your birthday (e.g. YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY)?
2025-03-15

2 + 0 + 2 + 5 + 0 + 3 + 1 + 5
=  18
1 + 8
=  9

Your lifepath number is 9: the Humanitarian.
```

### Desire number

Coming soon.


### Soul urge number

Coming soon.


## Glossary

| Number | Meaning        |
|--------|----------------|
| 1      | Leader         |
| 2      | Diplomat       |
| 3      | Creative       |
| 4      | Builder        |
| 5      | Freedom Seeker |
| 6      | Nurturer       |
| 7      | Seeker         |
| 8      | Achiever       |
| 9      | Humanitarian   |
| 11     | Master Intuitive |
| 22     | Master Builder |
| 33     | Master Teacher |


## Running tests

To run tests, run from project root: 
```bash
pytest
```
