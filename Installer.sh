# Install dependencies
pip install pywebview
pip install pyinstaller

# Build the executable
sudo pyinstaller --onefile --name "TuxTalk" --distpath /usr/local/bin/Tux-talk Tuxtalk.py

# Move the .desktop file to the right location
mv tux-talk.desktop ~/.local/share/applications/

# Move the logo too
mv logo.png /usr/local/bin/Tux-talk

# Make the .desktop file executable
chmod +x ~/.local/share/applications/tux-talk.desktop
