from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'register/register.html')

def change(request):
    return render(request, 'change/change.html')

