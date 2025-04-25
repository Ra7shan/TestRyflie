# second_win.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ThirdWindow(QWidget):
    def __init__(self, result, age):
        super().__init__()
        self.result = result
        self.age = age
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Результаты теста')

        layout = QVBoxLayout()

        # Вывод результата
        result_label = QLabel(f'Ваш результат: {self.result:.2f}')
        
        # Определение уровня здоровья на основе результата и возраста
        health_level = self.determine_health_level_rufye(self.result, self.age)
        
        health_label = QLabel(f'Уровень здоровья: {health_level}')

        layout.addWidget(result_label)
        layout.addWidget(health_label)

        self.setLayout(layout)
        self.resize(300, 200)

    def determine_health_level_rufye(self, index, age):
        if age >= 15:
            if index >= 15:
                return "Низкий"
            elif 11 <= index < 15:
                return "Удовлетворительный"
            elif 6 <= index < 11:
                return "Средний"
            elif 0.5 <= index < 6:
                return "Выше среднего"
            else:  # index <= 0.4
                return "Высокий"

        elif 13 <= age <= 14:
            if index >= 16.5:
                return "Низкий"
            elif 12.5 <= index < 16.5:
                return "Удовлетворительный"
            elif 7.5 <= index < 12.5:
                return "Средний"
            elif 2 <= index < 7.5:
                return "Выше среднего"
            else:  # index < 1.9
                return "Высокий"

        elif 11 <= age <= 12:
            if index >= 18:
                return "Низкий"
            elif 14 <= index < 18:
                return "Удовлетворительный"
            elif 9 <= index < 14:
                return "Средний"
            elif 3.5 <= index < 9:
                return "Выше среднего"
            else:  # index < 3.4
                return "Высокий"

        elif 9 <= age <= 10:
            if index >= 19.5:
                return "Низкий"
            elif 15.5 <= index < 19.5:
                return "Удовлетворительный"
            elif 10.5 <= index < 15.5:
                return "Средний"
            elif 5 <= index < 10.5:
                return "Выше среднего"
            else: # index <4.9
                return "Высокий"

        elif age >=7 and age<9 :
            if index >=21 :
                 return"Низкий" 
                
            elif (17<=index<21):
                 return"Удовлетворительный" 
                 
            elif (12<=index<17):
                 return"Средний" 
                 
            elif (6.5<=index<12):
                 return"Выше среднего" 
                 
            else: #index<=6.4
                 return"Высокий"

        else:
            return "Возраст вне диапазона (7-15 лет)"