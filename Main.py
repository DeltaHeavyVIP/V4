from data.Data import *
from entry.Entry import *
from methods.CoefficientPirsona import CoefficientPirsona
from methods.Function import Function


class Main:
    data = Data()
    Entry().read(data)
    CoefficientPirsona().count(data)
    Function().count(data)
    Function.function(data)
