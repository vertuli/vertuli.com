from django_tables2 import Table, Column
from django.template.loader import render_to_string


class TickerTable(Table):
    name = Column("Name")
    location = Column("Location", visible=False)
    permaticker = Column("Permaticker", visible=False)
    ticker = Column("Ticker", visible=False)
    secfilings = Column("SEC Filings", visible=False)
    companysite = Column("Company Site", visible=False)
    exchange = Column("Exchange")
    category = Column("Category", visible=False)
    sector = Column("Sector")
    industry = Column("Industry", visible=False)
    scalemarketcap = Column("Marketcap Scale")
    scalerevenue = Column("Revenue Scale")

    @staticmethod
    def render_name(record: dict) -> str:
        context = {"record": record}
        return render_to_string("equities/ticker_table_name.html", context)

    @staticmethod
    def render_exchange(record: dict) -> str:
        context = {"record": record}
        return render_to_string("equities/ticker_table_exchange.html", context)

    @staticmethod
    def render_sector(record: dict) -> str:
        context = {"record": record}
        return render_to_string("equities/ticker_table_sector.html", context)
