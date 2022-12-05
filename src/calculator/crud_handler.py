from sqlalchemy.orm import Session
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

    def menu(self):
        choice = menu_choice(CRUD_MENU, max_item=5)
        if choice in (0, None):
            return
        print(self.session, choice)
