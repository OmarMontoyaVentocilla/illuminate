from rest_framework import serializers
from .models import Facebook
from .models import Twitter
from .models import Google

class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facebook
        fields='__all__'


class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Twitter
        fields='__all__'

class GoogleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Google
        fields='__all__'
    

