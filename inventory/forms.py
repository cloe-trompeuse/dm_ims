from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control', 'min': '1.00'})

    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'unit_price']