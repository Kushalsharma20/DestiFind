from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from eruna.views import DestinationListView

urlpatterns = [
    path('', include('eruna.urls', namespace='eruna')),
    path('booking/', include('booking.urls', namespace='booking')),
    path('auth/', include('auth_app.urls', namespace='auth_app')),
    path('accounts/profile/', DestinationListView.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Added manually

admin.site.site_header = "DestiFind"
admin.site.index_title = "Welcome to DestiFind"
admin.site.site_title = "DestiFind"