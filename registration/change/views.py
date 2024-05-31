from django.shortcuts import render

# Create your views here.

def change(request):
    return render(request, 'change/change.html')