class IndepVarNotAscending(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return str(self.message)

class SeqSizeMismatch(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return str(self.message)

class InvalidInterpOrder(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return str(self.message)

class OutOfDomain(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return str(self.message)

class Full(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return str(self.message)


class InvalidIndex(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return str(self.message)
