from django.contrib import admin
from .models import Task # Importa o modelo Task do arquivo models.py
from .models import Comment # Importa o modelo Comment do arquivo models.py


@admin.register(Comment) # Decorador para registrar o modelo Comment no painel de administração do Django
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text' , 'author', 'task', 'created_at',] # Campos a serem exibidos na lista de comentários no painel de administração
    
@admin.register(Task) # Decorador para registrar o modelo Task no painel de administração do Django
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']# Campos a serem exibidos na lista de tarefas no painel de administração
    list_filter = [ 'created_at'] # Campos a serem filtrados na barra lateral do painel de administração
    search_fields = ('title', 'description') # Campos a serem pesquisados na barra de pesquisa do painel de administração
