"""
Profiles App - Forms
----------------
Forms for Profiles App.
"""
from django.forms import ModelForm
from django import forms
from datetime import date
from phonenumber_field.formfields import PhoneNumberField
from .models import UserProfile


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
         Add placeholders and classes, set delivery fields to readonly,
        remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_county"].widget.attrs["readonly"] = True
        self.fields["default_town_or_city"].widget.attrs["readonly"] = True

        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False


class DateOrdersForm(forms.Form):
    """
    Form for filtering the orders in admin manage orders page
    """

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "px-2", "value": date.today}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].required = False
        self.fields["date"].label = "Filter By Date:"
