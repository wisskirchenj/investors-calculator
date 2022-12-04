from base_metadata import Base
from sqlalchemy import Column, String


class Company(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)
