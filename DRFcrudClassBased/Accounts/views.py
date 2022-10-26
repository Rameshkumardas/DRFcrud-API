from functools import partial
from Accounts.models import UserRegistation
from Accounts.serializers import UserRegistationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

class UserRegastationClassBasedAPI(APIView):
    def get(self, request, pk=None, format=None):
        pk = pk
        if pk is not None:
            users = UserRegistation.objects.get(pk=pk)
            serialize = UserRegistationSerializer(users)
            return Response(serialize.data)
        users = UserRegistation.objects.all()
        serialize = UserRegistationSerializer(users, many=True)
        return Response(serialize.data)

    def post(self, request, format=None):
        serializer = UserRegistationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!'}, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            users = UserRegistation.objects.get(pk=pk)
            serializer = UserRegistationSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated!'}, status=status.HTTP_201_CREATED)       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserRegistation.DoesNotExist:
            return Response({'msg':'USER DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)        


    def patch(self, request, pk, format=None):
        try:
            users = UserRegistation.objects.get(pk=pk)
            serializer = UserRegistationSerializer(users, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated!'}, status=status.HTTP_201_CREATED)       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserRegistation.DoesNotExist:
            return Response({'msg':'USER DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)        


    def delete(self, request, pk, format=None):
        try:
            user = UserRegistation.get_object(pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserRegistation.DoesNotExist:
            return Response({'msg':'USER DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)        



