echo "E6hub downloader"
echo "Flavor: Normal"
echo "Github: https://github.com/HttpAnimation/E6hub"
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
sleep 2

git clone https://github.com/HttpAnimation/E6hub.git
cd E6hub
mv '[PUBLIC] clientconfig.json' clientconfig.json
rm README.md
rm UserFavDownloads/GITHUBDONTREMOVEME.md
rm UserFavDownloads/jsonData/GITHUBDONTREMOVEME.md