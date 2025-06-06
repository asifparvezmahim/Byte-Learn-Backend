# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .models import CustomUser


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "POST"])
def login_view(request):
    # GET method to return user data if authenticated
    if request.method == "GET":
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."}, status=401
            )

        # Admin Role: Return list of all users
        if request.user.role == "admin":
            users = CustomUser.objects.all()
            user_info = [
                {"id": user.id, "username": user.username, "first_name": user.first_name,
                 "last_name": user.last_name, "email": user.email}
                for user in users
            ]
            return Response(user_info, status=status.HTTP_200_OK)
        else:
            # Non-admin Role: Return only the authenticated user's details
            user_data = {
                "id": request.user.id,
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "role": request.user.role
            }
            return Response(user_data, status=status.HTTP_200_OK)

    # POST method for user login and JWT token generation
    elif request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Extracting validated data (username and password)
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user using Django's authenticate method
            user = authenticate(username=username, password=password)

            if user is not None:
                # If authentication is successful, create JWT tokens
                refresh = RefreshToken.for_user(user)

                # Return the access and refresh tokens
                return Response({
                    'message': 'Login successful',
                    'access': str(refresh.access_token),  # Access token for API requests
                    'refresh': str(refresh),              # Refresh token to obtain new access token
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # If the serializer data is invalid, return the validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

