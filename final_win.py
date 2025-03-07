# final_win.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ThirdWindow(QWidget):
    def __init__(self, result):
        super().__init__()
        self.initUI(result)

    def initUI(self, result):
        self.setWindowTitle('Результаты')

        layout = QVBoxLayout()

        if result < 66:
            message = 'Обратитесь к врачу!'
        else:
            message = 'С вами все хорошо!'

        result_label = QLabel(message)
        layout.addWidget(result_label)

        self.setLayout(layout)
        self.resize(300, 200)