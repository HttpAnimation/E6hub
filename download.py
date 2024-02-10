import requests
import json

def load_config():
    try:
        with open("clientconfig.json", "r") as config_file:
            config = json.load(config_file)
            if len(config) > 0:
                return config[0].get("Username", ""), config[0].get("Token", "")
            else:
                print("Configuration file is empty.")
                return "", ""
    except FileNotFoundError:
        print("Configuration file not found.")
        return "", ""

def download_favorites(username, api_key):
    base_url = "https://e621.net/favorites.json"

    headers = {
        "User-Agent": f"MyProject/1.0 (by {username} on e621)",
        "Authorization": f"Basic {api_key}"
    }

    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        favorites = response.json()
        for favorite in favorites:
            print(favorite)  
    else:
        print(f"Failed to download favorites. Status code: {response.status_code}")

def main():
    username, api_key = load_config()
    if username and api_key:
        download_favorites(username, api_key)
    else:
        print("Invalid configuration. Please check clientconfig.json.")

if __name__ == "__main__":
    main()
