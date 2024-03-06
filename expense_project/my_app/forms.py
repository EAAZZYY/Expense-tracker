from django import forms
from .models import MyExpense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = MyExpense
        fields = ["bought","amount","category"]
        labels = {
            "bought":"Purchased",
            "amount":"How much?",
            
        }