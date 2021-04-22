from methods.DecisionMatrix import DecisionMatrix


class Count:

    def count(self, data):
        data.set_s_x(self.count_s_x(data.get_mass()[0]))
        data.set_s_xx(self.count_s_xx(data.get_mass()[0]))
        data.set_s_xxx(self.count_s_xxx(data.get_mass()[0]))
        data.set_s_xxxx(self.count_s_xxxx(data.get_mass()[0]))
        data.set_s_y(self.count_s_x(data.get_mass()[1]))
        data.set_s_xy(self.count_s_xy(data.get_mass()))
        data.set_s_xxy(self.count_s_xxy(data.get_mass()))
        DecisionMatrix().decision(data)

    def count_s_x(self, mass):
        sum = 0
        for i in range(0, len(mass)):
            sum += mass[i]
        return sum

    def count_s_xx(self, mass):
        sum = 0
        for i in range(0, len(mass)):
            sum += (mass[i]) ** 2
        return sum

    def count_s_xxx(self, mass):
        sum = 0
        for i in range(0, len(mass)):
            sum += (mass[i]) ** 3
        return sum

    def count_s_xxxx(self, mass):
        sum = 0
        for i in range(0, len(mass)):
            sum += (mass[i]) ** 4
        return sum

    def count_s_xy(self, mass):
        sum = 0
        for i in range(0, len(mass[0])):
            sum += mass[0][i] * mass[1][i]
        return sum

    def count_s_xxy(self, mass):
        sum = 0
        for i in range(0, len(mass[0])):
            sum += mass[0][i] * mass[0][i] * mass[1][i]
        return sum