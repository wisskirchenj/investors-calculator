# IDEA EDU Course ...

Graduate project implemented in the Track 'SQL with Python' of hyperskill.org's JetBrains Academy.

## Technology / External Libraries

- Python 3.10.8,
- SQLite 3
- SQLAlchemy
- with packages: sqlite3, csv, sqlalchemy, typing, scikit-learn, tox, black and isort

## Repository Contents

The sources of main project tasks (4 stages) and testing.

## Installation

Install the wheel file using pip after clone/fork:

> $ pip install dist/investors-calculator-3.10-py3-none-any.whl

## Program description

The toy project implements a small program that helps investors make a fundamental analysis based on the company's
reports and estimate the company's performance. With this calculator, you can choose the best company in the industry
and decide whether to buy its shares or not..

Have fun!


## Project completion

[Project was completed on 10.11.22.]: #

## Progress

29.11.22 Project started - gitHub repo and project structure setup.

03.12.22 Stage 1 completed: just implementing the menus.

04.12.22 Stage 2 completed: Use SQLAlchemy with declarative ORM-Mapping of Company and Financial (= Financial Instrument)
entities. Use csv.DictReader to read initial csv-data, stored with **dict as keyword-parameters.