from rest_framework.response import Response
from rest_framework.views import APIView
from decouple import config

class SoapView(APIView):

    def get(self, request):
        objs = {
            "book_soap":f"http://{config('BACKEND_DOMAIN', cast=str)}/book/soap/",
        }
        return Response(objs, status=200)