from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from server.models import Trainee, Tag, Entry
from server.serializers import TraineeSerializer, TagSerializer, EntrySerializer

class Trainees(APIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Trainee(APIView):
    model = Trainee
    serializer_class = TraineeSerializer
    
    def get(self, request, pk, *args, **kwargs):
        trainee = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(trainee)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk, *args, **kwargs):
        trainee = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(trainee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    