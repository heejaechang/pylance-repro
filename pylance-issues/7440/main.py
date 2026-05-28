"""
Issue #7440 repro: Diagnostics for stdlib/external-package files persist after close.

Steps:
1. Open this file in VS Code with Pylance active
2. Ctrl+click on `.run` below to go to definition in asyncio/runners.py
3. Observe diagnostics appear in the Problems panel for runners.py
4. Close the runners.py tab
5. Check if diagnostics for runners.py persist in the Problems panel

Expected: Diagnostics for runners.py are cleared when the file is closed
Actual (bug): Diagnostics persist until language server restart
"""

from asyncio import Runner


async def main():
    print("Hello, World!")


Runner().run(main())
