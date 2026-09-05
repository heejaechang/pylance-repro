from django.db import models


class AbstractNetwork(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Network(AbstractNetwork):
    group = models.ForeignKey(
        "groups.Group",
        related_name="networks",
        on_delete=models.CASCADE,
    )
