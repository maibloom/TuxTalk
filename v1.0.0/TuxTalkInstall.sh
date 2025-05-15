sudo mkdir -p /usr/bin/TuxTalk
sudo mkdir -p /usr/share/applications/

chmod +x TuxTalk.desktop
chmod +x TuxTalk.py

sudo cp TuxTalk.py /usr/bin/TuxTalk/
sudo cp TuxTalk.png /usr/bin/TuxTalk/
sudo cp TuxTalk.desktop /usr/share/applications/
sudo update-desktop-database /usr/share/applications/

echo "Installation completed!"
