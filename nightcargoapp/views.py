from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import base64, os
from .forms import SignUpForm
from .forms import NewAddressForm
from .forms import CargoSendForm
from django.shortcuts import render, redirect
from nightcargoapp.models.cargo import Cargo

# Create your views here.
from .tokens import account_activation_token

from nightcargoapp.models.address import Address


def index(request):
    return render(request, 'index.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.tck_no = form.cleaned_data.get('tck_no')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def cargo_operations(request):
    addresses = Address.objects.filter(resident_id=request.user.id)
    return render(request, 'cargo_operations.html', {'addresses': addresses})


def new_address(request):
    if request.method == 'POST':
        form = NewAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.resident = request.user
            address.header = form.cleaned_data.get('header')
            address.type = form.cleaned_data.get('type')
            address.description = form.cleaned_data.get('description')
            address.district = form.cleaned_data.get('district')
            address.city = form.cleaned_data.get('city')
            address.save()
            return redirect('cargo_operations')
    else:
        form = NewAddressForm()
    return render(request, 'new_address.html', {'form': form})


def delete_address(request, address_id):
    Address.objects.filter(address_id=address_id).delete()
    return redirect('cargo_operations')


def tracking_number_generator():
    random_string = base64.b32encode(os.urandom(8))[:10].decode('utf-8')
    while Cargo.objects.filter(tracking_number=random_string).exists():
        random_string = base64.b32encode(os.urandom(8))[:10].decode('utf-8')
    else:
        return random_string


def shipping_total_calculator(weight, district):
    if district == "0":
        return weight*6
    elif district == "1":
        return weight*12
    elif district == "2":
        return weight*30
    else:
        return 10000


def send_cargo(request, address_id):
   # Address.objects.filter(address_id=address_id).get()
    if request.method == 'POST':
        form = CargoSendForm(request.POST)
        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.sender = request.user
            cargo.sender_address = Address.objects.filter(address_id=address_id).get()
            cargo.receiver = form.cleaned_data.get('receiver')
            cargo.receiver_gsm = form.cleaned_data.get('receiver_gsm')
            cargo.sent_day = form.cleaned_data.get('sent_day')
            cargo.sent_month = form.cleaned_data.get('sent_month')
            cargo.sent_hour = form.cleaned_data.get('sent_hour')
            cargo.sent_minute = form.cleaned_data.get('sent_minute')
            cargo.delivery_description = form.cleaned_data.get('delivery_description')
            cargo.delivery_district = form.cleaned_data.get('delivery_district')
            cargo.delivery_city = form.cleaned_data.get('delivery_city')
            cargo.tracking_number = tracking_number_generator()
            cargo.weight = form.cleaned_data.get('weight')
            cargo.shipping_total = shipping_total_calculator(cargo.weight, cargo.delivery_district)
            cargo.save()
    else:
        form = CargoSendForm()
    return render(request, 'cargo_sent.html', {'form': form})
