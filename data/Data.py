class Data:
    def __init__(self):
        self.__coefficient_pirsona = None
        self.__s_x = None
        self.__s_xx = None
        self.__s_xxx = None
        self.__s_xxxx = None
        self.__s_y = None
        self.__s_xy = None
        self.__s_xxy = None
        self.__s_ln_x = None
        self.__s_ln_xx = None
        self.__s_ln_y = None
        self.__s_ln_xy = None
        self.__s_x_ln_y = None
        self.__s_y_ln_x = None
        self.__n = None
        self.__mass = [[], []]
        self.__f = []
        self.__e = []
        self.__file_or_console = None
        self.__line_a = None
        self.__line_b = None
        self.__pow_a = None
        self.__pow_b = None
        self.__exp_a = None
        self.__exp_b = None
        self.__log_a = None
        self.__log_b = None
        self.__square_a = None
        self.__square_b = None
        self.__square_c = None

        self.__devition = None
        self.__standart_devition = None
        self.__accuracy = None

    def get_coefficient_pirsona(self):
        return self.__coefficient_pirsona

    def get_s_x(self):
        return self.__s_x

    def get_s_xx(self):
        return self.__s_xx

    def get_s_xxx(self):
        return self.__s_xxx

    def get_s_xxxx(self):
        return self.__s_xxxx

    def get_s_y(self):
        return self.__s_y

    def get_s_xy(self):
        return self.__s_xy

    def get_s_xxy(self):
        return self.__s_xxy

    def get_n(self):
        return self.__n

    def get_mass(self):
        return self.__mass

    def get_file_or_console(self):
        return self.__file_or_console

    def get_s_x_ln_y(self):
        return self.__s_x_ln_y

    def get_s_y_ln_x(self):
        return self.__s_y_ln_x

    def get_line_a(self):
        return self.__line_a

    def get_line_b(self):
        return self.__line_b

    def get_pow_a(self):
        return self.__pow_a

    def get_pow_b(self):
        return self.__pow_b

    def get_exp_a(self):
        return self.__exp_a

    def get_exp_b(self):
        return self.__exp_b

    def get_log_a(self):
        return self.__log_a

    def get_log_b(self):
        return self.__log_b

    def get_square_a(self):
        return self.__square_a

    def get_square_b(self):
        return self.__square_b

    def get_square_c(self):
        return self.__square_c

    def get_devition(self):
        return self.__devition

    def get_standart_devition(self):
        return self.__standart_devition

    def get_accuracy(self):
        return self.__accuracy

    def get_f(self):
        return self.__f

    def get_e(self):
        return self.__e

    def get_s_ln_x(self):
        return self.__s_ln_x

    def get_s_ln_xx(self):
        return self.__s_ln_xx

    def get_s_ln_y(self):
        return self.__s_ln_y

    def get_s_ln_xy(self):
        return self.__s_ln_xy

    def set_coefficient_pirsona(self, coefficient_pirsona):
        self.__coefficient_pirsona = coefficient_pirsona

    def set_s_x(self, s_x):
        self.__s_x = s_x

    def set_s_xx(self, s_xx):
        self.__s_xx = s_xx

    def set_s_xxx(self, s_xxx):
        self.__s_xxx = s_xxx

    def set_s_xxxx(self, s_xxxx):
        self.__s_xxxx = s_xxxx

    def set_s_y(self, s_y):
        self.__s_y = s_y

    def set_s_xy(self, s_xy):
        self.__s_xy = s_xy

    def set_s_xxy(self, s_xxy):
        self.__s_xxy = s_xxy

    def set_n(self, n):
        self.__n = n

    def set_element_mass(self, number, i, j):
        self.__mass[i].insert(j, number)

    def set_file_or_console(self, file_or_console):
        self.__file_or_console = file_or_console

    def set_line_a(self, line_a):
        self.__line_a = line_a

    def set_line_b(self, line_b):
        self.__line_b = line_b

    def set_pow_a(self, pow_a):
        self.__pow_a = pow_a

    def set_pow_b(self, pow_b):
        self.__pow_b = pow_b

    def set_exp_a(self, exp_a):
        self.__exp_a = exp_a

    def set_exp_b(self, exp_b):
        self.__exp_b = exp_b

    def set_log_a(self, log_a):
        self.__log_a = log_a

    def set_log_b(self, log_b):
        self.__log_b = log_b

    def set_square_a(self, square_a):
        self.__square_a = square_a

    def set_square_b(self, square_b):
        self.__square_b = square_b

    def set_square_c(self, square_c):
        self.__square_c = square_c

    def set_devition(self, devition):
        self.__devition = devition

    def set_standart_devition(self, standart_devition):
        self.__standart_devition = standart_devition

    def set_accuracy(self, accuracy):
        self.__accuracy = accuracy

    def set_f(self, f):
        self.__f = f

    def set_e(self, e):
        self.__e = e

    def set_s_ln_x(self, s_ln_x):
        self.__s_ln_x = s_ln_x

    def set_s_ln_xx(self, s_ln_xx):
        self.__s_ln_xx = s_ln_xx

    def set_s_ln_y(self, s_ln_y):
        self.__s_ln_y = s_ln_y

    def set_s_ln_xy(self, s_ln_xy):
        self.__s_ln_xy = s_ln_xy

    def set_s_x_ln_y(self, s_x_ln_y):
        self.__s_x_ln_y = s_x_ln_y

    def set_s_y_ln_x(self, s_y_ln_x):
        self.__s_y_ln_x = s_y_ln_x