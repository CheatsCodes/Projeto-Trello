from django.urls import path
from .views import task_list, task_detail  # Importe ambas as views

app_name = 'tasks'  # Namespace opcional para organização

urlpatterns = [
    # URL para lista de tarefas (página inicial)
    path('', task_list, name='task_list'),
    
    # URL para detalhes da tarefa (note o <int:task_id> corrigido)
    path('<int:task_id>/', task_detail, name='task_detail'),
]