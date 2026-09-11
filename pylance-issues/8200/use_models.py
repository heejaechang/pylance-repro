from sample.groups.models import Group

network = Group().networks.get()
# CHECK: direct reverse-manager result has group completion
network.group

network_from_method = Group().get_networks().get()
# CHECK: method reverse-manager result has group completion
network_from_method.group
