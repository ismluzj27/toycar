from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    payment_method = forms.ChoiceField(choices=[
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Bank Transfer', 'Bank Transfer'),
    ])
    card_number = forms.CharField(max_length=19)
    exp_date = forms.CharField(max_length=5)
    cvv = forms.CharField(max_length=3)