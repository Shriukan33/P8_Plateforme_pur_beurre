from django.urls import path
from .views import ProductLookupView

urlpatterns = [
    path('', ProductLookupView.as_view(), name='product_lookup'),
]
