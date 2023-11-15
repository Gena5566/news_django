from django import forms
from .models import AllNews


class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'placeholder': 'Введите заголовок'}))
    link = forms.URLField(label='Ссылка', required=False)
    image_url = forms.URLField(label='Ссылка на изображение', required=False)
    image = forms.ImageField(label='Изображение', required=False)
    content = forms.CharField(label='Содержание', widget=forms.Textarea(attrs={'placeholder': 'Введите содержание'}))

    class Meta:
        model = AllNews
        exclude = ('user',)