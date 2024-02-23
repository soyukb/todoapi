from django.shortcuts import render
from myapp.models import ToDos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from myapp.serializers import ToDosSerializer

# Create your views here.
class ToDoAPI(APIView):

    def get(self, request, pk):
        try:
            todo = ToDos.objects.get(pk=pk)
        except todo.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ToDosSerializer(
            todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = ToDos.objects.get(pk=pk)
        serializer = ToDosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = ToDos.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ToDosAPI(APIView):
    def get(self, request):
        todos = ToDos.objects.all()
        serializer = ToDosSerializer(todos, many=True)
        return Response(serializer.data)
