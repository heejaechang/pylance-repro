# Repro for https://github.com/microsoft/pylance-release/issues/8005
# Title: Erroneous tooltip hyperlinking behaviour for restructured text when using py:meth directive to reference dunder in same class
# See README.md in this workspace for the full reporter context.

class Ham:
    def __init__(self, spam): '''Initialize the Ham.'''
    def ham(self): '''Frobnicate the Ham according to the spam parameter passed to :meth:`__init__`.'''
