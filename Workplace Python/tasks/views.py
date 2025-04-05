from django.shortcuts import render, get_object_or_404, redirect  # Importações corrigidas
from .models import Task
from .forms import CommentForm

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.save()
            return redirect('task-detail', task_id=task.id)  # Nome da URL corrigido
    else:
        form = CommentForm()

    # Renderização movida para fora do bloco if/else
    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'comments': comments,
        'form': form
    })

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})