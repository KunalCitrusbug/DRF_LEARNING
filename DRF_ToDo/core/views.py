from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ToDo
from .serializers import ProfileSerializer
from rest_framework.authtoken.models import Token


class Task(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        data = ToDo.objects.filter(completed=False)
        if data.exists():
            serializer = ProfileSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response("NO TASK REMAINING..")

    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = ToDo.objects.get(id=data['id'])
        serializer = ProfileSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        ToDo.objects.get(id=data['id']).delete()
        return Response("Data Deleted Successfully")


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.pk,
            'username': user.username,
            'token': token.key
        })
