from django.shortcuts import render


def main_page(request):
    return render(request, 'task2/index.html')


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['filename']
        print(uploaded_file.name)
    return render(request, 'task2/upload.html')
