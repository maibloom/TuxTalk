#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineProfile
from PyQt5.QtCore import QUrl


class TuxTalk(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tux Talk")
        self.setGeometry(100, 100, 1000, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Navigation buttons
        self.reload_button = QPushButton("Reload")
        self.back_button = QPushButton("Back")
        self.forward_button = QPushButton("Forward")

        self.reload_button.clicked.connect(self.reload_active_tab)
        self.back_button.clicked.connect(self.go_back)
        self.forward_button.clicked.connect(self.go_forward)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.reload_button)

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.tabs)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        # Add tabs dynamically
        urls = {
            "Duck Duck Go AI": "https://duckduckgo.com/?q=DuckDuckGo%20AI%20Chat&ia=chat&duckai=1",
            "Copilot AI": "https://copilot.microsoft.com/"
        }
        for name, url in urls.items():
            self.add_tab(name, url)

    def add_tab(self, name, url):
        widget = QWidget()
        layout = QVBoxLayout()
        webview = self.create_webview(url)

        layout.addWidget(webview)
        widget.setLayout(layout)

        self.tabs.addTab(widget, name)

    def create_webview(self, url):
        try:
            profile = QWebEngineProfile.defaultProfile()
            profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36")
            webview = QWebEngineView()
            webview.setUrl(QUrl(url))
            return webview
        except Exception as e:
            print(f"Error loading {url}: {e}")
            return None

    def reload_active_tab(self):
        current_widget = self.tabs.currentWidget()
        if current_widget:
            webview = current_widget.findChild(QWebEngineView)
            if webview:
                webview.reload()

    def go_back(self):
        current_widget = self.tabs.currentWidget()
        if current_widget:
            webview = current_widget.findChild(QWebEngineView)
            if webview and webview.history().canGoBack():
                webview.back()

    def go_forward(self):
        current_widget = self.tabs.currentWidget()
        if current_widget:
            webview = current_widget.findChild(QWebEngineView)
            if webview and webview.history().canGoForward():
                webview.forward()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TuxTalk()
    window.show()
    sys.exit(app.exec_())
