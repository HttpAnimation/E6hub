# Head
echo "E6hub downloader"
echo "Flavor: Non remove-temp"
echo "Github: https://github.com/HttpAnimation/E6hub"
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
sleep 2

## Body
# Download
git clone -b stable https://github.com/HttpAnimation/E6hub.git
cd E6hub
mv '[PUBLIC] clientconfig.json' clientconfig.json
cd ../
# Foot
echo "Done installing"
rm install.bash