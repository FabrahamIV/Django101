from django import forms

class PostForm(forms.Form):
    title= forms.CharField(label='Post Text', widget=forms.TextInput(attrs={'placeholder': 'Enter your post here'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Enter a description', 'rows': 4}))
    image = forms.FileField(required=False, label='Upload Image')