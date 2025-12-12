from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["table", "foods"]

    def clean_foods(self):
        foods = self.cleaned_data.get("foods")
        if not foods:
            raise forms.ValidationError("You must select at least one food item.")
        return foods

