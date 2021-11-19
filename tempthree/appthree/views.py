from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'title':'hello universe', 'number':1000}
    return render(request, 'appthree/index.html', context_dict)

def other(request):
    return render(request, 'appthree/other.html')

def relative(request):
    return render(request, 'appthree/relative_url.html')