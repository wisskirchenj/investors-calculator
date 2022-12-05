from re import match

ENTER_OPTION = 'Enter an option:'
INVALID_OPTION = 'Invalid option!'


def menu_choice(menu_text: str, max_item: int, loop_on_invalid=False,
                invalid_message=INVALID_OPTION) -> int | None:
    print(menu_text, ENTER_OPTION, sep='\n')
    choice = input()
    while not match(f'[0-{max_item}]$', choice):
        if invalid_message:
            print(invalid_message)
        if not loop_on_invalid:
            return None
        print(menu_text, ENTER_OPTION, sep='\n')
        choice = input()
    return int(choice)
