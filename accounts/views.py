from rest_framework import generics
from .serializers import UserSerializer
from .models import CustomUser

# Create your views here.
class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer