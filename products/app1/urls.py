from django.urls import path
from app1 import views

urlpatterns = [

    path('api_overview/', views.api_overview, name='overview'),
    path('product-list/',views.showall,name='product-list'),
    path('product-create/',views.createproduct,name='product-create'),
    path('product-details/<int:pk>/',views.detailview,name='product-details')

]
