class Account():
    def __init__(self, balance, withdrawal_balance):
        self.balance = balance
        self.withdrawal_balance = withdrawal_balance
    def deposit():
        pass
    def withdrawal(self, balance, wb):
        if wb <= balance:
            balance -= wb
            print(balance)
        else:
            print("Insufficient Funds")

b, w = map(int, input().split())
a1 = Account(b, w)
a1.withdrawal(b, w)