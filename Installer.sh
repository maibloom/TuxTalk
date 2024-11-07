# Install dependencies
pip install pywebview
pip install pyinstaller

# Build the executable
sudo pyinstaller --onefile --name "TuxTalk" --distpath /usr/local/bin Tuxtalk.py

# Move the .desktop file to the right location
mv tux-talk.desktop ~/.local/share/applications/

# Make the .desktop file executable
chmod +x ~/.local/share/applications/tux-talk.desktop
