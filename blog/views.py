from django.shortcuts import render
from . import models
# from django.http import HttpResponse


def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article': article})

# Create your views here.
