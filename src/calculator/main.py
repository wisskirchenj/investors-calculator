from sqlalchemy.orm import Session

from crud_handler import CrudHandler
from init_db import init_database
from input_util import menu_choice

MAIN_MENU = '''
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
'''

TOP_TEN_MENU = '''
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
'''

WELCOME_MESSAGE = 'Welcome to the Investor Program!'
NOT_IMPLEMENTED = 'Not implemented!'
BYE_MESSAGE = 'Have a nice day!'


def main_menu() -> int:
    return menu_choice(MAIN_MENU, max_item=2, loop_on_invalid=True)


def top_ten_menu():
    choice = menu_choice(TOP_TEN_MENU, max_item=3)
    if choice not in [0, None]:
        print(NOT_IMPLEMENTED)


def user_entry_loop(session):
    choice = main_menu()
    while choice != 0:
        if choice == 1:
            CrudHandler(session).menu()
        else:
            top_ten_menu()
        choice = main_menu()
    print(BYE_MESSAGE)


def main():
    print(WELCOME_MESSAGE)
    engine = init_database()
    with Session(engine) as session:
        user_entry_loop(session)
        session.commit()


if __name__ == '__main__':
    main()
