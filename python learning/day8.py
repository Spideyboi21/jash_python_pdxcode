class BankAccount:
  def __init__(self, name, balance):
      self.name = name
      self.balance = balance

  def withdraw(self, amount):
      if self.balance - amount >0:
         self.balance -= amount
         print("Thanks {n}! You withdrew ${am}".format(n=self.name, am=amount))
    else:
    print('You don\'t have enough money to withdraw $ {am} fool!'.format(am))






class MinimumbalanceAccount(BankAccount):
    def__init__(self, amount):
    if self.balance - amount < self.Minimum_balance:
        print('Sorry, minimum balance must be maintained.')
    else:
        BankAccount.withdraw(self, amount)




account1 = BankAccount('Chelsea', 1000)

account2 = MinimumbalanceAccount(100)
account2.deposit(50)





class person:
    def__init__(self, name):
        self.name = name
        self.health = 100

player1 = Person('Jash')
player2 = Person('Nisa')

def fight(p1, p2):
    p1.health -= random.randint(1, 10)
    p2.health -= random.randint(1, 10)

fight(player1, player2)

print(player1.name, player1.health)

print(player2.name, player2.health)
