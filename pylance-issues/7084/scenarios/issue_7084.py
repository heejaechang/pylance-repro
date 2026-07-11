# SCENARIO: reStructuredText support should not leak literal `&nbsp;` entities into hover docstrings
# TARGET: hover on `ThreadPoolExecutor` in the constructor call
# TRIGGER: enable supportRestructuredText and show hover on the call target
# EXPECT: the hover docstring renders readable argument docs without visible `&nbsp;` sequences
# VERIFY: if the hover text still includes literal `&nbsp;` or the broken collapsed spacing pattern, the bug still reproduces
# RECOVER: no recovery needed

from concurrent.futures import ThreadPoolExecutor


x = ThreadPoolExecutor(max_workers=1)