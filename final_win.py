<<<<<<< HEAD
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem

class ThirdWindow(QWidget):
    def __init__(self, result,age):
        super().__init__()
        self.result = result
        self.age = int(age)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Результаты теста Руфье')
        layout = QVBoxLayout()

        # Отображение результата
        result_label = QLabel(f'Ваш результат: {self.result:.2f}')
        layout.addWidget(result_label)

        # Определение категории результата
        category = self.determine_health_level_rufye(self.result, self.age)
        category_label = QLabel(f'Категория: {category}')
        layout.addWidget(category_label)

        # Таблица с интерпретацией результатов
        #self.create_table(layout)

        self.setLayout(layout)
        self.resize(400, 300)

    def determine_health_level_rufye(self, index, age):
        if age >= 15:
            if index >= 15:
                return "Низкий"
            elif 11 <= float(index) < 15:
                return "Удовлетворительный"
            elif 6 <= float(index) < 11:
                return "Средний"
            elif 0.5 <= float(index) < 6:
                return "Выше среднего"
            else:  # index <= 0.4
                return "Высокий"
    
        elif 13 <= age <= 14:
            if float(index) >= 14:
                return "Низкий"
            elif 10 <= float(index) < 14:
                return "Удовлетворительный"
            elif 5 <= float(index) < 10:
                return "Средний"
            elif 0.5 <= float(index) < 5:
                return "Выше среднего"
            else:  # index <= 0.4
                return "Высокий"
        
        elif 11 <= age <= 12:
            if float(index) >= 13:
                return "Низкий"
            elif 9 <= float(index) < 13:
                return "Удовлетворительный"
            elif 4 <= float(index) < 9:
                return "Средний"
            elif 0.5 <= float(index) < 4:
                return "Выше среднего"
            else:  # index <= 0.4
                return "Высокий"
        
        elif 9 <= age <= 10:
            if float(index) >= 12:
                return "Низкий"
            elif 8 <= float(index) < 12:
                return "Удовлетворительный"
            elif 3 <= float(index) < 8:
                return "Средний"
            elif 0.5 <= float(index) < 3:
                return "Выше среднего"
            else:  # index <= 0.4
                return "Высокий"
        
        elif 7 <= age <= 8:
            if float(index) >= 11:
                return "Низкий"
            elif 7 <= float(index) < 11:
                return "Удовлетворительный"
            elif 2 <= float(index) < 7:
                return "Средний"
            elif 0.5 <= float(index) < 2:
                return "Выше среднего"
            else:  # index <= 0.4
                return "Высокий"
        
        else:
            return "Возраст вне диапазона (7-15 лет)"


    '''

    def get_category(self, result):
        if result < 0:
            return "Низкий уровень физической подготовленности"
        elif 0 <= result <= 5:
            return "Средний уровень физической подготовленности"
        elif 6 <= result <= 10:
            return "Хороший уровень физической подготовленности"
        else:
            return "Высокий уровень физической подготовленности"
    
    def create_table(self, layout):
        # Создание таблицы
        table = QTableWidget()
        table.setRowCount(4)
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['Результат', 'Категория'])

        # Заполнение таблицы
        data = [
            (-float('inf'), 0, "Низкий уровень физической подготовленности"),
            (0, 5, "Средний уровень физической подготовленности"),
            (6, 10, "Хороший уровень физической подготовленности"),
            (11, float('inf'), "Высокий уровень физической подготовленности"),
        ]

        for i, (lower, upper, category) in enumerate(data):
            table.setItem(i, 0, QTableWidgetItem(f"{lower} - {upper}"))
            table.setItem(i, 1, QTableWidgetItem(category))

        layout.addWidget(table)
        '''
=======
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
>>>>>>> 9fe90bc0ae06be2d1b8740305042e99b0c812580
