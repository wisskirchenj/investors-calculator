from sqlalchemy import Column, Float, String, func
from sqlalchemy.orm import Session

from base_metadata import Base
from input_util import user_value_input


class Financial(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)

    def print_financial_indicators(self):
        print('P/E =', none_corrected_float_divide(self.market_price, self.net_profit))
        print('P/S =', none_corrected_float_divide(self.market_price, self.sales))
        print('P/B =', none_corrected_float_divide(self.market_price, self.assets))
        print('ND/EBITDA =', none_corrected_float_divide(self.net_debt, self.ebitda))
        print('ROE =', none_corrected_float_divide(self.net_profit, self.equity))
        print('ROA =', none_corrected_float_divide(self.net_profit, self.assets))
        print('L/A =', none_corrected_float_divide(self.liabilities, self.assets))

    def update(self, updated_values: dict):
        for key, value in updated_values.items():
            self.__setattr__(key, value)


FINANCIAL_DEFAULT_DICT = dict(ebitda=987654321, sales=987654321, net_profit=98765432,
                              market_price=987654321, net_debt=987654321, assets=987654321,
                              equity=987654321, cash_equivalents=987654321, liabilities=987654321)

ND_EBITDA = 'ND/EBITDA'
ROE = 'ROE'
ROA = 'ROA'
INDICATOR_KEYS = [ND_EBITDA, ROE, ROA]

INDICATORS = {
    ND_EBITDA: func.round(Financial.net_debt / Financial.ebitda, 2),
    ROE: func.round(Financial.net_profit / Financial.equity, 2),
    ROA: func.round(Financial.net_profit / Financial.assets, 2)
}


def read_user_input(ticker: str, update=False, session=None) -> Financial:
    new_dict = {'ticker': ticker}
    for key, default in FINANCIAL_DEFAULT_DICT.items():
        new_dict[key] = float(user_value_input(key.replace('_', ' '), default))
    if update:
        get_financial_by_ticker(ticker, session).update(new_dict)
    else:
        return Financial(**new_dict)


def none_corrected_float_divide(f: float | None, g: float | None) -> str:
    if f is None or g is None:
        return 'None'
    return "%.2f" % (f / g)


def get_financial_by_ticker(ticker: str, session: Session) -> Financial:
    return session.query(Financial).filter(Financial.ticker == ticker).scalar()


def query_top_ten(indicator_key: str, session: Session) -> list[tuple]:
    indicator = INDICATORS[indicator_key]
    return session.query(Financial.ticker, indicator).order_by(indicator.desc()).limit(10).all()
