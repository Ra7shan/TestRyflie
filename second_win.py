<<<<<<< HEAD
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

        self.name_label = QLabel('Введите Ф.И.О.:')
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.age_label = QLabel('Полных лет:')
        self.age_input = QLineEdit(self)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        
        # Поле для давления
        self.pressure_label = QLabel('Лягте на спину и замерьте пульс за 15 секунд.')
        self.pressure_label.setAlignment(Qt.AlignLeft)  # Выравнивание вправо
        layout.addWidget(self.pressure_label)
        
        # Второе поле
        self.start_second_test_button = QPushButton('Замерить первый тест (15 секунд)')
        self.start_second_test_button.clicked.connect(self.start_second_test)
        layout.addWidget(self.start_second_test_button)        
        
        self.input_first = QLineEdit(self)
        layout.addWidget(self.input_first)        
        
        self.age_label = QLabel('Выполните 10 приседаний за 15 секунд.')
        self.input_second = QLineEdit(self)
        layout.addWidget(self.age_label)
        layout.addWidget(self.input_second)
        
        # Первое поле
        self.first_test_button = QPushButton('Начать приседания (15 секунд)')
        self.first_test_button.clicked.connect(self.start_first_test)
        layout.addWidget(self.first_test_button)
        
        self.pressure_label = QLabel('Лягте на спину и замерьте давление за первые 15 секунд и за последние 15 секунд.')
        self.pressure_label.setAlignment(Qt.AlignRight)  # Выравнивание вправо
        layout.addWidget(self.pressure_label)
        
        self.input_third = QLineEdit(self)
        layout.addWidget(self.input_third)        
        
        self.first_pressure_button = QPushButton('Запустить таймер на 15 секунд')
        self.first_pressure_button.clicked.connect(self.start_pressure_timer)
        layout.addWidget(self.first_pressure_button)        
        
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

    '''
    def calculate_result(self):
        try:
            age = float(self.age_input.text())
            # Другие вычисления
            self.openThirdWindow()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите правильные числа.")
'''
    def calculate_result(self):
         try:
             age = float(self.age_input.text())
             p1 = float(self.input_first.text())
             p2 = float(self.input_second.text())
             p3 = float(self.input_third.text())
             

             #print("age",age)
             #print(p1,p2,p3)
             index_rufye = (4 * (p1 + p2 + p3) - 200) / 10

             '''
             QMessageBox.information(
                 self,
                 "Индекс Руфье",
                 f"Индекс Руфье: {index_rufye:.2f}"
             )
             '''
             # Открытие третьего окна с результатом (если нужно передать данные)
             self.openThirdWindow(index_rufye, age) 

         except ValueError:
             QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите правильные числа.")
    
    def openThirdWindow(self, index, age):
        self.third_window = ThirdWindow(index, age)
        self.third_window.show()
=======
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

        self.name_label = QLabel('Введите Ф.И.О.:')
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.age_label = QLabel('Полных лет:')
        self.age_input = QLineEdit(self)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        
        # Поле для давления
        self.pressure_label = QLabel('Лягте на спину и замерьте пульс за 15 секунд.')
        self.pressure_label.setAlignment(Qt.AlignLeft)  # Выравнивание вправо
        layout.addWidget(self.pressure_label)
        
        # Второе поле
        self.start_second_test_button = QPushButton('Замерить первый тест (15 секунд)')
        self.start_second_test_button.clicked.connect(self.start_second_test)
        layout.addWidget(self.start_second_test_button)        
        
        self.pressure_input_first = QLineEdit(self)
        layout.addWidget(self.pressure_input_first)        
        
        self.age_label = QLabel('Выполните 10 приседаний за 15 секунд.')
        self.age_input = QLineEdit(self)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        
        # Первое поле
        self.first_test_button = QPushButton('Начать приседания (15 секунд)')
        self.first_test_button.clicked.connect(self.start_first_test)
        layout.addWidget(self.first_test_button)
        
        self.pressure_label = QLabel('Лягте на спину и замерьте давление за первые 15 секунд и за последние 15 секунд.')
        self.pressure_label.setAlignment(Qt.AlignRight)  # Выравнивание вправо
        layout.addWidget(self.pressure_label)
        
        self.pressure_input_first = QLineEdit(self)
        layout.addWidget(self.pressure_input_first)        
        
        self.first_pressure_button = QPushButton('Запустить таймер на 15 секунд')
        self.first_pressure_button.clicked.connect(self.start_pressure_timer)
        layout.addWidget(self.first_pressure_button)        
        
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
>>>>>>> 9fe90bc0ae06be2d1b8740305042e99b0c812580
        self.close()