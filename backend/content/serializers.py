from rest_framework import serializers
from .models import Projects, Tasks, Icons, StatusTasks
import locale

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

# Сериализатор для отображения ссылок на иконки
class IconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icons
        fields = ('icon',)

# Сериализатор для отображения названия статуса
class StatusTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTasks
        fields = ('title',)

class TasksSerializer(serializers.ModelSerializer):
    
    # Используем отдельный сериалайзер для вывода ссылок на иконки, а не id
    icon = IconsSerializer()
    # Используем отдельный сериалайзер для вывода названия статуса а не его id
    status = StatusTasksSerializer()
    
    # Изменяем формат даты на читабельный
    create = serializers.DateTimeField(format='%d %B %Y в %H:%M')
    dedline = serializers.DateField(format='%d %B %Y')

    class Meta:
        model = Tasks
        fields = '__all__'

    # Функция для вывода месяца даты на русском языке
    def to_representation(self, instance):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return super().to_representation(instance)

class AddTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class DestroyTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'