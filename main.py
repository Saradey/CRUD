import sys
from PyQt5.QtWidgets import QApplication
from  Widget.MainWidget import MainWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainWidget()
    md.show()
    sys.exit(app.exec_())