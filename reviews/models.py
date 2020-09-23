from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField(
        _("accuracy"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    communication = models.IntegerField(
        _("communication"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    cleanliness = models.IntegerField(
        _("cleanliness"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    location = models.IntegerField(
        _("location"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    check_in = models.IntegerField(
        _("check_in"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    value = models.IntegerField(
        _("value"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Average"

    class Meta:
        ordering = ("-created",)
