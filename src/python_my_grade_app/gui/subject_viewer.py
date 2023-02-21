from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout


class Gui_Application(QWidget):
    def __init__(self, logic):
        super().__init__()

        self.title = 'My Application'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        self.initialize_gui()
        self.logic = logic
        self.update_subject()

    def update_subject(self):
        current = self.logic.get_current_subject()
        self.text_name.setText(current["name"])
        self.text_semestry.setText(current["semestry"])
        self.text_professor.setText(current["professor"])
        self.text_grade.setText(str(current["grade"]))
    
    def advance_subject(self):
        self.logic.advance()
        self.update_subject()
    
    def back_subject(self):
        self.logic.back()
        self.update_subject()

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

        self.tag_grade = QLabel('Grade')
        self.text_grade = QLineEdit()

        distribution_box_subject.addWidget(self.tag_name, 0,0)
        distribution_box_subject.addWidget(self.tag_semestry, 1,0)
        distribution_box_subject.addWidget(self.tag_professor, 2,0)
        distribution_box_subject.addWidget(self.tag_grade, 3,0)

        distribution_box_subject.addWidget(self.text_name, 0,1)
        distribution_box_subject.addWidget(self.text_semestry, 1,1)
        distribution_box_subject.addWidget(self.text_professor, 2,1)
        distribution_box_subject.addWidget(self.text_grade, 3,1)


        self.box_buttons = QGroupBox()
        distribution_box_buttons = QHBoxLayout()
        self.box_buttons.setFixedHeight(50)
        self.box_buttons.setLayout(distribution_box_buttons)

        self.back_button = QPushButton("⬅️")
        self.back_button.clicked.connect(self.back_subject)
        self.advance_button = QPushButton("➡️")
        self.advance_button.clicked.connect(self.advance_subject)

        distribution_box_buttons.addWidget(self.back_button)
        distribution_box_buttons.addWidget(self.advance_button)

        self.vertical_distribution.addWidget(self.box_subject)
        self.vertical_distribution.addWidget(self.box_buttons)

        self.setLayout(self.vertical_distribution)

        self.show()
