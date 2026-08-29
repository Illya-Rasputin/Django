from django import forms

from games_app.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'name',
            'developer',
            'description',
            'release_date',
            'rating',
            'image_url',
        ]
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': '0.1'}),
        }
