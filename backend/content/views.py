from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Projects, Tasks
from .serializers import ProjectSerializer, TasksSerializer, AddTasksSerializer, DestroyTasksSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Получение информации о пользователе
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = {
            'id': user.id,
            'username': user.username,
        }
        return Response(data)

# Получение списка проектов
class ProjectListAPIView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Projects.objects.filter(author=user)
    
# Получение списка задач
class TasksListAPIView(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(author=user)

# Создание задач
class TasksCreateAPIView(CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = AddTasksSerializer
    # permission_classes = [IsAuthenticated]

# Удаление задач
class TasksDestroyAPIView(DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = DestroyTasksSerializer

# Изменение задач
class TasksUpdateAPIView(UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = AddTasksSerializer


