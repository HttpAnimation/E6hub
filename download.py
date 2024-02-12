import os
import json
import concurrent.futures
import wget
import requests

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

def download_favorite(favorite, index, save_directory):
    json_filename = os.path.join(save_directory, f"favorite_{index}.json")
    with open(json_filename, "w") as file:
        json.dump(favorite, file, indent=4)
    print(f"Favorite {index + 1} JSON data saved as {json_filename}")

    media = favorite.get("file", {})
    if media:
        media_url = media.get("url", "")
        if media_url:
            media_extension = os.path.splitext(media_url)[1].lower()
            media_folder = os.path.join(save_directory, media_extension[1:] + "s")
            os.makedirs(media_folder, exist_ok=True)
            media_filename = os.path.join(media_folder, f"favorite_{index}{media_extension}")
            wget.download(media_url, out=media_filename)
            print(f"Downloaded {media_filename}")
    else:
        print(f"No media found for favorite {index + 1}")

def download_favorites(username, api_key):
    base_url = "https://e621.net/favorites.json"
    headers = {
        "User-Agent": f"E6hub/1.8 (by {username} on e621)"
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
            save_directory = "UserFavDownloads"
            os.makedirs(save_directory, exist_ok=True)

            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                futures = []
                for idx, favorite in enumerate(favorites, total_favorites - len(favorites)):
                    futures.append(executor.submit(download_favorite, favorite, idx, save_directory))
                concurrent.futures.wait(futures)

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
