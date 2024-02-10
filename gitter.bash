mkdir E6hub
cd E6hub
git clone -b stable https://github.com/HttpAnimation/E6hub.git
mv E6hub stable
git clone -b main https://github.com/HttpAnimation/E6hub.git
mv E6hub main
git clone -b gh-pages https://github.com/HttpAnimation/E6hub.git
mv E6hub gh-pages
git clone -b blank https://github.com/HttpAnimation/E6hub.git
mv E6hub blank
echo "done"
cd ../
rm gitter.bash
