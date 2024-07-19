

class Delegation:

	def __init__(self, candidate:str, amount:int):
		self.candidate = candidate
		self.amount = amount


def validate_res(res):
	return res['result']['Ok']['data']['Ok']