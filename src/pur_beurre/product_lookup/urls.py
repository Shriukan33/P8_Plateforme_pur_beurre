from django.urls import path
from .views import ProductLookupView

app_name = 'product_lookup'

urlpatterns = [
    path('', ProductLookupView.as_view(), name='product_lookup'),
]
