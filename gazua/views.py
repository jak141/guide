from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'gazua/index.html')

def Test(request):
    return render(request, 'gazua/test.html')

def Login(request):
    return render(request, 'gazua/login.html', {})

def Register(request):
    return render(request, 'gazua/register.html', {})

def Guide_Write(request):
    return render(request, 'gazua/guide_write.html',{})
    
