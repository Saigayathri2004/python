class bankaccount:
	def __init__(self):
		self.balance=0
	def deposit(self):
		amount=int(input("Amount to be deposit: "))
		self.balance=+amount
	def withdraw(self):
		Amount=int(input("Amount to be withdraw: "))
		if self.balance>=Amount:
			self.balance=self.balance-Amount
		else:
			print("insufficient amount")
	def display(self):
		print("balance: ",self.balance)
object =bankaccount()
object.deposit()
object.withdraw()
object.display()