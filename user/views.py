from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import User
from user.permissions import AnnonPermission
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from .permissions import AnnonPermission, IsOwnerOrReadOnly


class RegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                is_active=True,
                phone_number=request.data['phone_number']
            )
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    permission_classes = (AnnonPermission, )
    serializer_class = MyTokenObtainPairSerializer


