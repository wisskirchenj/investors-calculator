from sqlalchemy.orm import Session

import company
import financial
from input_util import menu_choice

CRUD_MENU = '''
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
'''


class CrudHandler:
    handler = None

    def __new__(cls, session: Session):
        # CrudHandler implements lazy singleton
        if not cls.handler:
            cls.handler = object.__new__(cls)
        return cls.handler

    def __init__(self, session: Session):
        self.session = session
        self.menu_functions = (self.create_company, self.read_company, self.update_company,
                               self.delete_company, self.list_all_companies)

    def menu(self):
        choice = menu_choice(CRUD_MENU, max_item=5)
        if choice in (0, None):
            return
        self.menu_functions[choice - 1]()
        self.session.commit()

    def create_company(self):
        new_company = company.read_user_input()
        self.session.add(new_company)
        self.session.add(financial.read_user_input(new_company.ticker))
        print('Company created successfully!')

    def read_company(self):
        chosen_company = company.user_select(self.session)
        if not chosen_company:
            return
        print(chosen_company.ticker, chosen_company.name)
        associate_financial = financial.get_financial_by_ticker(chosen_company.ticker, self.session)
        associate_financial.print_financial_indicators()

    def update_company(self):
        chosen_company = company.user_select(self.session)
        if not chosen_company:
            return
        financial.read_user_input(chosen_company.ticker, update=True, session=self.session)
        print('Company updated successfully!')

    def delete_company(self):
        chosen_company = company.user_select(self.session)
        if not chosen_company:
            return
        self.session.delete(financial.get_financial_by_ticker(chosen_company.ticker, self.session))
        self.session.delete(chosen_company)
        print('Company deleted successfully!')

    def list_all_companies(self):
        print('COMPANY LIST')
        for comp in company.find_all(self.session):
            print(f'{comp.ticker} {comp.name} {comp.sector}')
