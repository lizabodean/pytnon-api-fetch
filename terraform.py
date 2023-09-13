import requests
import json

# Define your Terraform Cloud API token and organization name
api_token = 'MpFhzJUy7JMbHw.atlasv1.c6zqvTdzgCFxziuyYtNh6u8xKzeqmTEDP5xO8YBYu7juz83sM54THVznv6Qdk7OH528'
organization = 'Practice-UTM'

# Set the base URL for Terraform Cloud API
base_url = f'https://app.terraform.io/api/v2/organizations/Practice-UTM'

# Define headers with the API token
headers = {
    "Authorization": f'Bearer {api_token}',
    "Content-Type": 'application/vnd.api+json',
}

# Example: List workspaces
def list_workspaces():
    url = f"{base_url}/workspaces"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        workspaces = response.json()
        for workspace in workspaces['data']:
            print(workspace['attributes']['name'])
    else:
        print(f"Failed to retrieve workspaces. Status code: {response.status_code}")

# Example: Create a workspace
def create_workspace(workspace_name):
    url = f"{base_url}/workspaces"
    data = {
        "data": {
            "type": "workspaces",
            "attributes": {
                "name": workspace_name
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Workspace '{workspace_name}' created successfully.")
    else:
        print(f"Failed to create workspace. Status code: {response.status_code}")

if __name__ == "__main__":
    list_workspaces()
    create_workspace("my_new_workspace3")  # Uncomment to create a new workspace