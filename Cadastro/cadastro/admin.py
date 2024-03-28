from django.contrib import admin
from cadastro.models import Cadastro
# Register your models here.
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    pass
