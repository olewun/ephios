from django.db import models
from django.utils.translation import gettext_lazy as _

from ephios.core.models import Shift


class ResourceCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.name


class Resource(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    category = models.ForeignKey(
        ResourceCategory, on_delete=models.CASCADE, verbose_name=_("Category")
    )

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.title


class ResourceAllocation(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    resources = models.ManyToManyField(Resource, blank=True, verbose_name=_("Resources"))

    def __str__(self):
        return f"Resource allocation for {self.shift}"
