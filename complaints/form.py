from .models import Complaint
from django import forms  
  
class Complaintform(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['title','description','category','attachment']