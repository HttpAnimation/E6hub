echo "E6hub downloader"
echo "Flavor: Normal"
echo "Github: https://github.com/HttpAnimation/E6hub"
echo "Note: This script it going under a rewrite."
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
sleep 2

echo "Cloneing the repo."
git clone -b stable https://github.com/HttpAnimation/E6hub.git
echo "Heading into E6hub"
cd E6hub
echo "Done"

echo "Removing files"
rm InstallNonRM.bash
rm install.bash
rm MakeCD.bash
rm Personal.bash
rm README.md
rm -rf .git
rm .gitignore
rm download.py
echo "Done"

echo "Moving up"
cd ../
rm install.bash