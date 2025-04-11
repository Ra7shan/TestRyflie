# my_app.py
import sys
from PyQt5.QtWidgets import QApplication
from instr import HealthApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    health_app = HealthApp()
    health_app.show()
    sys.exit(app.exec_())