from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'gazua/index.html')

def Test(request):
    return render(request, 'gazua/test.html')
