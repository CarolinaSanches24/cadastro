from django.contrib import admin
from cadastro.models import Cadastro
# Register your models here.
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    
    # show fields
    list_display = ['name','email','data'] 
    search_fields = ['name','email']
    list_filter = ['data']
    
    
