import subprocess
import sys
import webview
import requests
import screeninfo  # For screen size detection

# List of required packages
required_packages = ["requests", "pywebview", "screeninfo"]

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# URL of the website to open
url = "https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1"

# Function to fetch HTML content (optional)
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return None

# Get screen information (assuming the first monitor)
screen = screeninfo.get_monitors()[0]

# Calculate 1/3 of the screen width and height
window_width = screen.width // 3
window_height = screen.height

# Set the window to appear on the right side
x_position = screen.width - window_width  # Position the window on the right side
y_position = 0  # Start from the top of the screen

# Open the URL in an embedded web browser window with calculated size and position
webview.create_window("My Web App", url, width=window_width, height=window_height, x=x_position, y=y_position)
webview.start()
