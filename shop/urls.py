from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.detail, name='product_detail'),
]