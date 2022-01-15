from django.forms import ModelForm
from .models import Cohort, Student


class CohortForm(ModelForm):
    class Meta:
        model = Cohort
        fields = ['cohort_name', 'start_date', 'end_date']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']
