 # SCENARIO: local packages should win over matching typeshed fallback packages for `from package import module`
 # TARGET: `import_export_module` in the import and call below
 # TRIGGER: hover or go to definition on `import_export` or `import_export_module`
 # EXPECT: resolution stays inside the local `import_export/` package
 # VERIFY: if navigation jumps to the typeshed fallback package instead, the bug still reproduces
 # RECOVER: no recovery needed

from import_export import import_export_module


import_export_module.say_hello()