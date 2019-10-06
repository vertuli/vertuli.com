from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from .models import Ticker
from .tables import TickerTable
from .filters import TickerFilter


class Home(SingleTableMixin, FilterView):
    template_name = "equities/home.html"
    model = Ticker
    filterset_class = TickerFilter
    table_class = TickerTable
