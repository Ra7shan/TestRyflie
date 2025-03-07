from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt, QTimer
from final_win import ThirdWindow

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ввод данных для теста')

        layout = QVBoxLayout()

        # Название
        self.title_label = QLabel('Введите данные для теста')
        self.title_label.setAlignment(Qt.AlignRight)  # Выравнивание вправо
        layout.addWidget(self.title_label)

        self.name_label = QLabel('Введите Ф.И.О.:')
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Второе поле
        self.start_second_test_button = QPushButton('Начать второй тест (15 секунд)')
        self.start_second_test_button.clicked.connect(self.start_second_test)
        layout.addWidget(self.start_second_test_button)

        self.age_label = QLabel('Полных лет:')
        self.age_input = QLineEdit(self)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        
        # Первое поле
        self.first_test_button = QPushButton('Начать первый тест (15 секунд)')
        self.first_test_button.clicked.connect(self.start_first_test)
        layout.addWidget(self.first_test_button)
        
        # Поле для давления
        self.pressure_label = QLabel('Лягте на спину и замерьте давление за первые 15 секунд и за последние 15 секунд.')
        self.pressure_label.setAlignment(Qt.AlignRight)  # Выравнивание вправо
        layout.addWidget(self.pressure_label)

        self.first_pressure_button = QPushButton('Запустить таймер на 15 секунд')
        self.first_pressure_button.clicked.connect(self.start_pressure_timer)
        layout.addWidget(self.first_pressure_button)

        self.last_pressure_button = QPushButton('Запустить таймер на 15 секунд')
        self.last_pressure_button.clicked.connect(self.start_pressure_timer)
        layout.addWidget(self.last_pressure_button)

        self.pressure_input_first = QLineEdit(self)
        layout.addWidget(self.pressure_input_first)

        self.pressure_input_second = QLineEdit(self)
        layout.addWidget(self.pressure_input_second)

        self.final_test_button = QPushButton('Начать финальный тест')
        self.final_test_button.clicked.connect(self.calculate_result)
        layout.addWidget(self.final_test_button)

        # Вспомогательный горизонтальный layout для таймера
        timer_layout = QHBoxLayout()
        
        # Метка для отображения таймера
        self.timer_label = QLabel('Оставшееся время: 0 секунд')
        self.timer_label.setStyleSheet("font-weight: bold;")  # Жирный текст
        timer_layout.addWidget(self.timer_label, alignment=Qt.AlignRight)  # Выровнять вправо
        
        layout.addLayout(timer_layout)
        self.setLayout(layout)
        self.resize(400, 300)

        # Таймер
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Переменная для хранения оставшегося времени
        self.remaining_time = 0

    def start_first_test(self):
        self.start_timer(15)  # 15 секунд

    def start_second_test(self):
        self.start_timer(15)  # 15 секунд

    def start_pressure_timer(self):
        self.start_timer(15)  # 15 секунд

    def start_timer(self, seconds):
        self.remaining_time = seconds
        self.timer_label.setText(f'Оставшееся время: {self.remaining_time} секунд')
        self.timer.start(1000)  # обновление каждую секунду
        print(f"Таймер запущен на {seconds} секунд.")

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.setText(f'Оставшееся время: {self.remaining_time} секунд')
        else:
            self.timer.stop()
            self.timer_label.setText('Таймер завершен.')
            print("Таймер завершен.")

    def calculate_result(self):
        try:
            age = float(self.age_input.text())
            # Другие вычисления
            self.openThirdWindow()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите правильные числа.")

    def openThirdWindow(self):
        self.third_window = ThirdWindow(75)
        self.third_window.show()
        self.close()