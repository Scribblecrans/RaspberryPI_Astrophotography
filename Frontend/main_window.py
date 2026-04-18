from boiler_plate_function_handlers import yes_no_popup

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QWidget,
    QAction,
    QMessageBox,
    QSplashScreen,
    QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_action = True
        self.image_saved = None
        self.setWindowTitle("AstroMod")
        self.resize(1200, 1600)

        menu_bar = self.menuBar()
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu("File")

    
        open_project_action = QAction("Open Project", self)
        save_action = QAction("Save Project", self)
        save_as_action = QAction("Save As...", self)
        exit_action = QAction("Exit AstroMod", self)
        exit_action.setMenuRole(QAction.NoRole)

        open_project_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        save_as_action.triggered.connect(self.save_file_as)
        exit_action.triggered.connect(self.exit_application)

        file_menu.addActions([open_project_action, 
                              save_action, 
                              save_as_action,
                              exit_action])

        self.closeEvent = lambda event: self.exit_application(event)

    def open_file(self):
        print("working")

    def save_file(self):
        print("works")

    def save_file_as(self):
        print("workininaign")

    def exit_application(self, event=None):
        if self.active_action == True:
            proceed_exit = yes_no_popup("Are you sure you want to exit? You are currently in the middle of a process.")
        elif self.image_saved == False:
            proceed_exit = yes_no_popup("Are you sure you want to exit? You have not saved your processed images")

        else: proceed_exit = QMessageBox.Yes

        if proceed_exit == QMessageBox.Yes: self.close()

def main():
    app = QApplication([])
    screen = app.primaryScreen().availableGeometry()
    loading_screen = QPixmap("/Users/evansumner/Projects/RaspberryPi Astrophotography/Frontend/AstroMod.png")
    loading_screen = loading_screen.scaled(
    int(screen.width() * 0.5),
    int(screen.height() * 0.5),
    Qt.KeepAspectRatio,
    Qt.SmoothTransformation
    )
    splash = QSplashScreen(loading_screen)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.show()
    app.processEvents()

    window = MainWindow()

    splash.finish(window)
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()