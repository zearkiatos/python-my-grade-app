import sys
from logic.subject_organizer import subject_organizer
from gui.subject_viewer import Gui_Application
from PyQt5.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.logic = subject_organizer()
        self.gui = Gui_Application(self.logic)


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
