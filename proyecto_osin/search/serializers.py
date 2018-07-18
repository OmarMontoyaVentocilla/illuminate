from rest_framework import serializers
from .models import Facebook
from .models import Twitter

class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facebook
        fields='__all__'


class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Twitter
        fields='__all__'
    

