from django import forms
from .models import *


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFiles
        fields = ('excel_file',)
