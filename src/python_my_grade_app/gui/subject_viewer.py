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

        self.tag_name = QLabel('Name')
        self.text_name = QLineEdit()

        self.tag_semestry = QLabel('Semestry')
        self.text_semestry = QLineEdit()

        self.tag_professor = QLabel('Professor')
        self.text_professor = QLineEdit()

        self.tag_note = QLabel('Note')
        self.text_note = QLineEdit()

        distribution_box_subject.addWidget(self.tag_name, 0,0)
        distribution_box_subject.addWidget(self.tag_semestry, 1,0)
        distribution_box_subject.addWidget(self.tag_professor, 2,0)
        distribution_box_subject.addWidget(self.tag_note, 3,0)

        distribution_box_subject.addWidget(self.text_name, 0,1)
        distribution_box_subject.addWidget(self.text_semestry, 1,1)
        distribution_box_subject.addWidget(self.text_professor, 2,1)
        distribution_box_subject.addWidget(self.text_note, 3,1)


        self.box_buttons = QGroupBox()
        distribution_box_buttons = QHBoxLayout()
        self.box_buttons.setLayout(distribution_box_buttons)

        self.back_button = QPushButton("⬅️")
        self.advance_button = QPushButton("➡️")

        distribution_box_buttons.addWidget(self.back_button)
        distribution_box_buttons.addWidget(self.advance_button)

        self.vertical_distribution.addWidget(self.box_subject)
        self.vertical_distribution.addWidget(self.box_buttons)

        self.setLayout(self.vertical_distribution)

        self.show()
