from rest_framework import viewsets
from .models import Facebook
from .models import Twitter
from .models import Google
from .models import Instagram
from .serializers import FacebookSerializer
from .serializers import TwitterSerializer
from .serializers import GoogleSerializer
from .serializers import InstagramSerializer

class FacebookViewSet(viewsets.ModelViewSet):
    queryset = Facebook.objects.filter(estado="1")
    serializer_class = FacebookSerializer


class TwitterViewSet(viewsets.ModelViewSet):
    queryset = Twitter.objects.filter(estado="1")
    serializer_class = TwitterSerializer

class GoogleViewSet(viewsets.ModelViewSet):
    queryset = Google.objects.filter(estado="1")
    serializer_class = GoogleSerializer

class InstagtramViewSet(viewsets.ModelViewSet):
    queryset = Instagram.objects.filter(estado="1")
    serializer_class = InstagramSerializer