from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class ProductLookupView(TemplateView):

    template_name = 'product_lookup/product_lookup.html'

    def get(self, request):
        return render(request, 'product_lookup/product_lookup.html')
