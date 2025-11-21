from django.http import HttpResponse
from django.shortcuts import render


def home_views(request):
    #return HttpResponse ('Bonjour le monde')
    return render(request, 'index.html')

def contact_views(request):
    #return HttpResponse ('contactez-nous')
    return render(request, 'contact.html')

def articles_views(request):
    #return HttpResponse ('contactez-nous')
    return render(request, 'articles.html')