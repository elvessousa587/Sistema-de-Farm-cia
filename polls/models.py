from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    cover = models.ImageField(upload_to='images/')
    preco = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title



class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.IntegerField()

    def __str__(self):
    	return self.nome
    	
 
class venda(models.Model):
    medicamento = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Medicamento")
    paciente = models.ForeignKey(Cadastro, on_delete=models.CASCADE, verbose_name="Paciente")
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits=4, decimal_places=2)
    endereco =  models.CharField(max_length=200)

    def __str__(self):
        return self.medicamento