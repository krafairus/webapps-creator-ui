#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl

class SimpleBrowser(QWidget):
    def __init__(self, url, icon_path=None):
        super().__init__()
        self.url = url
        self.icon_path = icon_path
        self.initUI()
        self.load_start_url()

    def initUI(self):
        layout = QVBoxLayout()

        self.browser = QWebEngineView()

        # If custom icon is provided, set it; else, icon will be updated upon webpage load
        if self.icon_path:
            self.setWindowIcon(QIcon(self.icon_path))
        else:
            self.browser.iconChanged.connect(self.update_window_icon)

        self.btnInicio = QPushButton('Inicio', self)
        self.btnInicio.clicked.connect(self.load_start_url)

        layout.addWidget(self.browser)
        layout.addWidget(self.btnInicio)

        self.setLayout(layout)

        self.browser.titleChanged.connect(self.update_window_title)

        self.setWindowTitle('WebApp Browser')
        self.setGeometry(300, 300, 800, 600)

    def load_start_url(self):
        self.browser.setUrl(QUrl(self.url))

    def update_window_title(self, title):
        self.setWindowTitle(title)

    def update_window_icon(self, icon):
        self.setWindowIcon(icon)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = 'https://www.example.com/'

    icon_path = sys.argv[2] if len(sys.argv) > 2 else None

    window = SimpleBrowser(url, icon_path)
    window.show()

    sys.exit(app.exec_())

