from django.contrib import admin
from django.urls import include, path
from interview_project_api import urls as interview_project_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('interview_project_api/', include(interview_project_api_urls)),
]