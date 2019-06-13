from django import forms
from .models import Cadastro, Post, venda


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'desc', 'cover', 'preco']


class CadastroForm(forms.ModelForm):
	class Meta:
		model = Cadastro
		fields = [
		
			'nome',
			'endereco',
			'email',
			'telefone',
			'idade',
			'cpf',
		]

		labels = {
	
			'nome': 'Nome',
			'endereco': 'Endereco',
			'email': 'Email',
			'telefone': 'Telefone',
			'idade': 'Idade',
			'cpf': 'Cpf',
		}

		widgets = {
			
			'nome': forms.TextInput(attrs={'class':'form-control'}),
			'endereco': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'telefone': forms.TextInput(attrs={'class':'form-control'}),
			'idade': forms.TextInput(attrs={'class':'form-control'}),
			'cpf': forms.TextInput(attrs={'class':'form-control'}),
			
		}


class vendaForm(forms.ModelForm):
	class Meta:
		model = venda 
		fields = [
		
			'medicamento',
			'paciente',
			'quantidade',
			'total',
			'endereco',
		]

		labels = {
	
			'medicamento': 'Medicamento',
			'paciente': 'Paciente',
			'quantidade': 'Quantidade',
			'total': 'Total',
			'endereco': 'Endereco',
		}

		widgets = {
			
			'Medicamento': forms.TextInput(attrs={'class':'form-control'}),
			'Paciente': forms.TextInput(attrs={'class':'form-control'}),
			'Quantidade': forms.TextInput(attrs={'class':'form-control'}),
			'Total': forms.TextInput(attrs={'class':'form-control'}),
			'Endereco': forms.TextInput(attrs={'class':'form-control'}),
			
		}
"""class vendaForm(forms.ModelForm):
    class Meta:
		model = venda
		fields = [
		
			'medicamentos',
			'paciente',
			'Quantidade',
			'total',
			'endereco',
		]

		labels = {
	
			'medicamento': 'Medicamento',
			'paciente': 'Paciente',
			'quantidade': 'Quantidade',
			'total': 'Total',
			'endereco': 'Endereco',
			
		}

		widgets = {
			
			'medicamentos': forms.TextInput(attrs={'class':'form-control'}),
			'paciente': forms.TextInput(attrs={'class':'form-control'}),
			'quantidade': forms.TextInput(attrs={'class':'form-control'}),
			'total': forms.TextInput(attrs={'class':'form-control'}),
			'endereco': forms.TextInput(attrs={'class':'form-control'}),
			
		}"""