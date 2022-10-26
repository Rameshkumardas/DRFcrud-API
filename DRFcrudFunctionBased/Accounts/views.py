from functools import partial
from yaml import serialize
from Accounts.models import UserRegistation
from Accounts.serializers import UserRegistationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def UserRegastationAPI(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            users = UserRegistation.objects.get(pk=id)
            serialize = UserRegistationSerializer(users)
            return Response(serialize.data)

        users = UserRegistation.objects.all()
        serialize = UserRegistationSerializer(users, many=True)
        return Response(serialize.data)

    elif request.method == 'POST':
        serializer = UserRegistationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!'}, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = request.data.get('id')
        users = UserRegistation.objects.get(pk=id)
        serializer = UserRegistationSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated!'}, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        id = request.data.get('id')
        users = UserRegistation.objects.get(pk=id)
        serializer = UserRegistationSerializer(users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated!'}, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.data.get('id')
        users = UserRegistation.objects.get(pk=id)
        users.delete()
        return Response({'msg':'Data Deleted!'})        
