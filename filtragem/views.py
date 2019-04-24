from .models import Product
from django.views.generic import DetailView, ListView
from .filters import ProductFilter


class FiltragemListView(ListView):
    model = Product
    template_name = 'Filtragem/filtragem_list.html'

    def get_context_data(self, **kwargs):
        # Dei um super para pegar os dados que esta no meu FiltragemListView
        context = super().get_context_data(**kwargs)
        # peguei o queryset do meu ProductFilter
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        # entreguei ele na response
        return context


class FiltragemDetailView(DetailView):
    model = Product
    template_name = 'Filtragem/filtragem_detail.html'
