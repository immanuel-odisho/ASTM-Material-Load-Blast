## @file Data.py
# @title Data
# @author Immanuel Odisho
# @date Feb/7/2018

from CurveADT import *
import SeqServices
from Exceptions import *

## @brief Data is an Abstract object that is a collection of all the curves and their corresponding values
class Data:

	## MAX_SIZE is the maximum amount of curves that Data can hold
	MAX_SIZE = 10

	Z = []
	S = []

	## @brief init is method to initialize the abstract object
	@staticmethod
	def init():
		Data.S = []
		Data.Z = []
		
	## @brief adds curves to data abstract object 
	@staticmethod
	def add(s,z):
		S = Data.S 		
		Z = Data.Z 		

		if (len(S) == Data.MAX_SIZE):
			raise Full("Maximum size exceeded")
		if ( not(Data.__isEmpty__(Data.Z)) and z <= Data.Z[-1]):
			raise IndepVarNotAscending("Independent Variable is Not Ascending")
		S = S + [s] 
		Z = Z + [z]

		Data.S = S
		Data.Z = Z

	## @brief returns the curve at the given index
	#  @param i is the value of the index to retrieve 
	#  @return returns a curve located at index i in Data
	@staticmethod
	def getC(i):
		S = Data.S
		size = len(Data.S)
		print(size)
		if (not(i >= 0 and i < size)):
			raise InvalidIndex("The index is not valid")
		return S[i]

	## @brief interpolates the data at the given index
	#  @param x independent value to use for interpolation
	#  @param z value that is used to retrieve the index of the curves in Data
	#  @return wil return the value of interpolation
	@staticmethod
	def eval(x,z):
	
		if (not(isInBounds(Data.Z,z))):
			raise OutOfDomain("The input variable is out of the domain")
	
		j = SeqServices.index(Data.Z,z)
	
		x1, y1, x2, y2 = Data.Z[j],(Data.S[j]).eval(x),Data.Z[j+1],(Data.S[j+1]).eval(x)

		return SeqServices.interpLin(x1, y1, x2, y2 ,x)

	## @brief slices the data and evaluates the curves at the same value
	#  @param x is the value to evaluate at
	#  @param i will be the order of the curve to return
	#  @return will return the new curve object
	@staticmethod
	def slice(x,i):
		Y = list(map(lambda CurveT: CurveT.eval(x), Data.S))
		return CurveT(Data.Z,Y,i)



	@staticmethod
	def __isEmpty__(X):
		return X == []




