from django import forms
from .models import File
from django.forms import ClearableFileInput

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
    

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if file.size > 4 * 1024 * 1024:
                raise forms.ValidationError("File size cannot exceed 4MB.")
            return file
        else:
            raise forms.ValidationError("File upload failed.")