from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username",)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password1"] != cleaned_data["password2"]:
            raise forms.ValidationError("رمزها یکی نیستند")
        return cleaned_data


