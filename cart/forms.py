from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Quantidade')
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput)
        
    quantity.widget.attrs.update({'class':'custom-select'})
    quantity.widget.attrs.update({'onchange':'submit()'})