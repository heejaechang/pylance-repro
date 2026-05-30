"""Main file that imports from mylib, which should be discoverable via sitecustomize.py.

If Pylance sets cwd=workspace_root when discovering sys.path, sitecustomize.py will add
./lib to sys.path and this import will resolve. If cwd is wrong, this import will be unresolved.
"""
from mylib import greet, MY_CONSTANT

print(greet("world"))
print(MY_CONSTANT)
