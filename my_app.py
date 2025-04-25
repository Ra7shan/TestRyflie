<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication
from instr import HealthApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    health_app = HealthApp()
    health_app.show()
=======
# my_app.py
import sys
from PyQt5.QtWidgets import QApplication
from instr import HealthApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    health_app = HealthApp()
    health_app.show()
>>>>>>> 9fe90bc0ae06be2d1b8740305042e99b0c812580
    sys.exit(app.exec_())