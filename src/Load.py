## @file Load.py
# @title Load
# @author Immanuel Odisho
# @date Feb/7/2018


from CurveADT import *
from Data import *

## @brief loads data from input file into Data abstract object
#  @details this function will receive and input file, sort the data and load it into Data abstract object
#  @param s is the input file
def Load(s):

	r = open(s,"r")
	z = r.readline().split(",")
	o = r.readline().split(",")
	z = [float(i) for i in z]
	o = [int(i) for i in o]
	if len(o) < len(z):
	    length = len(o)
	else:
	    length = len(z)

	z_x = {}
	z_y = {}
	for i in range(1,length+1):
	    z_x["z_{0}".format(i)] = []
	    z_y["z_{0}".format(i)] = []


	for line in r:
	    j = 1
	    n = line.split(",")
	    
	    for i in range(0,2*length,2):
	        if n[i] != '':
	            z_x["z_{0}".format(j)].append(float(n[i]))
	            z_y["z_{0}".format(j)].append(float(n[i+1]))
	        j += 1
            
    
	r.close()

	Data.init()
	curve = {}
	j = 1
	for i in range(length):
		curve["c_{0}".format(j)] = CurveT(z_x["z_{0}".format(j)],z_y["z_{0}".format(j)],o[i])
		Data.add(curve["c_{0}".format(j)],z[i])
		j += 1

