# Move the TuxTalk directory to /usr/bin
mv TuxTalk /usr/bin/

# Compile the C program and place the binary in /usr/bin/TuxTalk
gcc /usr/bin/TuxTalk/my_program.c -lcurl -lwebview -lX11 -o /usr/bin/TuxTalk/TuxTalk

# Set executable permissions for the compiled binary
chmod +x /usr/bin/TuxTalk/TuxTalk

# Copy the .desktop file to /usr/share/applications to make it accessible in the application menu
cp /usr/bin/TuxTalk/TuxTalk.desktop /usr/share/applications/
