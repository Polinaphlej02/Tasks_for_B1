from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import ExcelFiles


def main_page(request):
    return render(request, 'task2/index.html')


def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'task2/index.html')
    else:
        form = FileUploadForm()
    return render(request, 'task2/upload.html', {
        'form': form
    })
