import numpy as np


class DecisionMatrix:

    def decision(self, data):
        a = np.array([[data.get_s_xx(), data.get_s_x()],
                      [data.get_s_x(), data.get_n()]])
        b = np.array([data.get_s_xy(), data.get_s_y()])
        result = np.linalg.solve(a, b)
        data.set_line_a(result[0])
        data.set_line_b(result[1])
        a = np.array([[data.get_n(), data.get_s_x(), data.get_s_xx()],
                      [data.get_s_x(), data.get_s_xx(), data.get_s_xxx()],
                      [data.get_s_xx(), data.get_s_xxx(), data.get_s_xxxx()]])
        b = np.array([data.get_s_y(), data.get_s_xy(), data.get_s_xxy()])
        result = np.linalg.solve(a, b)
        data.set_square_a(result[2])
        data.set_square_b(result[1])
        data.set_square_c(result[0])
