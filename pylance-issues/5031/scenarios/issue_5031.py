# SCENARIO: installed `django-stubs` should take precedence over Pylance's bundled Django stubs.
# TARGET: `accepts_only_int(m.nullable)` and `models.IntegerField` in the model declaration.
# TRIGGER: wait for diagnostics to settle.
# EXPECT: when installed `django-stubs` wins, `accepts_only_int(m.nullable)` should not produce the nullable `int | None` mismatch described in the issue.
# VERIFY: if Pylance still reports that `int | None` cannot be assigned to `int`, treat that as evidence that bundled Django stubs still take precedence.
# RECOVER: no recovery needed.

from django.db import models


class MyModel(models.Model):
    nullable = models.IntegerField(null=True)


def foo() -> None:
    m = MyModel.objects.get()

    def accepts_only_int(x: int) -> None:
        pass

    accepts_only_int(m.nullable)