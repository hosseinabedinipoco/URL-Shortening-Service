from rest_framework import serializers
from .models import Url
import random
import string
from django.db import IntegrityError


class UrlSerializer(serializers.ModelSerializer):
    short_code = serializers.CharField(required=False)
    class Meta:
        model = Url
        fields = '__all__'
        

    def generate_short_code(self):
        # Generate a code with 3 letters and 3 digits
        letters = ''.join(random.choices(string.ascii_letters, k=3))
        digits = ''.join(random.choices(string.digits, k=3))
        return letters + digits
        
    def create(self, validated_data):
        while True:
            random_code = self.generate_short_code()
            try:
                url = Url.objects.create(
                    url=validated_data['url'],
                    short_code=random_code
                )
                break
            except IntegrityError:
                continue
        
        return url