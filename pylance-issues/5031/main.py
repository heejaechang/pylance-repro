from django.db import models

class MyModel(models.Model):
    nullable = models.IntegerField(null=True)

def foo():
    m = MyModel.objects.get()

    def accepts_only_int(x: int):
        pass

    accepts_only_int(m.nullable)
