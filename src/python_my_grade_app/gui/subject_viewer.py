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

        self.vertical_distribution = QVBoxLayout()
        self.box_subject = QGroupBox("Subject")
        distribution_box_subject = QGridLayout()
        self.box_subject.setLayout(distribution_box_subject)

        self.box_buttons = QGroupBox()
        distribution_box_buttons = QHBoxLayout()
        self.box_buttons.setLayout(distribution_box_buttons)

        self.vertical_distribution.addWidget(self.box_subject)
        self.vertical_distribution.addWidget(self.box_buttons)

        self.setLayout(self.vertical_distribution)

        self.show()
