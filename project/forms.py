from django.forms import ModelForm
from .models import Project_log


class LogForm(ModelForm):
    class Meta:
        model = Project_log
        fields = ['user', 'date', 'cost_center', 'prod_grp', 'project', 'hours', 'notes']



