from django.contrib import admin
from django.urls import path, include, re_path
from content.views import ProjectListAPIView, TasksListAPIView, TasksDestroyAPIView, TasksCreateAPIView, UserInfoView, TasksUpdateAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # API
    path('content/projects/', ProjectListAPIView.as_view()),
    path('content/tasks/', TasksListAPIView.as_view()),
    path('content/tasks/add/', TasksCreateAPIView.as_view()),
    path('content/tasks/<int:pk>/delete/', TasksDestroyAPIView.as_view()),
    path('userinfo/', UserInfoView.as_view()),
    path('content/tasks/<int:pk>/update/', TasksUpdateAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)