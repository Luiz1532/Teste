from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from Garagem.models.veiculo import Veiculo

class VeiculoApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, veiculo_id):
        try:
            return Veiculo.objects.get(id=veiculo_id)
        except Veiculo.DoesNotExist:
            return None

    def get(self, request, veiculo_id, *args, **kwargs):
        veiculo_instance = self.get_object(veiculo_id)
        if not veiculo_instance:
            return Response(
                {"res": "O veiculo não existe."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if veiculo_instance.tipo == 2:
            data = {
            'modelo': veiculo_instance.modelo, 
            'data_fabricacao': veiculo_instance.data_fabricacao
            }
        else:
            data = {
            'cor': veiculo_instance.cor, 
            'data_fabricacao': veiculo_instance.data_fabricacao
        }
        return Response(data, status=status.HTTP_200_OK)