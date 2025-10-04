from django.urls import path
from .views import index, contato, produto  #sao as 3 views que definimos

urlpatterns = [
    path('', index, name='index'),
    path('contato/',contato, name='contato'),
    path('produto/',produto, name='produto'),

]