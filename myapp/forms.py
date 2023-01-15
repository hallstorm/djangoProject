from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control mt-2 mb-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mt-2 mb-4'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control mt-2 mb-4'}))