from data.Data import *
from entry.Entry import *
from methods.CoefficientPirsona import CoefficientPirsona
from methods.Count import Count
from methods.Function import Function


class Main:
    data = Data()
    Entry().read(data)
    CoefficientPirsona().count(data)
    Count().count(data)
    Function().function(data)
