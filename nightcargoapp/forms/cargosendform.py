from django import forms
from nightcargoapp.models.cargo import Cargo


class DateInput(forms.DateInput):
    input_type = 'date'


class CargoSendForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('receiver', 'receiver_gsm', 'sent_day', 'sent_month', 'sent_hour', 'sent_minute',
                  'delivery_description', 'delivery_district', 'delivery_city', 'weight')
