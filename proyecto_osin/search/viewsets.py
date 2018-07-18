from rest_framework import viewsets
from .models import Facebook
from .models import Twitter
from .serializers import FacebookSerializer
from .serializers import TwitterSerializer


class FacebookViewSet(viewsets.ModelViewSet):
    queryset = Facebook.objects.filter(estado="1")
    serializer_class = FacebookSerializer


class TwitterViewSet(viewsets.ModelViewSet):
    queryset = Twitter.objects.filter(estado="1")
    serializer_class = TwitterSerializer