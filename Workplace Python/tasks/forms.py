from django import forms # Importa o módulo forms do Django para criar formulários
from .models import Comment # Importa o modelo Comment do arquivo models.py

class CommentForm(forms.ModelForm): # Cria um formulário baseado no modelo Comment
    class Meta:
        model = Comment # Define o modelo a ser usado para criar o formulário
        fields = ['text'] # Campos a serem incluídos no formulário
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Escreva seu comentário aqui...',
                'rows' : 3

            }), # Define o widget para o campo de texto como uma área de texto com um espaço reservado e 3 linhas visíveis'
        }