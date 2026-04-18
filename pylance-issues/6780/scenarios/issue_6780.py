# SCENARIO: installed scikit-learn 1.6.0 should expose `sklearn.utils.Tags` from the selected environment rather than falling back to bundled stubs.
# TARGET: the imported `Tags` symbol below and the bad call to `accepts_tags('not tags')`.
# TRIGGER: wait for diagnostics, inspect Problems, then use hover/definition on `Tags` if needed to disambiguate.
# EXPECT: `Tags` resolves as a real symbol from the installed scikit-learn package, not as an unknown or `Any` symbol from bundled stubs.
# VERIFY: Problems should report an argument-type mismatch for `accepts_tags('not tags')`; if no type error appears, treat that as evidence that `Tags` degraded to `Any` or otherwise failed to resolve strongly.
# RECOVER: no recovery needed.

from sklearn.utils import Tags


def accepts_tags(value: Tags) -> None:
	pass


accepts_tags('not tags')