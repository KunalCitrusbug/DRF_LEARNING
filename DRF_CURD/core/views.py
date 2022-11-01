from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


# ====================================================================================
#                           FUNCTION BASED VIEWS
# ====================================================================================
@api_view(["GET", "POST", "PATCH", "DELETE"])
def profile(request):
    if request.method == "GET":
        profile_data = Profile.objects.all()
        if profile_data.exists():
            serializer = ProfileSerializer(profile_data, many=True)
            return Response(serializer.data)
        else:
            return Response("NO DATA AT MOMENT")

    if request.method == "POST":
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)

    if request.method == "PATCH":
        data = request.data
        obj = Profile.objects.get(id=data['id'])
        serializer = ProfileSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)

    else:
        data = request.data
        obj = Profile.objects.get(id=data['id']).delete()
        return Response("Data Deleted Successfully")


# ====================================================================================
#                           CLASS BASED VIEWS
# ====================================================================================

class Class_Profile(APIView):
    def get(self, request):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            serializer = ProfileSerializer(profile_data, many=True)
            return Response(serializer.data)
        else:
            return Response("NO DATA AT MOMENT")

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
        obj = Profile.objects.get(id=data['id'])
        serializer = ProfileSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Profile.objects.get(id=data['id']).delete()
        return Response("Data Deleted Successfully")


# ====================================================================================
#                               GENERIC VIEWS
# ====================================================================================

class Generic_Profile_GET(generics.ListAPIView):  # ListApiView is used for Get method or to show all data in DRF
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class Generic_Profile_POST(generics.CreateAPIView):  # CreateApiView is used for Get method or to show all data in DRF
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class Generic_Profile_DELETE(
    generics.DestroyAPIView):  # DestroyApiView is used for Get method or to show all data in DRF
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'


class Generic_Profile_UPDATE(generics.UpdateAPIView):  # UpdateAPIView is used for Get method or to show all data in DRF
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
