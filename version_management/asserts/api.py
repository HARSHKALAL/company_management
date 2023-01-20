from rest_framework.views import APIView,Response
from .serializers import CompanySerializer

class CompanyApi(APIView):
    def get(self, request):
        return Response({"message": "called Account Api GET"})

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            company=serializer.save()
        return Response({"message":"called Registraion Api POST"})

