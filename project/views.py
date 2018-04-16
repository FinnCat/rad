from django.shortcuts import render, redirect
from .models import Project_log
from .forms import LogForm

# Create your views here.

def list_project_log(request):
    logs = Project_log.objects.all()
    return render(request, 'project.html', {'logs':logs})

def new_project_log(request):
    form = LogForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_project_log)


    return render(request, 'log_form.html', {'form':form})
