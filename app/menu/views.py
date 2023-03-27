from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def page_view(request, slug):
    return render(request, 'index.html')
