from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """mostra todos os topicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """seleciona um unico topico"""
    topic = Topic.objects.get(id=topic_id)
    # verifica se o topico pertence ao usuario atual 
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context) 

@login_required
def new_topic(request):
    """adiciona um topico novo"""
    if not request.method == 'POST':
        # nenhum dado envia; cria form em branco
        form = TopicForm()
    else:
        # dados POST enviado; processa os dados
        form = TopicForm(data=request.POST)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        return redirect('learning_logs:topics')
    
    # exibe um formulario em branco ou invalido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """adicionar uma entrada nova"""
    topic = Topic.objects.get(id=topic_id)

    if not request.method == 'POST':
        # nenhum dado envia; cria form em branco
        form = EntryForm()
    else:
        # dados POST enviado; processa os dados
        form = EntryForm(data=request.POST)
    if form.is_valid():
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.owner = request.user
        new_entry.save()
        return redirect('learning_logs:topic', topic_id=topic_id)
    # exibe um formulario em branco ou invalido
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if not request.method == 'POST':
        # requisiçao inicial; pre-preenche o formulario com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # dados POST enviados; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request):
        owner = request.user
        return owner
    