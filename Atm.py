class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self,amount):
        balanceAmount = self.balanceAmountCheck(self.cardNumber)
        if amount < balanceAmount:
            
            print("Current Account balance:",balanceAmount - amount)
        else:
            print('Your amount balance is less')
    
    def balanceAmountCheck(self,cardNumber):
        balance = int(50000)
        print("Account Balance:",balance)
        return balance
        

    def depositAmount(self,amount):
        balanceAmount = self.balanceAmountCheck(self.cardNumber)
        print('Current Account balance:',balanceAmount + amount)

def main():

    cardNumber = 183248957
    pinNumber = 1000000

    atm = Atm(cardNumber,pinNumber)
    print('Enter 1 for balance enquiry')
    print('Enter 2 for withdrawl')
    print('Enter 3 for deposit')
    option = int(input('Enter your option: '))

    if option == 1:
        atm.balanceAmountCheck(cardNumber)
    elif option == 2:
        amount = int(input('Enter an amount: '))
        atm.cashWithdrawl(amount)
    elif option == 3:
        amount = int(input('Enter an amount: '))
        atm.depositAmount(amount)

main()