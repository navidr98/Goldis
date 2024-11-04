from django import forms

class SaleForm(forms.Form):
    rial_amount = forms.DecimalField(
        max_digits=20,
        decimal_places=2,
        required=False,
        label='مبلغ',
        widget=forms.TextInput(attrs={
            'placeholder': '0',
            'class': 'amount-input',
            'id': 'id_rial_amount'
        })
    )
    gold_amount = forms.DecimalField(
        max_digits=20,
        decimal_places=2,
        required=False,
        label='گرم طلا',
        widget=forms.TextInput(attrs={
            'placeholder': '0',
            'class': 'amount-input',
            'id': 'id_gold_amount'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        rial_amount = cleaned_data.get('rial_amount')
        gold_amount = cleaned_data.get('gold_amount')

        if rial_amount and gold_amount:
            raise forms.ValidationError("لطفاً فقط یکی از مبالغ ریال یا طلا را وارد کنید.")
        if not rial_amount and not gold_amount:
            raise forms.ValidationError("لطفاً یکی از مبالغ را وارد کنید.")


class Walletform(forms.Form):
    rial_amount = forms.DecimalField(
        max_digits=20,
        decimal_places=2,
        required=True,
        label='مبلغ',
        widget=forms.TextInput(attrs={
            'placeholder': '0',
            'class': 'amount-input',
        })
    )
