from django.shortcuts import render
from forms import FileUploadForm


def main_page(request):
    return render(request, 'task2/index.html')


def upload(request):
    form = FileUploadForm()
    return render(request, 'task2/upload.html', {
        'form': form
    })
