# Install Package. Need to restart iTerm after this.
echo "Installing Statusbar plugin, wifi-signal.."

mkdir -p ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/wifi-signal

cp -r ./wifi-signal ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/wifi-signal
cp setup.cfg ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/wifi-signal
cp metadata.json ${HOME}/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/wifi-signal
echo "plugin wifi-signal installation completed."
