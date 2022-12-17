# IDEA EDU Course ...

Graduate project implemented in the Track 'SQL with Python' of hyperskill.org's JetBrains Academy.

## Technology / External Libraries

- Python 3.11.0,
- SQLite 3
- SQLAlchemy
- with packages: sqlite3, csv, sqlalchemy, typing, scikit-learn, tox, black and isort

## Repository Contents

The sources of main project tasks (4 stages) and testing.

## Installation

Install the wheel file using pip after clone/fork:

> $ pip install dist/investors-calculator-3.11-py3-none-any.whl

## Program description

The toy project implements a small program that helps investors make a fundamental analysis based on the company's
reports and estimate the company's performance. With this calculator, you can choose the best company in the industry
and decide whether to buy its shares or not..

Have fun!


## Project completion

Project was completed on 17.12.22 

## Progress

29.11.22 Project started - gitHub repo and project structure setup.

03.12.22 Stage 1 completed: just implementing the menus.

04.12.22 Stage 2 completed: Use SQLAlchemy with declarative ORM-Mapping of Company and Financial 
(= Financial Analytics Details) entities. Use csv.DictReader to read initial csv-data, stored with **dict 
as keyword-parameters.

11.12.22 Stage 3 completed: Now all the crud menu items are implemented - create, update, delete, list companies and
associated financial indicatives as well as calculate some ratios. Intensely used SQL Alchemy - a great tool !
Implemented lazy singleton for the CrudHandler.

17.12.22 Final Stage 4 completed: A Top Ten Menu is added, whose menu items serve for displaying the TOP 10 performer
companies with regard to some specific predefined indicator (e.g. ROE = Return On Equity). Uses SQL Alchemy's function
generator func (here: func.round()) and more advanced querying, ordering and limiting.