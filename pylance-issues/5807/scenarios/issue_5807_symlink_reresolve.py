# Issue 5807: Symlinking a directory does not cause a reresolve of imports
#
# Setup:
# - Workspace has importer.py with `from exporter import *`
# - `non_linked/` directory exists with `__init__.py` defining `foo_func`
# - Initially the import is unresolved (exporter/ doesn't exist)
# - User symlinks non_linked/ to exporter/
#
# Expected: Import error disappears without reloading VS Code
# Actual: VS Code must be reloaded before the error clears
#
# Root cause: In service.ts `_shouldHandleSourceFileWatchChanges`, when a folder
# watch event fires for the newly-symlinked directory, the handler checks:
#   1) Does the parent have __init__.py? (No, parent is workspace root)
#   2) Does program.containsSourceFileIn(path)? (No, it's brand new)
# Since both are false, the event is dropped and no re-analysis occurs.

from exporter import *
