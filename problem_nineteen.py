print("Welcome to the Python ATM")
print("-----------------------------------------")
pn = int(input("Create pin for your security: "))
user = {
    'pin': pn,
    'balance':0
}

def deposit_cash():
    while True:
        amount = int(input("Enter the amount of money you want to deposit: "))
        if amount > 0:
            user['balance'] = user['balance'] + amount
            print(f"{amount} Dollars successfully deposited your new balance is {user['balance']} Dollars")
            print('')
            return False

def widthdraw_cash():
        amount = int(input("Enter the amount of money you want to widthdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Dollars successfully widthdrawn your remaining balance is {user['balance']} Dollars")
            print('')

def current_balance():
    print(f"Total balance {user['balance']} Dollars")
    print('')


is_quit = False

print('')

pin = int(input('Please enter your pin: '))

print("------------------------------------------------------------")

if pin == user['pin']:
    while is_quit == False:
        print("what do you want to do")
        print(" Enter 1 to Deposit Cash \n Enter 2 to Widthdraw Cash \n Enter 3 for Current_balance \n Enter 4 to Quit")

        query = int(input("Enter the number corresponding to the activity you want to do: "))
        print("------------------------------------------------------------")
        if query == 1:
            deposit_cash()
        elif query == 2:
            widthdraw_cash()
        elif query == 3:
            current_balance()
        elif query == 4:
            is_quit = True

        else:
            print("Please enter a correct value shown")
else:
    print("You entered wrong pin")