from sqlalchemy.orm import Session

from financial import query_top_ten, INDICATOR_KEYS
from input_util import menu_choice

TOP_TEN_MENU = '''
TOP TEN MENU
0 Back
'''
for i in range(len(INDICATOR_KEYS)):
    TOP_TEN_MENU += f'{i + 1} List by {INDICATOR_KEYS[i]}\n'


class TopTenHandler:
    handler = None

    def __new__(cls, session: Session):
        # TopTenHandler implements lazy singleton
        if not cls.handler:
            cls.handler = object.__new__(cls)
        return cls.handler

    def __init__(self, session: Session):
        self.session = session

    def menu(self):
        choice = menu_choice(TOP_TEN_MENU, max_item=3)
        if choice in (0, None):
            return
        self.show_top_ten(choice - 1)

    def show_top_ten(self, index: int):
        indicator_key = INDICATOR_KEYS[index]
        print(f'TICKER {indicator_key}')
        top_indicators = [f'{row[0]} {row[1]}' for row in query_top_ten(indicator_key, self.session)]
        for line in top_indicators:
            print(line)
