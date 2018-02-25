## @file Plot.py
# @title Plot
# @author Immanuel Odisho
# @date Feb/7/2018

from CurveADT import *
import matplotlib.pyplot as plt 
from Exceptions import *


win = plt.plot()

#  @param function to plot and display graph of two sequences
#  @param X is the first sequence, the independent variable
#  @param Y is the dependent variable sequences
def PlotSeq(X,Y):
	if (len(X) != len(Y)):
		raise SeqSizeMismatch("Sequence Sizes are a Mismatch")
	win = plt.plot(X,Y)
	plt.show(win)

## @brief will plot a curve using it's order of interpolation
#  @param c is the curve to plot
#  @param n is the interval between points 
def PlotCurve(c,n):
		X = range(round(c.minD()),c.maxD()+n,n)
		Y = [c.eval(i) for i in X]
		win = plt.plot(X,Y)
		plt.show(win)


