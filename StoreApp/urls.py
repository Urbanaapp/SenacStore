from django.urls import path
from StoreApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('produtos/',views.produto_lista, name='produto_lista'),
    path('produto/',views.produto_detalhe, name='produto_detalhe'),

]