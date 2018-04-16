from django.urls import path
from .views import list_project_log, new_project_log

urlpatterns = [
    path('', list_project_log, name="project_list" ),
    path('new_log_entry/', new_project_log, name="log_new" )
]
