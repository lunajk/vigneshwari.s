class bankaccount:
  def __init__(self, account_number,account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("deposited ${}. new balance: ${}".format(amount,self.__account_balance))
    else:
      print("invalid deposit amount. please deposit a positive amount.")

  def withdrew(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdrew ${}. new balance: ${}".format(amount,self.__account_balance))
    else:
      print("invalid withdrawl amount or insufficint balance.")

  def display_balance(self):
    print("account balance for {} (account #{}): ${}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))



account = bankaccount(account_number="12345678",
                     account_holder_name="hari",
                     initial_balance=5000.0)


account.display_balance()
account.deposit(500.0)
account.withdrew(200.0)
account.withdrew(20000.0)
account.display_balance()
      
    
    
    