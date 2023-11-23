from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import os
import uuid

from eruna.models import Destination

class VacationBooking(models.Model):
    destination = models.ForeignKey(
        to=Destination,
        on_delete=models.CASCADE
    )
    user_id = models.IntegerField(
        _('User Id'),
        default='1'
    )
    total_price = models.DecimalField(
        _('Total Price'),
        decimal_places=2,
        max_digits=8
    )
    start_date = models.DateField(
        _('Start Date')
    )
    end_date = models.DateField(
        _('End Date')
    )
    is_complete = models.BooleanField(
        _("Vacation is complete"),
        default=False
    )
    added_on = models.DateTimeField(
        _("Upload On"),
        default=timezone.now,
        editable=False
    )
    def __str__(self) -> str:
        return f'{self.destination.name}'