import requests

# Define your e621 username and API key
username = "your_username"
api_key = "your_api_key"

# Define the base URL for the favorites endpoint
base_url = "https://e621.net/favorites.json"

headers = {
    "User-Agent": f"MyProject/1.0 (by {username} on e621)",
    "Authorization": f"Basic {api_key}"
}

def download_favorites():
    response = requests.get(base_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        favorites = response.json()
        for favorite in favorites:
            print(favorite)  
    else:
        print(f"Failed to download favorites. Status code: {response.status_code}")

download_favorites()
