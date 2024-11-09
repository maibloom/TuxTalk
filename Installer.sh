# Install pip
sudo pacman -S python-pip

# Install dependencies
sudo pacman -Sy pkg-config gtk3 webkit2gtk

# Install Python packages
pip install pywebview
pip install pyinstaller
pip install requests
pip install screeninfo

# Build the executable
sudo pyinstaller --onefile --name "TuxTalk" --distpath /usr/local/bin/Tux-talk Tuxtalk.py

# Move the .desktop file to the right location
mv tux-talk.desktop ~/.local/share/applications/

# Move the logo too
mv logo.png /usr/local/bin/Tux-talk

# Make the .desktop file executable
chmod +x ~/.local/share/applications/tux-talk.desktop
