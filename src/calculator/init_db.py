from csv import DictReader
from typing import Type

from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import DeclarativeMeta

import company
import financial
from base_metadata import Base

CSV_COMPANY = 'test/companies.csv'
CSV_FINANCIAL = 'test/financial.csv'


def replace_empty_items_with_none(line: dict[str, str | None]):
    for key in line.keys():
        if line[key] == '':
            line[key] = None


def read_and_insert_csv(session: Session, filepath: str, entity_class: Type[DeclarativeMeta]):
    with open(filepath) as csv_file:
        dict_reader = DictReader(csv_file, delimiter=",")
        for line in dict_reader:
            replace_empty_items_with_none(line)
            session.add(entity_class(**line))


def init_database() -> Engine:
    engine = create_engine('sqlite:///investor.db')
    # if database has 2 tables return else create them from csv
    if len(inspect(engine).get_table_names()) == 2:
        return engine
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        read_and_insert_csv(session, CSV_COMPANY, company.Company)
        read_and_insert_csv(session, CSV_FINANCIAL, financial.Financial)
        session.commit()
    print('Database created successfully!')
    return engine
