from django.urls import path
from . import views
"""define padroes de URL para learning_logs"""

app_name = 'learning_logs'
urlpatterns = [
    # pagina inicial
    path('', views.index, name='index'),
    # pagina que mostra todos os topicos
    path('topics/', views.topics, name='topics'),
    # pagina de detalhes para um UNICO topico
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # pagina para adicionar um topico novo
    path('new_topic/', views.new_topic, name='new_topic'),
    # pagina para adicionar uma entrada nova
    path('new_entry/<int:topic_id>', views.new_entry ,name='new_entry'),
    # pagina para editar as entradas
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    
    
]
