from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse


class Rateable(models.Model):
    """An entity that can have ratings"""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rateable_objects',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)  # TODO: Convert to something like tags

    class Meta:
        unique_together = ('owner', 'name', )  # So name can be used as ID by client, different clients can have same name

    def __str__(self):
        return f'{self.type} - {self.name} by {self.owner}'

    def get_absolute_url(self):
        return reverse('rateable:rateable-detail', args=(self.pk,))
