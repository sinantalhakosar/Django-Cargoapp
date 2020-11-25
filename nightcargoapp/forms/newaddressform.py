from django import forms
from nightcargoapp.models.address import Address


class NewAddressForm(forms.ModelForm):
    header = forms.CharField(max_length=20, help_text='Adres Başlığı Giriniz (Örn. Evim)')
    description = forms.CharField(max_length=100, help_text='Adres Bilgileri (Cadde/Sokak vs.)')
    district = forms.CharField(max_length=50, help_text='İlçe Giriniz')
    city = forms.CharField(max_length=50, help_text='İl Giriniz')

    class Meta:
        model = Address
        fields = ('header', 'description', 'district', 'city')