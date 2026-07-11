 # SCENARIO: Django auto-import suggestions should include deeper modules like `django.utils.timezone`
 # TARGET: `timezone` in `timezone.now()`
 # TRIGGER: invoke the auto-import quick fix on `timezone`
 # EXPECT: suggestions include `from django.utils import timezone`
 # VERIFY: if the desired deep import is missing from the quick fix list, the enhancement still reproduces
 # RECOVER: undo the import change

import datetime

from django.db import models


class Question(models.Model):
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)