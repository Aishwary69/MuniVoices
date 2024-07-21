from django import forms

from .models import Samasya
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewSamasyaForm(forms.ModelForm):
    class Meta:
        model = Samasya
        fields = ('category', 'name', 'description', 'time', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'time': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditSamasyaForm(forms.ModelForm):
    class Meta:
        model = Samasya
        fields = ('name', 'description', 'time', 'image', 'is_solved')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'time': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }