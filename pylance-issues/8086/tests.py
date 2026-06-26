import unittest


class MyTest(unittest.TestCase):
    def test_foo(self):
        # Issue #8086 repro target:
        # Place the cursor on `assertEqual` below and invoke "Go to Definition".
        # Expected: jumps to TestCase.assertEqual in the unittest stub.
        # Actual (with Pyrefly as diagnostics source): "No definition found".
        self.assertEqual(1, 1)
