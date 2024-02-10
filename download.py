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
        "User-Agent": f"E6hub/1.3 (by {username} on e621)"
    }
    auth = (username, api_key)
    page = 1
    total_favorites = 0
    
    while True:
        params = {"page": page}
        response = requests.get(base_url, headers=headers, auth=auth, params=params)
        
        if response.status_code == 200:
            data = response.json()
            favorites = data.get("posts", [])
            if not favorites:
                break
            total_favorites += len(favorites)
            save_directory = "UserFavDownloads/jsonData"
            os.makedirs(save_directory, exist_ok=True)
            for idx, favorite in enumerate(favorites):
                filename = os.path.join(save_directory, f"favorite_{total_favorites - len(favorites) + idx}.json")
                with open(filename, "w") as file:
                    json.dump(favorite, file, indent=4) 
                print(f"Favorite {total_favorites - len(favorites) + idx + 1} downloaded and saved as {filename}")
            page += 1
        else:
            print(f"Failed to download favorites. Status code: {response.status_code}")
            break

def main():
    username, api_key = load_config()
    if username and api_key:
        download_favorites(username, api_key)
    else:
        print("Invalid configuration. Please check clientconfig.json.")

if __name__ == "__main__":
    main()
