import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Access environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
scope = os.getenv("SCOPE")
tenant_id = os.getenv("TENANT_ID")

# Step 2: Obtain an Access Token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
token_payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope
}

response = requests.post(token_url, headers=headers, data=token_payload)
access_token = response.json()["access_token"]

# Step 3: Construct and Send API Request to Update User Attribute
update_url = "https://graph.microsoft.com/v1.0/users/gjackson@zv1n6.onmicrosoft.com"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
data = {
    "jobTitle": "Grand Poobah"
}

update_response = requests.patch(update_url, headers=headers, json=data)

# patch returns an http code of 204 on success
if update_response.status_code == 204:
    print("User jobTitle updated successfully:")
else:
    print("Failed to update user jobTitle:", update_response.status_code)
    print(update_response.json())