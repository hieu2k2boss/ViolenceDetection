# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestAPI.models import ModelAPI as YourModel
from RestAPI.models import ResultAPI
from RestAPI.serializers import MyResultSerializer
from RestAPI.serializers import MyModelSerializer as YourModelSerializer

@api_view(['GET', 'POST', 'PUT'])
def your_model_view(request):
    if request.method == 'GET':
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        instance = YourModel.objects.get(id=request.data.get('id'))
        serializer = YourModelSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'POST', 'PUT'])
def Result(request):
    if request.method == 'GET':
        queryset = ResultAPI.objects.all()
        serializer = MyResultSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MyResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        instance = ResultAPI.objects.get(id=request.data.get('id'))
        serializer = MyResultSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    