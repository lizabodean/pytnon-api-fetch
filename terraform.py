import json
import requests

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


#Create a variable
def create_variable(type, key, value, sensitive, description):
    data = {
        "data": {
            "type":type,
            "attributes": {
            "key": key,
            "value": value,
            "description": description,
            "category": 'terraform',
            "hcl": False,
            "sensitive": sensitive
            },
            "relationships": {
            "workspace": {
                "data": {
                "id":"ws-f1oYyG7qpweuikUD",
                "type":"workspaces"
                }
            }
            }
        }
    }
    url = 'https://app.terraform.io/api/v2/vars'
    requests.post(url, headers=headers, data=json.dumps(data))


#Get variables for a workspace
def get_list_variables():
    url =f'https://app.terraform.io/api/v2/vars?filter%5Borganization%5D%5Bname%5D={organization}&filter%5Bworkspace%5D%5Bname%5D=workspace_set_var'
    response = requests.get(url, headers=headers)
    return response

# Update a variable.
def update_variables(id, key, value, description):
    data = {
        "data": {
            "id": id,
            "attributes": {
            "key": key,
            "value": value,
            "description": description,
            "category": 'terraform',
            "hcl": False,
            "sensitive": False
            },
            "type":"vars"
        }
    }
    url = f'https://app.terraform.io/api/v2/vars/{id}'
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    return response


#  Delete the variable we created.
def delete_variables(id):
    url = f'https://app.terraform.io/api/v2/vars/{id}'
    response = requests.delete(url, headers=headers)
    return response


def get_workspace(name):
    url = f'{base_url}/workspaces'
    response = requests.get(url, headers=headers)
    workspace_ans = None
    if response.status_code == 200:
        workspaces = response.json()
        for workspace in workspaces['data']:
            if workspace['attributes']['name'] == name:
                workspace_ans = workspace     
    else:
        print(f'Failed to retrieve workspaces. Status code: {response.status_code}')
    return workspace_ans

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
    #create_workspace(f'workspace_set_var')
    #list_workspaces()
    #workspace = get_workspace('workspace_set_var')
    create_variable('test', 'key', 'value', False, 'description')
    print('create_variable')
    list_variables = get_list_variables()
    variable_id = list_variables.json()['data'][0]['id']
    print(list_variables.json())
    update_variables(variable_id, 'test', 'test', 'test')
    print('update_variables')
    list_variables = get_list_variables()
    print(list_variables.json())
    delete_variables(variable_id)
    print('delete_variables')
    list_variables = get_list_variables()
    print(list_variables.json())
