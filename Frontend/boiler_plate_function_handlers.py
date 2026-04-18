from PyQt5.QtWidgets import QMessageBox

def yes_no_popup(text):
    reply = QMessageBox.question(
        None,
        "Confirm Action",
        text,
        QMessageBox.Yes | QMessageBox.No
    )
    return reply