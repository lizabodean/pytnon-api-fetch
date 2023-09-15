import requests
import random

import os
from dotenv import load_dotenv

load_dotenv()
#environment variables

api_token = os.getenv('API_TOKEN')
organization = os.getenv('ORGANIZATION')
base_url = os.getenv('BASE_URL')

# Define headers with the API token
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/vnd.api+json',
}

# Example: List workspaces
def list_workspaces():
    url = f'{base_url}/workspaces'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        workspaces = response.json()
        for workspace in workspaces['data']:
            print(workspace['attributes']['name'])
    else:
        print(f'Failed to retrieve workspaces. Status code: {response.status_code}')

# Example: Create a workspace
def create_workspace(workspace_name):
    url = f'{base_url}/workspaces'
    data = {
        'data': {
            'type': 'workspaces',
            'attributes': {
                'name': workspace_name
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'Workspace "{workspace_name}" created successfully.')
    else:
        if response.status_code == 422:
            print(f'Failed to create workspace. workspace was created')  
        else:
            print(f'Failed to create workspace. Status code: {response.status_code}')

if __name__ == '__main__':
    list_workspaces()
    create_workspace(f'workspace_{random.randint(1, 200)}')
