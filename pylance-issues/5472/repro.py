 # SCENARIO: go to definition should work for `shutil.rmtree` the same way it works for neighboring imports
 # TARGET: `rmtree` in the import statement below
 # TRIGGER: run go to definition on `rmtree`
 # EXPECT: navigation reaches the stdlib implementation or matching stub for `rmtree`
 # VERIFY: if `rmtree` lacks go to definition while `copyfile` and `copy` work, the bug still reproduces
 # RECOVER: no recovery needed

from shutil import copyfile, copy, rmtree

rmtree('tmp')
