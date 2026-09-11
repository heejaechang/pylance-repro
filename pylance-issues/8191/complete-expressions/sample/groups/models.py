from django.db import models


class AbstractGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Group(AbstractGroup):
    def get_networks(self):
        # CHECK: reverse relation is recognized
        return self.networks.all()

    def get_first_network(self):
        # CHECK: self has a networks completion
        return self.networks.get()


# CHECK: use_models.py direct result has group completion
# CHECK: use_models.py method result has group completion
