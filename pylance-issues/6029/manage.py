 # SCENARIO: Django deprecation warning imports should resolve from the bundled stubs
 # TARGET: `RemovedInDjango51Warning` on the import line
 # TRIGGER: hover or go to definition on `RemovedInDjango51Warning`
 # EXPECT: Pylance resolves the symbol from `django.utils.deprecation`
 # VERIFY: if the symbol is unresolved or reported missing, the bug still reproduces
 # RECOVER: no recovery needed

from django.utils.deprecation import RemovedInDjango51Warning


warning_cls = RemovedInDjango51Warning