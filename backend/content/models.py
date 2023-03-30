from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Icons(models.Model):
    title = models.CharField('Название', max_length=100)
    icon = models.ImageField('Иконка', upload_to='icons_img', default='no_icon.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Иконка'
        verbose_name_plural = 'Иконки'

class StatusTasks(models.Model):
    title = models.CharField('Название статуса', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задач'

class Tasks(models.Model):
    title = models.CharField('Название', max_length=100)
    type = models.CharField('Тип объекта', max_length=100, default='Задача')
    description = models.TextField('Описание')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Принадлежит к проекту')
    icon = models.ForeignKey(Icons, on_delete=models.CASCADE, verbose_name='Иконка', blank=True, null=True)
    status = models.ForeignKey(StatusTasks, on_delete=models.CASCADE, verbose_name='Статус')
    dedline = models.DateField('Дата сдачи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'