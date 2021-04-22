class Data:
    def __init__(self):
        self.__correlation = None
        self.__s_x = None
        self.__s_xx = None
        self.__s_xxx = None
        self.__s_xxxx = None
        self.__s_y = None
        self.__s_xy = None
        self.__s_xxy = None
        self.__n = None
        self.__mass = [[], []]
        self.__file_or_console = None

    def get_correlation(self):
        return self.__correlation

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

    def set_correlation(self, correlation):
        self.__correlation = correlation

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
        self.__mass[i][j] = number

    def set_file_or_console(self, file_or_console):
        self.__file_or_console = file_or_console
