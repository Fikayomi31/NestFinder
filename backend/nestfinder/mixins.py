import phonenumbers
from django.core.exceptions import ValidationError

class PhoneNumberValidatorMixin:
    def validate_phone_number(self):
        try:
            phone_number = phonenumbers.parse(self.phone, None)
            if not phonenumbers.is_valid_number(phone_number):
                raise ValidationError("The phone number entered is not valid.")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("The phone number entered is not valid.")

    def clean(self):
        super().clean()
        self.validate_phone_number()