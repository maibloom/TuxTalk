sudo mkdir /usr/bin/TuxTalk

chmod +x TuxTalk.desktop
chmod +x TuxTalk.py

sudo cp TuxTalk.py /usr/bin/TuxTalk/ && sudo cp TuxTalk.png /usr/bin/TuxTalk/

cp TuxTalk.desktop ~/.local/share/applications/

update-desktop-database ~/.local/share/applications