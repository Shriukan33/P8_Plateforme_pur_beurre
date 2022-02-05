from django.urls import path
from .views import ProductLookupView, ProductLookupResultsView

app_name = 'product_lookup'

urlpatterns = [
    path('', ProductLookupView.as_view(), name='product_lookup'),
    path('search/<str:product_name>', ProductLookupResultsView.as_view(),
         name='product_lookup_results'),
]
