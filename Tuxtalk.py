# filename: WebApp.py
import subprocess
import sys

# List of required packages
required_packages = ["requests", "pywebview"]

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Import after installation
import webview
import requests

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

# Open the URL in an embedded web browser window
webview.create_window("My Web App", url)
webview.start()
