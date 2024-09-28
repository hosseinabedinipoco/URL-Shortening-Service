from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Url
from .serializer import UrlSerializer
from rest_framework import status
# Create your views here.

class create_url(APIView):
    def post(self, request):
        url = UrlSerializer(data=request.data)
        if url.is_valid():
            url.save()
            return Response(url.data, status=status.HTTP_201_CREATED)
        return Response(url.errors, status=status.HTTP_400_BAD_REQUEST)


class opreate_url(APIView):
    def get(self, request, code):
        pass

    def put(self, request, code):
        pass

    def delete(self, request, code):
        pass


