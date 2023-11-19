from accounts import admin
from . import views
from django.urls import path , include

from django.utils.translation import gettext as _

admin.site_header = _('project management')

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_Create'),
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='Project_update'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('task/create', views.TaskCreateView.as_view(), name='Task_create'),
    path('task/edit/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),

]
