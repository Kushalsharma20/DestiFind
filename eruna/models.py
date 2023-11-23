from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(f'images/{instance.__class__.__name__}', filename)

class Destination(models.Model):
    name = models.CharField(
        _('Destination Name'),
        max_length=256
    )
    description = models.TextField(
        _('Destination Description')
    )
    location = models.CharField(
        _('Destination Location'),
        max_length=256
    )
    price = models.IntegerField(
        _('Cost of Vacation')
    )
    distance = models.IntegerField(
        _('Distance From Kampala'),
        blank=True,
        null=True
    )
    slug = models.SlugField(
        _("Safe Url"),
        unique=True,
        blank = True,
        null = True,
    )
    related_url = models.URLField(
        _('Url To Related Article'),
        blank=True,
        null=True,
    )
    added_on = models.DateTimeField(
        _("Upload On"),
        default=timezone.now,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        self.name = self.name.title()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name}'


class DestinationImage(models.Model):
    destination = models.ForeignKey(
        to=Destination,
        on_delete=models.CASCADE
    )
    img_url = models.ImageField(
        _('Image Url'),
        blank=True,
        null=True,
        upload_to=get_file_path
    )
    online_url = models.URLField(
        _('Online Image Url'),
        blank=True,
        null=True,
    )
    added_on = models.DateTimeField(
        _("Upload On"),
        default=timezone.now,
    )

    def __str__(self) -> str:
        return f'{self.destination.name}'
