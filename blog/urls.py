from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('mensagem/', views.mensagem, name='mensagem'),
    path('mensagem/<int:mensagem_id>/editar', views.editar_mensagem, name='editar_mensagem'),
    path('mensagem/<int:mensagem_id>/deletar', views.deletar_mensagem, name='deletar_mensagem'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
