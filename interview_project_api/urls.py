from django.urls import path
from interview_project_api.views.garagemApiView import GaragemApiView
from interview_project_api.views.pessoaApiView import PessoaApiView
from interview_project_api.views.veiculoApiView import VeiculoApiView

urlpatterns = [
    path('pessoa_api', PessoaApiView.as_view()),
    path('garagem_api', GaragemApiView.as_view()),
    path('veiculo_api/<int:veiculo_id>/', VeiculoApiView.as_view()),
]