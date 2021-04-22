from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['tittle', 'anons','full_text','data']
        widgets = {
            "tittle": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название статьи'
                } ),
            "anons": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Мини текст'
                }),
            "data": DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Дата'
                }),
            "full_text": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Текст статьи'
                })
            }

