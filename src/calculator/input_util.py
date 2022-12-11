from re import match

ENTER_OPTION = 'Enter an option:'
INVALID_OPTION = 'Invalid option!'


def menu_choice(menu_text: str, max_item: int, loop_on_invalid=False,
                invalid_message=INVALID_OPTION, enter_message=ENTER_OPTION) -> int | None:
    print(menu_text, enter_message, sep='\n')
    choice = input()
    while not match(f'\\d+$', choice) or int(choice) > max_item:
        if invalid_message:
            print(invalid_message)
        if not loop_on_invalid:
            return None
        print(menu_text, enter_message, sep='\n')
        choice = input()
    return int(choice)


def user_value_input(key: str, default):
    return input(f"Enter {key} (in the format '{default}'):\n")
