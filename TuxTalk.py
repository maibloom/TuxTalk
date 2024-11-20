# File: TuxTalk.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # Import QUrl

class WebLoader(QMainWindow):
    def __init__(self, url: str):
        super().__init__()
        self.setWindowTitle("TuxTalk")

        # Create the main layout
        self.browser = QWebEngineView()

        # Convert the URL string to a QUrl object
        self.browser.setUrl(QUrl(url))

        # Set the central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # URL of the website to load
    website_url = "https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1"

    window = WebLoader(website_url)
    window.resize(1024, 768)
    window.show()

    sys.exit(app.exec_())
