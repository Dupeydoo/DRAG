from django.shortcuts import render

def index(request):
    return render(request, 'DRAG/index.html')

def diversify(request):
    return render(request, 'DRAG/startdiversify.html')