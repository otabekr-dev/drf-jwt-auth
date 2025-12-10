from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsAdmin, IsManager, IsUser


class UserProfielView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUser]

    def get(self, request: Request) -> Response:
        return Response({'message': 'hello world'})

class UserProfieUpdatelView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def put(self, request: Request) -> Response:
        # udpate profile
        return Response({'message': 'hello world'})
