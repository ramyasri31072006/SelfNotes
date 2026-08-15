''' Encapsulation --> Hiding Internal details and Control how Data is accessed
For example :
You want withdraw cash from your account. curr Balance = 100
you tried to withdraw 500
will it success?-->No bcoz _balance can't be -ve .
this is how encapsulation Controls the data.
'''
class BankAccount:
  def __init__(self,balance):
    self._balance = balance
  @property
  def balance(self):
    return self._balance
    
  def deposit(self,amount):
    if(amount < 0):
      raise ValueEroor("Deposit must be a Positve")
    self._balance += amount
    
  def withdraw(self,amount):
    if(amount <= 0)
      raise ValueError("Withdraw amount must be positive")
    if(amount > self.balance):
      raise ValueError("insufficient amount")
    self._balance -= amount
account = BankAccount(500)
account.balance = -50
account.deposit(-100)
account.withdraw(10000)
'''
In above class -->Deposit and withdraw ensures that balance always be in valid state
_balance --> kept as protected --> you are informing the others that it is 
a protected variable so handle it with care. 
which means while writing methods using this variables you need to add some 
validate conditions 
i.e withdraw -->making use of _balance -->so to validate you added few conditions

In python we can also access the protected variable without any restrictons
it belives developers doesn't missues it
'''
