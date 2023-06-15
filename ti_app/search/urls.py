from django.urls import path
from .import views

urlpatterns = [
    path('', views.new_search, name='new_search'),
    path('details_handler', views.details_handler, name='details_handler'),
    path('<str:pk>', views.ProductDetailView.as_view(), name='product-detail')
]
