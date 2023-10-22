
from django import forms as dforms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(dforms.Form):
    email = dforms.CharField(widget=dforms.TextInput(attrs={'placeholder': 'Email'}))
    password = dforms.CharField(widget=dforms.PasswordInput())
    address_1 = dforms.CharField(
        label='Address',
        widget=dforms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = dforms.CharField(
        widget=dforms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = dforms.CharField()
    state = dforms.ChoiceField(choices=STATES)
    zip_code = dforms.CharField(label='Zip')
    check_me_out = dforms.BooleanField(required=False)

    class Meta:
      name = 'forma'
