"""Runtime check for https://github.com/microsoft/pylance-release/issues/8191."""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

import django

django.setup()

from sample.groups.models import Group
from sample.networks.models import Network

group_field = Network._meta.get_field("group")
reverse_accessor = group_field.remote_field.get_accessor_name()

assert reverse_accessor == "networks"
assert hasattr(Group, "networks")

print(f"reverse accessor: {reverse_accessor}")
print(f"Group.networks: {Group.networks!r}")
