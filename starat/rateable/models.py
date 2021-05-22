from django.db import models
from django.db.models import Avg
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
        
    def get_average_rating(self):
        ratings = self.ratings.all()
        avg_stars = ratings.aggregate(Avg('stars'))['stars__avg']
        return int(avg_stars)


class Rating(models.Model):
    """A rating for a Rateable object"""

    rateable = models.ForeignKey(
        Rateable,
        related_name='ratings',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    reviewer = models.CharField(max_length=255, null=True, blank=True)
    stars = models.IntegerField(min=1, max=10, null=False, blank=False)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.stars} - {self.rateable}'
