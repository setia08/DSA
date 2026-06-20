class BankAccount:
    def __init__(self, owner, balance):   # called when object is created
        self.owner = owner
        self.balance = balance

    def __str__(self):                    # called by print()
        return f"{self.owner}'s account: ₹{self.balance}"

    def __repr__(self):                   # called in terminal/debugging
        return f"BankAccount('{self.owner}', {self.balance})"

    def __len__(self):                    # called by len()
        return self.balance

    def __add__(self, other):             # called by +
        return BankAccount(self.owner, self.balance + other.balance)

    def __eq__(self, other):              # called by ==
        return self.balance == other.balance

    def __lt__(self, other):             # called by <
        return self.balance < other.balance

    def __bool__(self):                  # called by if obj:
        return self.balance > 0


a1 = BankAccount("Navneet", 5000)
a2 = BankAccount("Rahul",   3000)

print(a1)           # __str__  → Navneet's account: ₹5000
print(repr(a1))     # __repr__ → BankAccount('Navneet', 5000)
print(len(a1))      # __len__  → 5000

a3 = a1 + a2        # __add__  → new account with ₹8000
print(a3)           # Navneet's account: ₹8000

print(a1 == a2)     # __eq__   → False
print(a2 < a1)      # __lt__   → True

if a1:              # __bool__
    print("Has money")   # prints this
