from django.db import models


class AbstractGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Group(AbstractGroup):
    def get_networks(self):
        # Pylance reports reportAttributeAccessIssue on this direct access.
        return self.networks.all()
