from django.shortcuts import render
from django.http import HttpResponse
from cadastro.forms import CadastroForm
# Create your views here.
def inicio(request):
  
    return render(request,'inicio.html')

def cadastro(request):
    sucess = False
    if(request.method=='GET'):
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            sucess = True
            form.save()
    context = {
    'form':form,
    'sucess':sucess
    }
    return render(request,'cadastro.html', context);