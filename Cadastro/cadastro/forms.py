from django import forms
from cadastro.models import Cadastro
from django.contrib.auth.hashers import make_password

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cadastro
        fields = ['name','email','password']
        
    def save(self, commit=True):
        # Obtém a senha não criptografada do formulário
        password = self.cleaned_data.get('password')
        
        # Criptografa a senha antes de salvar o objeto Cadastro
        if password:
            self.instance.password = make_password(password)
        
        return super().save(commit)