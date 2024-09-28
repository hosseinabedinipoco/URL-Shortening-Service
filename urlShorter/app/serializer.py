from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
        
    def create(self, validated_data):
        random_code = 1
        url = Url.objects.create(
            url = validated_data['url'],
            short_code = random_code
        )    
        return url