from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .forms import FileForm
from .models import File

def home(request):
    return render(request, 'uploads/home.html')


class CustomLoginView(LoginView):
    template_name = 'uploads/login.html'

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileslist')
    else:
        form = FileForm()
    return render(request, 'uploads/files.html')

def file_list(request):
    
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileslist')
    else:
        form = FileForm()

    documents = File.objects.all()
    context={
    'documents': documents,
    'form':form
    }
    return render(request, 'uploads/files.html',context)