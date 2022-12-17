from sqlalchemy import Column, String
from sqlalchemy.orm import Session

from base_metadata import Base
from input_util import user_value_input, menu_choice


class Company(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)


COMPANY_DEFAULT_DICT = dict(ticker='MOON', name='Moon Corp', sector='Technology')
DISPLAY_KEY = {'ticker': 'ticker', 'name': 'company', 'sector': 'industries'}


def read_user_input() -> Company:
    new_co = dict()
    for key, default in COMPANY_DEFAULT_DICT.items():
        new_co[key] = user_value_input(DISPLAY_KEY[key], default)
    return Company(**new_co)


def query_company_contains(search_text: str, session: Session) -> list[Company]:
    return session.query(Company).filter(Company.name.ilike(f'%{search_text}%')).all()


def user_select(session: Session) -> Company | None:
    search = input('Enter company name:\n')
    matching = query_company_contains(search, session)
    if not matching:
        print('Company not found!')
        return None
    chosen = menu_choice('\n'.join(f'{i} {company.name}' for i, company in enumerate(matching)),
                         len(matching) - 1, loop_on_invalid=True, enter_message='Enter company number:')
    return matching[chosen]


def find_all(session: Session) -> list[Company]:
    return session.query(Company).order_by(Company.ticker).all()
