from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from .models import Products


class ProductLookupView(TemplateView):

    template_name = 'product_lookup/product_lookup.html'

    def post(self, request, *args, **kwargs):
        """
        This method is called when the user submits the form.
        """
        product_name = request.POST['product_name']
        return HttpResponseRedirect(reverse(
            'product_lookup:product_lookup_results',
            args=[product_name])
            )


class ProductLookupResultsView(TemplateView):

    template_name = 'product_lookup/product_lookup_results.html'

    def get_context_data(self, **kwargs) -> dict:

        context = super().get_context_data(**kwargs)
        product_name = kwargs['product_name']

        # Get the first item that matches the query to look for
        # alternatives in databases
        searched_product = Products.objects.filter(
            product_name__icontains=product_name).first()
        context['searched_product'] = searched_product

        # Get the alternatives to the found product

        if searched_product:
            alternatives = Products.objects.filter(
                product_nutriscore__lte=searched_product.product_nutriscore,
                product_category=searched_product.product_category
                ).exclude(
                product_name=searched_product.product_name
                ).order_by('product_nutriscore')
            context['alternatives'] = alternatives
        else:
            context['alternatives'] = None

        return context
