from data.Data import *
from entry.Entry import *
from methods.CoefficientPirsona import CoefficientPirsona


class Main:
    data = Data()
    Entry().read(data)
    CoefficientPirsona().count(data)
