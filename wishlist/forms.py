from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Wishlist, WishlistItem


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class WishlistTitleForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ('title',)


class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ('text', 'url')
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'What do you wish for?'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://... (optional)'}),
        }
