import pytest
import SeqServices
from CurveADT import *
from Data import *


class TestSeq:
	def setup_method(self,method):
		self.X = [1,2,3,4,5]
		self.Y = [1,2,1,2]
		self.Z = [1,1,1,1]
	def teardown_method(self,method):
		self.X  = None
	def test_isAscending(self):
		assert SeqServices.isAscending(self.X) == True
		assert not(SeqServices.isAscending(self.Y) == True)
		assert SeqServices.isAscending(self.Z) == True
	def test_inBounds(self):
		assert SeqServices.isInBounds(self.X,3.3) == True

	def test_interpLin(self):
		assert SeqServices.interpLin(3.5,7.2,6,8.3,2) == pytest.approx(6.54, rel = 1e-3)

	def test_interpQuad(self):
		assert SeqServices.interpQuad(3.5,7.2,6,8.3,9.9,60,2) == pytest.approx(6132.308, rel = 1e-3)

	def test_index(self):
		assert SeqServices.index(self.X,1) == 0
		assert SeqServices.index(self.X,4.9) == 3

class TestCurve:
	def setup_method(self,method):
		self.curve = CurveT([1,2,3],[1,4,9],2)
	def teardown_method(self,method):
		self.X  = None

	def test_minD(self):
		assert self.curve.minD() == 1

	def test_maxD(self):
		assert self.curve.maxD() == 3

	def test_order(self):
		assert self.curve.order() == 2
	def test_eval(self):
		assert self.curve.eval(2.2) == pytest.approx(4.84, rel = 1e-5)
	def test_dfdx(self):
		assert self.curve.dfdx(2.3) == pytest.approx(4.6010000000, rel = 1e-3)

	def test_dfdx2(self):
		assert self.curve.dfdx2(2.3) == pytest.approx(1.9999999993913775, rel = 1e-3)

class TestData:
	def setup_method(self,method):
		Data.init()
		self.curve1 = CurveT([1,2,3],[1,4,9],2)
		self.curve2 = CurveT([1,2,3],[10,20,30],1)
		self.curve3 = CurveT([1,2,3],[3,6,9],2)

	def test_add(self):
		Data.add(self.curve1,1)
		Data.add(self.curve2,2)
		Data.add(self.curve3,9)

		assert Data.S[0] == self.curve1
		assert Data.S[1] == self.curve2
		assert Data.S[2] == self.curve3

		assert Data.Z == [1,2,9]

	def test_getC(self):
		Data.add(self.curve1,1)
		Data.add(self.curve2,2)
		Data.add(self.curve3,9)
		assert Data.getC(0) == self.curve1
		assert Data.getC(1) == self.curve2
		assert Data.getC(2) == self.curve3

	def test_eval(self):
		Data.add(self.curve1,1)
		Data.add(self.curve2,2)
		Data.add(self.curve3,9)	
		assert Data.eval(1,2.9) == pytest.approx(11.0, rel=1e-5)
	
	def test_slice(self):
		Data.add(self.curve1,1)
		Data.add(self.curve2,2)
		Data.add(self.curve3,9)
		self.curveNew = Data.slice(2.2,1)
		assert self.curveNew.minD() == 1
		assert self.curveNew.maxD() == 9 
		assert self.curveNew.order() == 1
		assert self.curveNew.eval(1.2) == pytest.approx(8.272,rel=1e-3)
		assert self.curveNew.dfdx(2.9)  == pytest.approx(-2.1999999999984254, rel = 1e-3)
		assert self.curveNew.dfdx2(3)  == pytest.approx(3.552713678800501e-09, rel = 1e-3)