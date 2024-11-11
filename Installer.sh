# downloading the required dependency

sudo pacman -S qutebrowser

# giving permisions to everything

chmod +x *

# move one backward, because we're in side the TuxTalk folder, but we want to move the folder itself.

cd ..

# move codes and etc to /usr/bin

sudo mv TuxTalk/TuxTalk /usr/bin

# moving the starting app to the desktop

mv /usr/bin/TuxTalk/TuxTalk.desktop ~/Desktop
