from django import forms
from .models import Book


class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['titre', 'publisher', 'year', 'isbn', 'backCover', 'cover']
        widgets = {
            'year' : forms.SelectDateWidget(years=range(1950,2024)),
        }
