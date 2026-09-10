from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Booking


def home(request):
    return render(request, 'home.html')


@login_required
def add_booking(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        event_date = request.POST['event_date']
        hall_name = request.POST['hall_name']
        phone = request.POST['phone']

        Booking.objects.create(
            customer_name=customer_name,
            event_date=event_date,
            hall_name=hall_name,
            phone=phone
        )

        return redirect('booking_list')

    return render(request, 'add_booking.html')


@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})


@login_required
def edit_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        booking.customer_name = request.POST['customer_name']
        booking.event_date = request.POST['event_date']
        booking.hall_name = request.POST['hall_name']
        booking.phone = request.POST['phone']

        booking.save()

        return redirect('booking_list')

    return render(request, 'edit_booking.html', {'booking': booking})


@login_required
def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()

    return redirect('booking_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('booking_list')
        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')