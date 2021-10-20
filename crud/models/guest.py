from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(blank=False, unique=True)

    class Meta:
        verbose_name = "Guest"

    def __str__(self):
        return f"{self.name}"
