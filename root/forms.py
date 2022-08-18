from django import forms
from .models import UploadFormModel


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFormModel
        fields = ['uploadedFile', 'password']  # QuestionForm에서 사용할 Question 모델의 속성