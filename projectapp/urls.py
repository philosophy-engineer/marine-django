from django.urls import path
from .views import ProjectCreateView, ProjectDetailView, ProjectListView


app_name = 'projectapp'
urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('list/', ProjectListView.as_view(), name='list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project'),
]
