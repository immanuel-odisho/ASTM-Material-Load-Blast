## @file CurveADT.py
# @title CurveADT
# @author Immanuel Odisho
# @date Feb/7/2018

from SeqServices import *
from scipy import interpolate
from Exceptions import *

## MAX_ORDER is the maximum order of interpolation
MAX_ORDER = 2
## DX is the constant used for derivative calculations
DX = 1e-3

## @brief CurveT is and ADT that allows isntances of curve objects to be made
class CurveT():
	## @brief CurveT initiliaze curve object
	#  @param X is a sequence of values represent the independent variable must and are ascending
	#  @param Y is a sequence of values represent the dependent variable
	#  @param i is the order of the interpolation for the curve
	def __init__(self,X,Y,i):
		if (not(isAscending(X))):
			raise IndepVarNotAscending("Independent Variable is Not Ascending")
		if (len(X) != len(Y)):
			raise SeqSizeMismatch("Sequence Sizes are a Mismatch")
		if(not(i == 1 or i ==2)):
			raise InvalidInterpOrder("Invalid Order of Interpolation")
		self.minx = X[0]
		self.maxx = X[-1]
		self.o = i
		self.f = interpolate.interp1d(X,Y,i)

	## @brief minD, getter that returns minimum value in the independent variable sequence
	#  @return minimum value in the independent variable sequence
	def minD(self):
		return self.minx

	## @brief maxD, getter that returns maximum value in the dependent variable sequence
	#  @return maximum value in the dependent variable sequence
	def maxD(self):
		return self.maxx

	## @brief getter that returns the order of interpolation for the curve
	#  @return order of interpolation for the curve
	def order(self):
		return self.o
	## @brief evaluates the interpolation function of the curve at x
	#  @param x is the independent value to evaluate the function at
	#  @return the value of the interpolation function at x 
	def eval(self,x):
		if (not(x <= self.maxx and x >= self.minx)):
			raise OutOfDomain("The input variable is out of the domain")
		return self.f(x)

	## @brief evaluates the derivative of the curve at x
	#  @param x is the independent value to evaluate the derivative at
	#  @return the value of the derivative at x
	def dfdx(self,x):
		if (not(x <= self.maxx and x >= self.minx)):
			raise OutOfDomain("The input variable is out of the domain")
		return ((self.f(x+DX) - self.f(x))/ DX)

	## @brief evaluates the second derivative of the curve at x
	#  @param x is the independent value to evaluate the second derivative at
	#  @return the value of the second derivative at x
	def dfdx2(self,x):
		if (not(x <= self.maxx and x >= self.minx)):
			raise OutOfDomain("The input variable is out of the domain")
		return ((self.f(x+2*DX) - 2*self.f(x + DX) + self.f(x))/ DX**2)









