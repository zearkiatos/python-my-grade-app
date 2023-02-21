from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QDialogButtonBox, QGroupBox, QGridLayout, QLabel, QLineEdit, QComboBox, QMessageBox


class New_subject_dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(New_subject_dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Add new subject")

        self.distribute = QVBoxLayout()

        Q_Buttons = QDialogButtonBox.Save | QDialogButtonBox.Cancel
        self.box_buttons = QDialogButtonBox(Q_Buttons)

        self.box_buttons.accepted.connect(self.accept)
        self.box_buttons.rejected.connect(self.reject)

        self.dialog_initialize()

        self.distribute.addWidget(self.box_buttons)

        self.setLayout(self.distribute)

    def dialog_initialize(self):
        box_fields = QGroupBox("Add the data")
        distribution_fields = QGridLayout()

        self.tag_name = QLabel("Name")
        self.text_name = QLineEdit()
        self.tag_semestry = QLabel("Semestry")
        self.text_semestry = QComboBox()
        self.text_semestry.addItems(["2019-1","2019-2","2020-1"])
        self.tag_professor = QLabel("Professor")
        self.text_professor = QLineEdit()
        self.tag_grade = QLabel("Grade")
        self.text_grade = QLineEdit()

        distribution_fields.addWidget(self.tag_name, 0, 0)
        distribution_fields.addWidget(self.text_name, 0, 1)
        distribution_fields.addWidget(self.tag_semestry, 1, 0)
        distribution_fields.addWidget(self.text_semestry, 1, 1)
        distribution_fields.addWidget(self.tag_professor, 2, 0)
        distribution_fields.addWidget(self.text_professor, 2, 1)
        distribution_fields.addWidget(self.tag_grade, 3, 0)
        distribution_fields.addWidget(self.text_grade, 3, 1)

        box_fields.setLayout(distribution_fields)
        self.distribute.addWidget(box_fields)

    
    def get_values(self):
        return {
            "name": self.text_name.text(),
            "semestry": self.text_semestry.currentText(),
            "professor": self.text_professor.text(),
            "grade": float(self.text_grade.text())
        }
    
    def accept(self):
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setText("Are you sure that you want to save the data as a new subject?")
        confirm_dialog.setWindowTitle('Confirm')
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if self.value_verified() and confirm_dialog.exec_() == QMessageBox.Yes:
            super().accept()
        else:
            super().reject()
    
    def value_verified(self):
        if self.text_name.text() == "" or self.text_professor.text() == "" or self.text_grade.text() == "":
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("The new subject fields cannot be empty")
            error_dialog.setWindowTitle("Error")
            error_dialog.setStandardButtons(QMessageBox.Ok)
            error_dialog.exec_()
            return False
        return True
