from math import sqrt


class CoefficientPirsona:

    def count(self, data):
        sum_x = 0
        for i in range(0, data.get_n()):
            sum_x += data.get_mass()[0][i]
        middle_x = sum_x / data.get_n()

        sum_y = 0
        for i in range(0, data.get_n()):
            sum_y += data.get_mass()[1][i]
        middle_y = sum_y / data.get_n()

        sum_up = 0
        sum_down_x = 0
        sum_down_y = 0
        for i in range(0, data.get_n()):
            sum_up += (data.get_mass()[0][i] - middle_x) * (data.get_mass()[0][i] - middle_y)
            sum_down_x += (data.get_mass()[0][i] - middle_x) ** 2
            sum_down_y += (data.get_mass()[1][i] - middle_y) ** 2
        r = sum_up / (sqrt(sum_down_x * sum_down_y))
        data.set_coefficient_pirsona(r)
