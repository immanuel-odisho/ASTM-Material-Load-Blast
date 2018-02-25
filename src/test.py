from CurveADT import *
from Data import *
from Load import *
from Plot import *

X = range(11)
Y = list(map(lambda x: x**2, X))

c1 = CurveT(X, Y, 1)

print(c1.eval(6.5))

PlotCurve(c1, 2)

c2 = CurveT(X, Y, 2)

print(c2.eval(6.5))

PlotCurve(c2, 5)
#PlotCurve(c, 50) will look strange because of edge effects
#The scipy and the "lambda" version have the same problem

Load('glass.csv')

c3 = Data.getC(9)
PlotCurve(c3, 13)
print(Data.eval(18, 34))

c4 = Data.slice(18, 1)
PlotCurve(c4, 5)
print(c4.eval(34))
