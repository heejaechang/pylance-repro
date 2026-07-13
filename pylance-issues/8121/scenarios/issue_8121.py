# Repro for pylance-release#8121
# When Pyrefly is the diagnostics source over TSP, an unresolved name like `os`
# should offer an "Add `import os`" quick fix. The bug is that only
# "ignore type error" fixes are offered.
#
# `os` is intentionally used WITHOUT `import os` so a diagnostic fires and
# quick fixes can be triggered on it.

print(os.getcwd())
