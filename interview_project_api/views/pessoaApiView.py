from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from Pessoa.models.pessoa import Pessoa
from interview_project_api.serializers.pessoaSerializer import PessoaSerializer

class PessoaApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.filter(tipo = 2)
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)