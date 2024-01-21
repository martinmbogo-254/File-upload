from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .forms import FileForm
from .models import File,Client
from django.db.models import Q

def home(request):
    # clients = Client.objects.all()
    q= request.GET.get('q') if request.GET.get('q') != None else ""
    clients = Client.objects.filter(
        Q(name__icontains=q)|
        Q(mobile__icontains=q)|
        Q(veh_reg__icontains=q)
        # Q(category__category_name__icontains=q)
   
        
    )
    total_clients = clients.count()
    context={
        'clients': clients,
        'total_clients': total_clients
    }
    return render(request, 'uploads/home.html',context)

def ClientDetail(request, pk):
    client = Client.objects.get(id=pk)
    files = File.objects.filter(client=client)
    total_files = files.count()
    context = {
        'client': client,
        'files': files,
        'total_files':total_files
     
    }
    return render(request, 'uploads/details.html', context)

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