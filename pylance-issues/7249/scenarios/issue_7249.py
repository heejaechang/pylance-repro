# SCENARIO: return type inlay hints for functions returning `attrgetter` and `itemgetter` should not insert invalid subscripted runtime types
# TARGET: the return type inlay hints on `customattrgetter` and `customitemgetter`
# TRIGGER: apply the visible return type inlay hints
# EXPECT: any inserted return type annotation remains runtime-valid for `operator.attrgetter` and `operator.itemgetter`
# VERIFY: the inserted annotations do not subscript `attrgetter` or `itemgetter`
# RECOVER: revert the file to its original text after the check

from operator import attrgetter, itemgetter


def customattrgetter():
    return attrgetter('age', 'name')


def customitemgetter():
    return itemgetter('age', 'name')