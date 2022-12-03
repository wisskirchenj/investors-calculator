from re import match

MAIN_MENU = '''
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
'''

SUB_MENUS = [{"text": '''
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
''', "item_count": 5},
             {"text": '''
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
''', "item_count": 3}]

ENTER_OPTION = 'Enter an option:'
INVALID_OPTION = 'Invalid option!'
NOT_IMPLEMENTED = 'Not implemented!'
BYE_MESSAGE = 'Have a nice day!'


def main_menu() -> int:
    choice = None
    while choice != 0:
        print(MAIN_MENU, ENTER_OPTION, sep='\n')
        choice = input()
        if not match('[012]$', choice):
            print(INVALID_OPTION)
            continue
        return int(choice)


def sub_menu(menu_text: str, item_count: int):
    print(menu_text, ENTER_OPTION, sep='\n')
    choice = input()
    if not match(f'[0-{item_count}]$', choice):
        print(INVALID_OPTION)
    elif int(choice) > 0:
        print(NOT_IMPLEMENTED)


def main():
    choice = main_menu()
    while choice != 0:
        sub_menu(SUB_MENUS[choice - 1].get('text'), SUB_MENUS[choice - 1].get('item_count'))
        choice = main_menu()
    print(BYE_MESSAGE)


if __name__ == '__main__':
    main()
