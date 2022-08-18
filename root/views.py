from django.shortcuts import render
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import realtp
from . import models
from Config import config
import os
from django.db.models import Q

def index(request):
    form = UploadForm()
    return render(request, 'index.html', {'form': form})

def progress(request):
    if request.method == "POST":
        uploadedFile = request.FILES["uploadedFile"]
        excelPassword = request.POST.get('password')
        UserUploadModel = models.UserUpload(
            uploadedFile=uploadedFile
        )
        UserUploadModel.save()
    UserUploadModel = models.UserUpload.objects.all()
    form = UploadForm()
    return render(request, 'index.html', {'form': form})
    #python manage.py runserver --noreload
