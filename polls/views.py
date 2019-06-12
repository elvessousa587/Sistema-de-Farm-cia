from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cadastro, Post, venda
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy 
from .forms import CadastroForm, PostForm, vendaForm 


def index(request):
   return render(request, 'index.html')
	
	
	
class CadastroCriar(CreateView):
	model = Cadastro
	form_class = CadastroForm
	template_name = 'cadastro/cadastro_form.html'
	success_url = reverse_lazy('cadastro_listar')



class CadastroListar(ListView):
	queryset = Cadastro.objects.all()
	template_name = 'cadastro/cadastro_list.html'
	paginate_by = 5 #quantidade de registros que quero que apareça na minha pagina, ai aparece 5 registros e o resto aparece em outra pagina atravez do botao proximo ou next


class CadastroUpdate(UpdateView):
	model = Cadastro
	form_class = CadastroForm
	template_name = 'cadastro/cadastro_form.html'
	success_url = reverse_lazy('cadastro_listar')


class CadastroDelete(DeleteView):
	model = Cadastro
	template_name = 'cadastro/cadastro_delete.html'
	success_url = reverse_lazy('cadastro_listar')


class CadastroShow(DetailView):
	model = Cadastro
	template_name = 'cadastro/cadastro_show.html'



def medicamento(request):
   return render(request, 'medicamento/medicamento.html')
	
	

def index2(request):
   return render(request, 'templates2/index.html')
	



class HomePageView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'medicamento/medicamento.html'


class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('indeximg')

class  deletePostView(DeleteView):
	model = Post
	template_name = 'deletePost.html'
	success_url = reverse_lazy('indeximg')

class  blogdetails(DetailView):
	model = Post
	template_name = 'blogdetails.html'

class  mycart(DetailView):
	model = Post
	template_name = 'mycart.html'


class vendaCriar(CreateView):
	model = venda
	form_class = vendaForm
	template_name = 'venda.html'
	success_url = reverse_lazy('listavenda')


class listaVenda(ListView):
	queryset = venda.objects.all()
	template_name = 'listaVenda.html'
	paginate_by = 5 #quantidade de registros que quero que apareça na minha pagina, ai aparece 5 registros e o resto aparece em outra pagina atravez do botao proximo ou next


class enviarVenda(DetailView):
	model = venda
	template_name = 'delivery.html'


class eliminarvenda(DeleteView):
	model = venda
	template_name = 'venda_delete.html'
	success_url = reverse_lazy('listavenda')




class delivery(ListView):
	queryset = venda.objects.all()
	template_name = 'delivery.html'
	paginate_by = 5 #quantidade de registros que quero que apareça na minha pagina, ai aparece 5 registros e o resto aparece em outra pagina atravez do botao proximo ou next



def contato(request):
   return render(request, 'contato.html')
	
	