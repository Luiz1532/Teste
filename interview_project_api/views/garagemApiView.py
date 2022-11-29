from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from Garagem.models.garagem import Garagem
from interview_project_api.serializers.garagemSerializer import GaragemSerializer

class GaragemApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        garagens = Garagem.objects.filter(ativa = True)
        serializer = GaragemSerializer(garagens, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)