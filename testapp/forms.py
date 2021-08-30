from django import forms
from testapp.models import StudentResult

class StudentResultForm(forms.ModelForm):
    def clean_marks(self):
        if inputmarks >= 90 and inputmarks <=100:
            return 'A'
        elif inputmarks >= 80 and inputmarks <=89:
            return 'B'
        elif inputmarks >= 70 and inputmarks <=79:
            return 'C'
        elif inputmarks >= 60 and inputmarks <=69:
            return 'D'
        elif inputmarks >= 50 and inputmarks <=59:
            return 'E'
        elif inputmarks >= 40 and inputmarks <=49:
            return 'F'


    class Meta:
        Model=StudentResult
        fields='__all__'
