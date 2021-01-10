
class account():
	
	def __init__(self, data,balance = 500):
		self.balance = balance
		self.name  = data[0]

	def get_Balance(self):
		return self.balance()

	def calculate_Profit_Percent(self,amount,percent):
		return percentage_increase(amount,percent)


new = account("Samuel")
print(new.calculate_Profit_Percent(100,50))