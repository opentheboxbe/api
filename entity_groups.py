import sys
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
session.cookies['user.language'] = 'nl'
auth0_otb_test_client_id = ""
auth0_otb_test_client_secret = ""
root_url = "https://openthebox.be"

def get_entity_groups(token):
    token = token or get_auth0_token(auth0_otb_test_client_id, auth0_otb_test_client_secret)

    url = root_url + "/api/entity-group-summaries"

    headers = {
        "authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    print("Getting the entity groups via " + url + "...")
    response = session.get(url, headers=headers, verify=False, timeout=120)

    if response.status_code != requests.codes.ok:
        print("Get entity groups error, status code = " + str(response.status_code) + ", content:" + response.text + ". Aborting.")
        return None

    return response.json()


def create_entity_group(token):
    token = token or get_auth0_token(auth0_otb_test_client_id, auth0_otb_test_client_secret)

    url = root_url + "/api/entity-groups"

    headers = {
        "authorization": "Bearer " + token,
        "Csrf-Token": "nocheck",
        "Content-Type": "application/json"
    }

    vats = ["BE0123456789"]

    data = {
        "name": "Test",
        "vats": vats,
    }

    print("Creating the entity group via " + url + "...")
    response = session.post(url, data=json.dumps(data), headers=headers, verify=False, timeout=120)

    if response.status_code != requests.codes.ok:
        print("Create entity group error, status code = " + str(response.status_code) + ", content:" + response.text + ". Aborting.")
        return False

    return True


def update_entity_group_add_items(entity_group_id, token):
    token = token or get_auth0_token(auth0_otb_test_client_id, auth0_otb_test_client_secret)

    url = root_url + "/api/entity-groups/" + entity_group_id + "/items"

    headers = {
        "authorization": "Bearer " + token,
        "Csrf-Token": "nocheck",
        "Content-Type": "application/json"
    }

    vats = ["BE0123456789", "BE0111111111", "BE0111111111"]

    data = {
        "vats": vats,
    }

    print("Adding the items to the entity group via " + url + "...")
    response = session.post(url, data=json.dumps(data), headers=headers, verify=False, timeout=120)

    if response.status_code != requests.codes.ok:
        print("Update entity group add items error, status code = " + str(response.status_code) + ", content:" + response.text + ". Aborting.")
        return False

    return True


def update_entity_group_remove_items(entity_group_id, token):
    token = token or get_auth0_token(auth0_otb_test_client_id, auth0_otb_test_client_secret)

    url = root_url + "/api/entity-groups/" + entity_group_id + "/items"

    headers = {
        "authorization": "Bearer " + token,
        "Csrf-Token": "nocheck",
        "Content-Type": "application/json"
    }

    vats = ["BE0111111111", "BE0111111111", "BE0222222222"]

    data = {
        "vats": vats,
    }

    print("Removing the items from the entity group via " + url + "...")
    response = session.delete(url, data=json.dumps(data), headers=headers, verify=False, timeout=120)

    if response.status_code != requests.codes.ok:
        print("Update entity group remove items error, status code = " + str(response.status_code) + ", content:" + response.text + ". Aborting.")
        return False

    return True


def delete_entity_group(entity_group_id, token):
    token = token or get_auth0_token(auth0_otb_test_client_id, auth0_otb_test_client_secret)

    url = root_url + "/api/entity-groups/" + entity_group_id

    headers = {
        "authorization": "Bearer " + token,
        "Csrf-Token": "nocheck",
        "Content-Type": "application/json"
    }

    print("Deleting the entity group via " + url + "...")
    response = session.delete(url, headers=headers, verify=False, timeout=120)

    if response.status_code != requests.codes.ok:
        print("Delete entity group error, status code = " + str(response.status_code) + ", content:" + response.text + ". Aborting.")
        return False

    return True


def get_auth0_token(client_id, client_secret):
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": "https://openthebox.be/api",
        "grant_type": "client_credentials"
    }

    headers = {
        "content-type": "application/json"
    }

    url = root_url + "/oauth/token"
    
    token_response = requests.post(url, json.dumps(data), headers=headers, verify=False)

    if token_response.status_code == requests.codes.ok:
        return token_response.json()["access_token"]
    else:
        print("Unable to get authentication token from auth0, status code = " + str(token_response.status_code) + ", content:" + token_response.text + ". Aborting.")

        return None
