from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserLoginSerializer




class UserLoginView(APIView):

    def post(self,request):

        data = request.data
        serializer = UserLoginSerializer(data = data)

        if serializer.is_valid():

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username, password = password)

            if user:
                refresh = RefreshToken.for_user(user)

                return Response({
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            
            return Response({"Error":"Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            refresh_token = request.data.get('refresh_token')

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message":"User logged out successfully."},status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response({"error": str(e)},status= status.HTTP_400_BAD_REQUEST)