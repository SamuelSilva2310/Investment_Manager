import calculations



#This is the account class, it will hold all information and actions the user can do.
#It will recieve:
	# data -> This could be the data converted from JSON, it will have everything needed about the account
	# balance -> This is temporary just for testing and developing, all data will then be recieves trough the data object
class account():
	
	def __init__(self, data,balance = 500):
		self.balance = balance
		self.name  = data

	def get_Balance(self):
		return self.balance()

	def calculate_Profit_Percent(self,amount,percent):
		return calculations.percentage_increase(amount,percent)


new = account("Samuel")
print(new.calculate_Profit_Percent(100,50), new.name)