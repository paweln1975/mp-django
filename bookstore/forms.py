from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your name"
        }


class ProfileForm(forms.Form):
    user_image = forms.FileField(allow_empty_file=False)