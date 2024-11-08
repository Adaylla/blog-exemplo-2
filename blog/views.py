from django.shortcuts import render
from .models import Post, Blog, Mensagem

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first()
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
    }
    return render(request, "post.html", context)

def sobre(request):
    context = {
        "blog": Blog.objects.first()
    }
    return render(request, "about.html", context)

def contato(request):
    context = {
        "blog": Blog.objects.first()
    }
    if request.method == "POST":
        context['erro'] = {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['mensagem']:
            context['erro']['mensagem'] = True
        if context['erro']:
            return render(request, "contact.html", context)
        
        mensagem = Mensagem(nome = request.POST['nome'],
                            email = request.POST['email'],
                            telefone = request.POST['telefone'],
                            cidade = request.POST['cidade'],
                            mensagem = request.POST['mensagem'])
        mensagem.save()
        
        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html", context)
    
def mensagem(request):
    context = {
        "mensagem": Mensagem.objects.all(),
        "blog": Blog.objects.first()

    }
    return render(request, "mensagem.html", context)