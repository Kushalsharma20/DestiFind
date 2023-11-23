from curses import start_color
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from eruna import models
from booking.models import VacationBooking

from booking.mixin import SecuredAccessMixin

from django.template import context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import random

from django.core.cache import cache
from django.contrib.auth import logout

def sendCode(user):
    generated_code = "".join([f"{random.randint(1, 10)}" for _ in range(5)])
    context = {
        "user": user,
        'msg': f"Auth Code: {generated_code}",
    }
    email_subject = "Secure Authentication"
    email_body = render_to_string('email/secure_email_message.txt', context)
    # print(email_body)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [user.email, ],
    )
    return email.send(fail_silently=False), generated_code


class verifyCodeView(View):
    template = './booking/verify_code.html'

    def get(self, request):
        _, generated_code = sendCode(request.user)
        content_data = {
            "code": generated_code
        }
        cache.set("verify_code", generated_code)
        return render(request, self.template, context=content_data)
    
    def post(self, request):
        if not cache.get("verify_code"):
            logout(request)
            return redirect(reverse('auth_app:login'))
        
        # compare codes
        if request.POST.get("verify_code") == cache.get("verify_code"):
            return redirect(reverse('booking:bookings'))


class VacationBookingView(View):
    template = './booking/booking-travel.html'
    queryset = models.Destination

    def post(self, request, slug):
        if request.user.is_authenticated:
            destination = self.queryset.objects.filter(slug=slug).first()
        
            booking = VacationBooking(
                destination = destination,
                user_id = request.user.id,
                total_price = destination.price,
                start_date =  request.POST.get('start-date'),
                end_date = request.POST.get('end-date')
            )
            booking.save()
            return redirect(reverse('booking:bookings'))
        return redirect(reverse('auth_app:login'))


    def get(self, request):
        return redirect(reverse('eruna:destinations'))

class BookingListViews(View):
    template = './booking/bookings.html'

    def get(self, request):

        if request.user.is_authenticated:
            content_data = {
                'vacations' : VacationBooking.objects.filter(user_id=request.user.id)
            }

            return render(request, self.template, context=content_data)
        return redirect(reverse('auth_app:login'))