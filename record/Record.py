class Record:
    def record(self, data, name, fi):
        if data.get_file_or_console() == "file":
            self.record_file(data, name, fi)
        else:
            self.record_console(data, name, fi)

    def record_file(self, data, name, fi):
        return 1

    def record_console(self, data, name, fi):
        print(name)
        string = '|%-7c' % '№'
        for i in range(0, data.get_n()):
            string += '|%-7d' % (i+1)
        string += '|\n'

