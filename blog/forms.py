from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from blog.models import CustomUser, Article, Comment


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'photo', 'publish', 'category')

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'publish': forms.CheckboxInput(attrs={
                'class': 'form-check'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Category'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
        widgets = {
            "description":forms.Textarea(attrs={
                "class":"form-control",
                "id":"exampleFormControlTextarea1",
                "rows":3
            })
        }