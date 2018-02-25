## @file SeqServices.py
# @title SeqServices
# @author Immanuel Odisho
# @date Feb/7/2018

## @brief will check if a sequence of numbers is ascending
#  @param X is the sequence of numbers
#  @return boolean
def isAscending(X):
	for i in range(0,len(X)-1):
		if (X[i+1] >= X[i]):
			pass
		else:
			return False
	return True

## @brief will see if a given value falls within a sequence
#  @param X is the sequence 
#  @param x is the value
#  @return will return a boolean
def isInBounds(X,x):
	return (x <= X[-1] and x >= X[0])

## @brief will apply linear interpolation between 2 points and given value
#  @param x1 x1 coordinate
#  @param y1 y1 coordinate
#  @param x2 x2 coordinate
#  @param y2 y2 coordinate
#  @param x is the value to interpolate about
#  @return returns evaluation 
def interpLin(x1,y1,x2,y2,x):
	return ((y2-y1)/(x2-x1))*(x-x1) + y1
	 
## @brief will apply quadratic interpolation between 3 points and given value
#  @param x1 x1 coordinate
#  @param y1 y1 coordinate
#  @param x2 x2 coordinate
#  @param y2 y2 coordinate
#  @param x3 x3 coordinate
#  @param y3 y3 coordinate
#  @param x is the value to interpolate about
#  @return returns evaluation 
def interpQuad(x0,y0,x1,y1,x2,y2,x):
	return y1 + ((y2-y0)/(x2-x0))*(x-x1)+((y2-2*y1+y0)/2*(x2-x1)**2)*(x-x1)**2


## @brief will return the index of a value in a sequence
#  @param X is the sequence
#  @param x is the value
#  @return index
def index(X,x):
	for i in range(0,len(X)):
		
		if (x < X[i]):
			return i - 1
		elif (x == X[i]):
			return i



