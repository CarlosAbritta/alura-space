from django.urls import path
from apps.galeria.views import index, imagem,buscar,nova_imagem,editar_imagem,deletar_imagem,filtro  # Importa as funções de view 'index' e 'imagem' do módulo 'galeria.views'

# Define a lista de padrões de URL
urlpatterns = [
    # Mapeia a URL raiz ('') para a view 'index'
    # Nome da URL: 'index'
    path('', index, name='index'),

    # Mapeia a URL 'imagem/<int:foto_id>' para a view 'imagem'
    # <int:foto_id> é um parâmetro que captura um número inteiro da URL e o passa como argumento 'foto_id' para a view
    # Nome da URL: 'imagem'
    path('imagem/<int:foto_id>', imagem, name='imagem'),

    path('buscar',buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]
