# Repro for pylance-release issue #8127
# "[TSP] Goto implementation doesn't work for Pyrefly"
#
# Setup: configure Pylance to use Pyrefly as the diagnostics source (external
# type server over TSP), then open this file.
#
# Steps:
#   Right click on `BaseWithConcreteMethod.method` (the `method` name on the
#   line below) and select `Go To Implementations` / `Find All Implementations`.
#
# Expected result:
#   All overrides are shown:
#     - BaseWithConcreteMethod.method
#     - Intermediate.method
#     - Derived2.method
#
# Actual result (bug):
#   Only the clicked symbol (BaseWithConcreteMethod.method) is returned.
from abc import ABC


class BaseWithConcreteMethod(ABC):
    def method(self):  # <-- invoke Go To Implementations here on `method`
        ...


class Intermediate(BaseWithConcreteMethod):
    def method(self):
        pass


class Derived2(Intermediate):
    def method(self):
        pass
