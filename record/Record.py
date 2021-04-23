from math import exp


class Record:

    def __init__(self):
        self.__string = ""

    def record(self, data, name, fi):
        self.__string += name

        self.__string += '\n|%-13c' % '№'
        for i in range(0, data.get_n()):
            self.__string += '|%-13d' % (i + 1)
        self.__string += '|\n'

        self.__string += '|%-13c' % 'X'
        for i in range(0, data.get_n()):
            self.__string += '|%-13.4f' % (data.get_mass()[0][i])
        self.__string += '|\n'

        self.__string += '|%-13c' % 'Y'
        for i in range(0, data.get_n()):
            self.__string += '|%-13.4f' % (data.get_mass()[1][i])
        self.__string += '|\n'

        self.__string += '|%-13s' % fi
        for i in range(0, data.get_n()):
            self.__string += '|%-13.4f' % (data.get_f()[i])
        self.__string += '|\n'

        self.__string += '|%-13s' % 'Eps'
        for i in range(0, data.get_n()):
            self.__string += '|%-13.4f' % (data.get_e()[i])
        self.__string += '|\n'

        if name == "ЛИНЕЙНАЯ ФУНКЦИЯ":
            number = data.get_line_a()
            self.__string += 'A = {}\n'.format(number)
            number = data.get_line_b()
            self.__string += 'B = {}\n'.format(number)
            number = data.get_coefficient_pirsona()
            self.__string += 'Коэффициент корреляции Пирсона = {}\n'.format(number)
            if abs(number) < 0.3:
                self.__string += "Связь слабая\n"
            elif 0.3 <= abs(number) < 0.5:
                self.__string += "Связь умеренная\n"
            elif 0.5 <= abs(number) < 0.7:
                self.__string += "Связь заметная\n"
            elif 0.7 <= abs(number) < 0.9:
                self.__string += "Связь высокая\n"
            elif 0.9 <= abs(number) < 0.99:
                self.__string += "Связь весьма высокая\n"
            elif abs(number) == 1:
                self.__string += "Строгая линейная функциональная зависимость\n"
        elif name == "ПОЛИНОМИАЛЬНАЯ ФУНКЦИЯ":
            number = data.get_square_a()
            self.__string += 'A = {}\n'.format(number)
            number = data.get_square_b()
            self.__string += 'B = {}\n'.format(number)
            number = data.get_square_c()
            self.__string += 'C = {}\n'.format(number)
        elif name == "ЭКСПОНЕНЦИАЛЬНАЯ ФУНКЦИЯ":
            number = exp(data.get_line_a())
            self.__string += 'A = {}\n'.format(number)
            number = data.get_line_b()
            self.__string += 'B = {}\n'.format(number)
        elif name == "ЛОГАРИФМИЧЕСКАЯ ФУНКЦИЯ":
            number = data.get_line_a()
            self.__string += 'A = {}\n'.format(number)
            number = data.get_line_b()
            self.__string += 'B = {}\n'.format(number)
        elif name == "СТЕПЕННАЯ ФУНКЦИЯ":
            number = exp(data.get_line_a())
            self.__string += 'A = {}\n'.format(number)
            number = data.get_line_b()
            self.__string += 'B = {}\n'.format(number)

        self.__string += 'Мера отклонения = {}\n'.format(data.get_devition())
        self.__string += 'Среднеквадратичное отклонение = {}\n'.format(data.get_standart_devition())
        self.__string += 'Достоверность аппроксимации = {}\n'.format(data.get_accuracy())
        self.__string += '---------------------------------------------------------------------------------------------\n'

    def output(self, file_or_console, index):
        if file_or_console == "console":
            print(self.__string)
            print("Наилучшая аппроксимирующая функция №",index)
        else:
            print(1)#TODO