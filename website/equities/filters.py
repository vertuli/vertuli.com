from django_filters import FilterSet, CharFilter, AllValuesFilter


class TickerFilter(FilterSet):
    name = CharFilter(label="Name", lookup_expr="icontains")
    ticker = CharFilter(label="Ticker", lookup_expr="iexact")
    exchange = AllValuesFilter(label="Exchange")
    sector = AllValuesFilter(label="Sector")
    scalemarketcap = AllValuesFilter(label="Marketcap Scale")
    scalerevenue = AllValuesFilter(label="Revenue Scale")
