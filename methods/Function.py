from math import *
from record.Record import Record
from draw.DrawGraph import DrawGraph


class Function:

    def function(self, data):
        index = 0
        max = 0
        draw = DrawGraph(data)
        # Линейная функция
        self.public(data, 1)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 1
        Record().record(data)
        draw.drawLine(data)
        # Полиномиальную функцию 2-й степени
        self.public(data, 2)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 2
        Record().record(data)
        draw.drawLine(data)
        # Экспоненциальную функцию
        self.public(data, 3)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 3
        Record().record(data)
        draw.drawLine(data)
        # Логарифмическую функцию
        self.public(data, 4)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 4
        Record().record(data)
        draw.drawLine(data)
        # Степенную функцию
        self.public(data, 5)
        if data.get_accuracy() > max:
            max = data.get_accuracy()
            index = 5
        Record().record(data)
        draw.drawLine(data)

    def public(self, data, equation):
        mass = []
        for i in range(0, data.get_n()):
            if equation == 1:
                number = data.get_line_a() * data.get_mass()[0][i] + data.get_line_b()
            elif equation == 2:
                number = data.get_mass()[0][i] * data.get_mass()[0][i] * data.get_square_a() + data.get_square_b() * \
                         data.get_mass()[0][i] + data.get_square_c()
            elif equation == 3:
                number = exp(data.get_line_a()) * exp(data.get_line_b() * data.get_mass()[0][i])
            elif equation == 4:
                number = data.get_line_a() * log(data.get_mass()[0][i], e) + data.get_line_b
            elif equation == 5:
                number = exp(data.get_line_a()) * pow(data.get_mass[0][i], data.get_line_b())
            mass.insert(i, number)
        data.set_f(mass)
        for i in range(0, data.get_n):
            number = data.get_mass()[1][i] - data.get_f()[i]
            mass.insert(i, number)
        data.set_e(mass)
        sum = 0
        for i in range(0, data.get_n()):
            sum += (data.get_e()[i]) ** 2
        data.set_devition(sum)
        sum = 0
        for i in range(0, data.get_n):
            sum += (data.get_f()[i] - data.get_mass()[1][i]) ** 2
        data.set_standart_devition(sqrt(sum / data.get_n()))
        sum_up = 0
        sum_down_left = 0
        sum_down_right = 0
        for i in range(0, data.get_n()):
            sum_up += (data.get_mass[1][i] - data.get_f()[i]) ** 2
            sum_down_left += (data.get_f()[i]) ** 2
            sum_down_right += data.get_f()[i]
        r = 1 - (sum_up / (sum_down_left - (sum_down_right / data.get_n())))
        data.set_accuracy(r)
