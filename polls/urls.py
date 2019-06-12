from django.urls import path
from . import views

urlpatterns = [
	
    path('index/', views.index, name='index'),
    
	 path('novoCadastro/', views.CadastroCriar.as_view(), name='cadastro_criar'),
 	 path('listarCadastro/', views.CadastroListar.as_view(), name='cadastro_listar'),
 	 path('eliminarCadastro/(?P<pk>\d+)/', views.CadastroDelete.as_view(), name='cadastro_eliminar'),
 	 path('editarCadastro/(?P<pk>\d+)/', views.CadastroUpdate.as_view(), name='cadastro_editar'),
 	 path('mostrarCadastro/(?P<pk>\d+)/', views.CadastroShow.as_view(), name='cadastro_mostrar'),
 	 path('medicamento/', views.medicamento, name='medicamento'),
	 path('index2/', views.index2, name='index2'),
 	 

 	 path('imagem/', views.HomePageView.as_view(), name='indeximg'),
 	 path('post/', views.CreatePostView.as_view(), name='add_post'),
 	 path('blogdetails/(?P<pk>\d+)/', views.blogdetails.as_view(), name='blogdetails'),
 	 path('mycart/(?P<pk>\d+)/', views.mycart.as_view(), name='mycart'),
 	 path('deletepost/(?P<pk>\d+)/', views.deletePostView.as_view(), name='deletepost'),

 	 path('delivery/', views.delivery.as_view(), name='delivery'),
 	 path('venda/', views.vendaCriar.as_view(), name='venda'),
 	 path('listavenda/', views.listaVenda.as_view(), name='listavenda'),
 	 path('enviarVenda/(?P<pk>\d+)/', views.enviarVenda.as_view(), name='enviarVenda'),
 	 path('eliminarvenda/(?P<pk>\d+)/', views.eliminarvenda.as_view(), name='eliminarvenda'),
 	 path('contato/', views.contato, name='contato'),

]