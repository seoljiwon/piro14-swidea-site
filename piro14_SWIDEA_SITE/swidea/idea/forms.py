from django import forms
from .models import Ideas, DevTool


class IdeasForm(forms.ModelForm):

    class Meta:
        model = Ideas
        fields = '__all__'


class DevToolForm(forms.ModelForm):

    class Meta:
        model = DevTool
        fields = '__all__'
