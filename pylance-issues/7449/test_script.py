from azure.identity import AzureCliCredential
from azure.mgmt.authorization import AuthorizationManagementClient

subscription = "<GUID of valid Azure subscription I'm logged in to>"
credential = AzureCliCredential()
auth_client = AuthorizationManagementClient(credential, subscription)
role_assignments_iterable = auth_client.role_assignments.list_for_subscription()
role assignments = []
for role_assignment in role_assignments iterable:
    role_assignments.append(role_assignment)
