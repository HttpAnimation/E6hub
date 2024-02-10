import os
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
        "User-Agent": f"MyProject/1.0 (by {username} on e621)"
    }
    auth = (username, api_key)

    response = requests.get(base_url, headers=headers, auth=auth)
    
    if response.status_code == 200:
        favorites = response.json()
        save_directory = "UserFavDownloads"
        os.makedirs(save_directory, exist_ok=True)
        for idx, favorite in enumerate(favorites):
            filename = os.path.join(save_directory, f"favorite_{idx}.json")
            with open(filename, "w") as file:
                json.dump(favorite, file, indent=4) 
            print(f"Favorite {idx + 1} downloaded and saved as {filename}")
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
