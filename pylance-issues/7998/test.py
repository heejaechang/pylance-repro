"""
Repro for https://github.com/microsoft/pylance-release/issues/7998

When auto-completing __init__ override of FileSensor, Pylance replaces
complex default values (like conf.getboolean(...)) with `...` (Ellipsis)
instead of preserving the original default expression.

Steps:
1. Open this file in VS Code with Pylance
2. Place cursor inside _FileSensor class
3. Start typing `def __init__` and accept the auto-completion
4. Observe that `deferrable` parameter's default value becomes `...`
   instead of `conf.getboolean("operators", "default_deferrable", fallback=False)`
"""

from base import FileSensor


class _FileSensor(FileSensor):
    def __init__
