from boiler_plate_function_handlers import yes_no_popup

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QAction,
    QMessageBox,
    QFileDialog,
    QGridLayout,
    QLabel,
    QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Astrophotography App")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setFixedSize(800, 200)

        self.camera_label = QLabel("Camera connected")
        self.camera_connect_label = QLabel()
        self.camera_connect_label.setStyleSheet("background-color: red;")

        self.layout.addWidget(self.camera_label, 0, 0)
        self.layout.addWidget(self.camera_connect_label, 0, 1)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()