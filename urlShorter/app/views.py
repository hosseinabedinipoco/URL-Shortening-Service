from django.shortcuts import render
from rest_framework.decorators import APIView
# Create your views here.

class create_url(APIView):
    def post(self, request):
        pass

class opreate_url(APIView):
    def get(self, request, code):
        pass

    def put(self, request, code):
        pass

    def delete(self, request, code):
        pass


