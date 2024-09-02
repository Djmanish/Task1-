from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/',                    admin.site.urls),
    path('api/products/',             views.product_list, name='product-list'),
    path('api/products/<int:pk>/',    views.product_detail, name='product-detail'),
    
]
