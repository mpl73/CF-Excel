from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gastos', views.gastos, name='gastos'),
    path('cartoes', views.cartoes, name='cartoes'),
    path('novo_cartao', views.novo_cartao, name='novo_cartao'),
    path('cartoes/<int:id>', views.editar_cartao, name='editar_cartao'),
    path('deletar_cartao/<int:id>', views.deletar_cartao, name='deletar_cartao'),
]