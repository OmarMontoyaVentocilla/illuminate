from rest_framework import viewsets
from .models import Facebook
from .models import Twitter
from .models import Google
from .serializers import FacebookSerializer
from .serializers import TwitterSerializer
from .serializers import GoogleSerializer

class FacebookViewSet(viewsets.ModelViewSet):
    queryset = Facebook.objects.filter(estado="1")
    serializer_class = FacebookSerializer


class TwitterViewSet(viewsets.ModelViewSet):
    queryset = Twitter.objects.filter(estado="1")
    serializer_class = TwitterSerializer

class GoogleViewSet(viewsets.ModelViewSet):
    queryset = Google.objects.filter(estado="1")
    serializer_class = GoogleSerializer
