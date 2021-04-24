import matplotlib.pyplot as plt
import numpy as np


class DrawGraph:
    def __init__(self, data):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        rect = ax.patch
        rect.set_facecolor('lightslategray')
        rect.set_alpha(0.25)
        plt.plot(data.get_mass()[0], data.get_mass()[1], 'o', alpha=0.7, lw=0, mec='b', mew=2, ms=3)
        ax.grid(True, which=u'major', color='w', linewidth=2., linestyle='solid')
        ax.grid(True, which=u'minor', color='b')

    def drawLine(self, data, equation):
        x = np.arange(min(data.get_mass()[0]) - 2, max(data.get_mass()[0]) + 2, 0.01)
        np.seterr(divide='ignore')
        if equation == 1:
            number = data.get_line_a() * x + data.get_line_b()
        elif equation == 2:
            number = x * x * data.get_square_a() + data.get_square_b() * x + data.get_square_c()
        elif equation == 3:
            number = np.exp(data.get_exp_b()) * np.exp(data.get_exp_a() * x)
        elif equation == 4:
            number = data.get_log_a() * np.log1p(x) + data.get_log_b()
        elif equation == 5:
            number = np.exp(data.get_pow_b()) * pow(x, data.get_pow_a())
        plt.plot(x, number)

    def draw_show(self):
        plt.legend(['points', 'Fi=ax+b', 'Fi=ax^2+bx+c', 'Fi=ae^bx', 'Fi=a*ln(x)+b', 'Fi=ax^b'])
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.show()
