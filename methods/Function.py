from math import *
from record.Record import Record
from draw.DrawGraph import DrawGraph


class Function:

    def function(self, data):
        index = 0
        max = 0
        draw = DrawGraph(data)
        recorded = Record()
        # Линейная функция
        self.public(data, 1)
        recorded.record(data, "ЛИНЕЙНАЯ ФУНКЦИЯ", "Fi=ax+b")
        draw.drawLine(data)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 1
        # Полиномиальную функцию 2-й степени
        self.public(data, 2)
        recorded.record(data, "ПОЛИНОМИАЛЬНАЯ ФУНКЦИЯ", "Fi=ax^2+bx+c")
        draw.drawLine(data)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 2
        # Экспоненциальную функцию
        self.public(data, 3)
        recorded.record(data, "ЭКСПОНЕНЦИАЛЬНАЯ ФУНКЦИЯ", "Fi=ae^bx")
        draw.drawLine(data)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 3
        # Логарифмическую функцию
        self.public(data, 4)
        recorded.record(data, "ЛОГАРИФМИЧЕСКАЯ ФУНКЦИЯ", "Fi=a*ln(x)+b")
        draw.drawLine(data)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 4
        # Степенную функцию
        self.public(data, 5)
        recorded.record(data, "СТЕПЕННАЯ ФУНКЦИЯ", "Fi=ax^b")
        draw.drawLine(data)
        if data.get_accuracy() > max:
            index = 5
        recorded.output(data.get_file_or_console(), index)

    def public(self, data, equation):

        mass = []
        for i in range(0, data.get_n()):
            if equation == 1:
                number = data.get_line_a() * data.get_mass()[0][i] + data.get_line_b()
            elif equation == 2:
                number = data.get_mass()[0][i] * data.get_mass()[0][i] * data.get_square_a() + data.get_square_b() * \
                         data.get_mass()[0][i] + data.get_square_c()
            elif equation == 3:
                number = exp(data.get_exp_b()) * exp(data.get_exp_a() * data.get_mass()[0][i])
            elif equation == 4:
                number = data.get_log_a() * log(data.get_mass()[0][i], e) + data.get_log_b()
            elif equation == 5:
                number = exp(data.get_pow_b()) * pow(data.get_mass()[0][i], data.get_pow_a())
            mass.insert(i, number)
        data.set_f(mass)

        mass = []
        for i in range(0, data.get_n()):
            number = data.get_f()[i] - data.get_mass()[1][i]
            mass.insert(i, number)
        data.set_e(mass)

        sum = 0
        for i in range(0, data.get_n()):
            sum += (data.get_e()[i]) ** 2
        data.set_devition(sum)

        sum = 0
        for i in range(0, data.get_n()):
            sum += (data.get_f()[i] - data.get_mass()[1][i]) ** 2
        data.set_standart_devition(sqrt(sum / data.get_n()))

        sum_up = 0
        sum_down_left = 0
        sum_down_right = 0
        for i in range(0, data.get_n()):
            sum_up += (data.get_mass()[1][i] - data.get_f()[i]) ** 2
            sum_down_left += (data.get_f()[i]) ** 2
            sum_down_right += data.get_f()[i]
        r = 1 - (sum_up / (sum_down_left - (sum_down_right ** 2 / data.get_n())))
        data.set_accuracy(r)
