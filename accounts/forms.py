from django import forms
from .models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class CustomTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super().__init__(*args, **kwargs)

class CustomPhoneNumberWidget(PhoneNumberPrefixWidget):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control prefix-dropdown'})
        super().__init__(*args, **kwargs)

class UserForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=CustomPhoneNumberWidget(attrs={'style': 'width: 50%; margin-right: 5px;'}),
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'confirm_password', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field.widget, (forms.TextInput, forms.EmailInput)):
                field.widget = CustomTextInput()