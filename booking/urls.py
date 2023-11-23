from django.urls import path
from booking import views

app_name = 'booking'

urlpatterns = [
    path('', views.BookingListViews.as_view(), name='bookings'),
    path('vacations/<str:slug>/', views.VacationBookingView.as_view(), name='vacations'),
    path("verify", views.verifyCodeView.as_view(), name="verify_code")
]