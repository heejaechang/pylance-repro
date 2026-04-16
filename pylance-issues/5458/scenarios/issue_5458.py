# SCENARIO: Django model field calls should offer keyword parameter completions for a typed prefix
# TARGET: the trailing `c` in `models.CharField(max_length=1, null=False, c)` below
# TRIGGER: Completion
# EXPECT: completion opens at the partial keyword-argument position inside the `CharField` call
# VERIFY: the suggestion list includes at least one `CharField` keyword parameter starting with `c`, such as `choices=`
# RECOVER: no recovery needed

from django.db import models


class Transacoes(models.Model):
    tipo = models.CharField(max_length=1, null=False, c)

    class Meta:
        managed = False
        db_table = 'transacoes'