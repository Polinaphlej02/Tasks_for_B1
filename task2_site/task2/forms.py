from django import forms
from .models import *


class FileUploadForm(forms.Form):
    class Meta:
        model = ExcelFiles
        fields = ('file_name', 'excel_file')