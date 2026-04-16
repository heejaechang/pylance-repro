 # SCENARIO: compiled modules with `.pyc` and `.pyi` but no `.py` source should not trigger `reportMissingModuleSource`
 # TARGET: `from compiledmod import VALUE`
 # TRIGGER: run `python .\generate_compiledmod.py`, then inspect diagnostics on the import
 # EXPECT: the import resolves without `reportMissingModuleSource`
 # VERIFY: if Pylance still complains about missing module source after generating `compiledmod.pyc`, the bug still reproduces
 # RECOVER: delete `compiledmod.pyc` and rerun the generator when needed

from compiledmod import VALUE


result = VALUE