"""sitecustomize.py — adds ./lib to sys.path based on cwd.

This reproduces the user's scenario from issue #7109.
When Python is invoked with cwd=workspace_root, this adds workspace_root/lib to sys.path.
When cwd is the extension directory or /, lib will not be found.
"""
import os
import sys

lib_path = os.path.join(os.getcwd(), "lib")
if os.path.isdir(lib_path):
    sys.path.insert(0, lib_path)
