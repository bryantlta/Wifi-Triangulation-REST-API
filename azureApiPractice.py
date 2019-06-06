import urllib.request
import json

azure_client_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
azure_secret = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
azure_subscription_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
azure_tenant = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
resource_group_name = 'my-new-resourcegroup'

# authorize with azure
url = "https://login.windows.net/" + azure_tenant + "/oauth2/token"
data = "resource=https%3A%2F%2Fmanagement.core.windows.net%2F&client_id=" + azure_client_id + "&grant_type=client_credentials&client_secret=" + azure_secret
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = urllib.request.post(url, data=data, headers=headers)
print(response.json())

# create new resource group using Azure REST API
url = "https://management.azure.com/subscriptions/" + azure_subscription_id + "/resourcegroups/" + resource_group_name + "?api-version=2017-05-10"
headers = { 'Authorization': 'Bearer ' + response.json()['access_token'], 'Content-Type': 'application/json' }
body = { 'name': resource_group_name, 'location': 'eastus' }
response = urllib.request.put(url, data=json.dumps(body), headers=headers)

print(response.json())