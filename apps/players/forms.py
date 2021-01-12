# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Apps.players
from apps.players import models

class PlayerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.Player
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]