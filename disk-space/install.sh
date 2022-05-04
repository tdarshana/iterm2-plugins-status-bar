# Install Package. Need to restart iTerm after this.
echo "Installing Statusbar plugin, disk-space.."
mkdir -p ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/disk-space

cp -r ./disk-space ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/disk-space
cp setup.cfg ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/disk-space
cp metadata.json ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/disk-space
echo "plugin disk-space installation completed."
