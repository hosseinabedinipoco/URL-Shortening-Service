from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Url
from .serializer import UrlSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
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
        url = get_object_or_404(Url, short_code=code)
        serializer = UrlSerializer(url)
        return Response(url.data, status=status.HTTP_200_OK)


    def put(self, request, code):
        url = get_object_or_404(Url, short_code=code)
        serializer = UrlSerializer(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, code):
        url = get_object_or_404(Url, short_code=code)
        url.delete()
        return Response({'message':"deleted"}, status=status.HTTP_204_NO_CONTENT)


