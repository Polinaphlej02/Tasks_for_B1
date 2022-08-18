from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def main_page(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['filename']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'task2/index.html')


def update_details(request):
    message = ''
    form = UpdateDetailsForm(request.POST, request.FILES)
    if form.is_valid():
        from task2.models import ClassTable, BankAccount2, BankAccount4, OpeningBalance, Turnover
        # import your django model here like from django.appname.models import model_name
        excel_file = request.FILES['excel_file']
        
