from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from second_win import SecondWindow

class HealthApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Программа по определению состояния здоровья')

        layout = QVBoxLayout()

        welcome_label = QLabel('Добро пожаловать в программу\nпо определению состояния\nздоровья!')
        welcome_label.setAlignment(Qt.AlignLeft)

        info_label = QLabel(
            'Данное приложение позволит вам с помощью теста Руфье\n'
            'провести первичную диагностику вашего здоровья. Важно!\n'
            'Если в процессе проведения испытания вы почувствуете себя плохо,\n'
            'то тест необходимо прервать и обратиться к врачу.'
        )
        info_label.setAlignment(Qt.AlignLeft)

        self.start_button = QPushButton('Начать')
        self.start_button.clicked.connect(self.openSecondWindow)

        layout.addWidget(welcome_label)
        layout.addWidget(info_label)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.resize(600, 400)

    def openSecondWindow(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()