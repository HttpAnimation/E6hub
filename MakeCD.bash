#!/bin/bash

# Safety Warning
echo "WARNING: This script is intended for the dev system only. Proceed with caution."

# Change directory
target_directory="/home/httpanimations/Desktop"
cd "$target_directory" || exit 1

# Check if the folder exists and remove if it does
folder="E6hub"
if [ -d "$folder" ]; then
    rm -rf "$folder"
    echo "Folder '$folder' removed successfully."
else
    echo "Folder '$folder' does not exist."
fi

# Download script from URL and rename
wget -O install.bash https://raw.githubusercontent.com/HttpAnimation/E6hub/stable/installNonRM.bash

# Check if download was successful
if [ $? -eq 0 ]; then
    echo "Downloaded install script successfully."
    bash install.bash
else
    echo "Failed to download install script."
    exit 1
fi
