import numpy as np


class DecisionMatrix:

    def decision(self, data):
        # Линейная функция
        a = np.array([[data.get_s_xx(), data.get_s_x()],
                      [data.get_s_x(), data.get_n()]])
        b = np.array([data.get_s_xy(), data.get_s_y()])
        result = np.linalg.solve(a, b)
        data.set_line_a(result[0])
        data.set_line_b(result[1])
        # Экспоненциальную функцию
        a = np.array([[data.get_s_xx(), data.get_s_x()],
                      [data.get_s_x(), data.get_n()]])
        b = np.array([data.get_s_x_ln_y(), data.get_s_ln_y()])
        result = np.linalg.solve(a, b)
        data.set_exp_a(result[0])
        data.set_exp_b(result[1])
        # Логарифмическую функцию
        a = np.array([[data.get_s_ln_xx(), data.get_s_ln_x()],
                      [data.get_s_ln_x(), data.get_n()]])
        b = np.array([data.get_s_y_ln_x(), data.get_s_y()])
        result = np.linalg.solve(a, b)
        data.set_log_a(result[0])
        data.set_log_b(result[1])
        # Степенную функцию
        a = np.array([[data.get_s_ln_xx(), data.get_s_ln_x()],
                      [data.get_s_ln_x(), data.get_n()]])
        b = np.array([data.get_s_ln_xy(), data.get_s_ln_y()])
        result = np.linalg.solve(a, b)
        data.set_pow_a(result[0])
        data.set_pow_b(result[1])
        # Полиномиальную функцию 2-й степени
        a = np.array([[data.get_n(), data.get_s_x(), data.get_s_xx()],
                      [data.get_s_x(), data.get_s_xx(), data.get_s_xxx()],
                      [data.get_s_xx(), data.get_s_xxx(), data.get_s_xxxx()]])
        b = np.array([data.get_s_y(), data.get_s_xy(), data.get_s_xxy()])
        result = np.linalg.solve(a, b)
        data.set_square_a(result[2])
        data.set_square_b(result[1])
        data.set_square_c(result[0])
