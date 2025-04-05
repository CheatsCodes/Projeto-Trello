from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re

User = get_user_model()  # Definir ANTES de usar o modelo

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comentário de {self.author} em {self.task.title}"

    # Método para processar menções ao salvar o comentário
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Salva primeiro o comentário
        self.process_mentions()

    def process_mentions(self):
        mentioned_usernames = re.findall(r'@(\w+)', self.text)
        for username in mentioned_usernames:
            try:
                user = User.objects.get(username=username)
                # Aqui você pode adicionar lógica de notificação
                print(f"Usuário mencionado: {user.username}")  # Exemplo
            except User.DoesNotExist:
                pass  # Ou tratar o erro como desejar