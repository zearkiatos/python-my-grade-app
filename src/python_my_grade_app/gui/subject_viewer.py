from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout


class Gui_Application(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'My Application'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        self.initialize_gui()

    def initialize_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
