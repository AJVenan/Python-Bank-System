import os
import re
from pathlib import Path
from datetime import datetime

now = datetime.now()
dateTime = now.strftime("%d/%m/%Y %H:%M:%S")

class AJSVBank():

    def __init__(self, currentBalance=0.00):
        self.balance = float(currentBalance)


    def log_transactions(self, transaction_Details):
        with open(f"{Path.home()}/Downloads/{accountName}.txt", "a") as file:
            file.write(f"{transaction_Details}\n")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance - amount
        self.log_transactions(f"Withdraw an amount of: {amount} (Date: {dateTime})")
        return self.balance

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance + amount
        self.log_transactions(f"Deposit an amount of: {amount} (Date: {dateTime})")
        return self.balance

    def isDigit(self, x):
        try:
            float(x)
            return True
        except ValueError:
            return False
        
    def modify(self, filepath, from_, to_):
        file = open(filepath,'r+')
        text = file.read()
        pattern = from_
        splitted_text = re.split(pattern,text)
        modified_text = to_.join(splitted_text)
        with open(filepath, 'w') as file:
            file.write(modified_text)

print('\n Welcome to AJSV Bank')
accountVerification = input('\n Do you already have an account here? Y/N: ')

if accountVerification in ('Yes', 'yes', 'YES', 'ye', 'YE', 'Y', 'y'):
    accountName = input('\n What is your account Name? ')

    if os.path.exists(f'{Path.home()}/Downloads/{accountName}.txt'):
        print(f'\n Account is verified, Welcome {accountName}')

        transaction = input('\n What transaction would you like to make? Withdraw, Deposit or Balance: ')

        if transaction in ('Withdraw', 'W', 'w'):
            userAccount = open(f'{Path.home()}/Downloads/{accountName}.txt', 'r')
            userAccountRead = userAccount.readlines()

            for i in userAccountRead: 
                userAccountCurrentBalance = i.split()[1]
                break

            userAccountBalance = AJSVBank(userAccountCurrentBalance)

            withdrawAmount = input(f'\n Your current balance is {userAccountBalance.balance}, Enter the amount that you want to withdraw: ')
            
            if userAccountBalance.isDigit(withdrawAmount):

                if(float(userAccountBalance.balance) < float(withdrawAmount)):
                        print('\n Error you cannot withdraw an amount that is greater than your balance')
                else:
                    userAccountBalance.modify(f'{Path.home()}/Downloads/{accountName}.txt', f'Balance: {float(userAccountBalance.balance)}', f'Balance: {userAccountBalance.withdraw(withdrawAmount)}')
                    print(f'\n Thank you for your transaction your new balance is {userAccountBalance.balance}, now leaving the ATM\n')
                    # userAccountWrite = open(f'{Path.home()}/Downloads/{accountName}.txt', 'w')
                    # for i in userAccountRead:
                    #     userAccountWrite.writelines(f'Balance: {userAccountBalance.withdraw(withdrawAmount)}')  
                    #     break
                    # userAccountBalance.log_transactions(f"Withdraw an amount of: {withdrawAmount} {dateTime}")
                # for line in userAccountRead:
                #     if(float(userAccountBalance.balance) < float(withdrawAmount)):
                #         print('\nError you cannot withdraw an amount that is greater than your balance')
                #     else:
                #         userAccountBalance.modify(f'{Path.home()}/Downloads/{accountName}.txt', f'Balance: {int(userAccountBalance.balance)}', f'Balance: {userAccountBalance.withdraw(withdrawAmount)}')
                #         # userAccountWrite = open(f'{Path.home()}/Downloads/{accountName}.txt', 'w')
                #         # for i in userAccountRead:
                #         #     userAccountWrite.writelines(f'Balance: {userAccountBalance.withdraw(withdrawAmount)}')  
                #         #     break
                #         # userAccountBalance.log_transactions(f"Withdraw an amount of: {withdrawAmount} {dateTime}")
                #         break
                #         # # userAccountWrite.writelines(f'Balance: {currentBalance}') 
                #     break
            else:
                print('\n Error entered amount')
        elif transaction in ('deposit', 'D', 'd'):
            userAccount = open(f'{Path.home()}/Downloads/{accountName}.txt', 'r')
            userAccountRead = userAccount.readlines()

            for i in userAccountRead: 
                userAccountCurrentBalance = i.split()[1]
                break

            userAccountBalance = AJSVBank(userAccountCurrentBalance)

            depositAmount = input(f'\n Your current balance is {userAccountBalance.balance}, Enter the amount that you want to deposit: ')
            
            if userAccountBalance.isDigit(depositAmount):
                userAccountBalance.modify(f'{Path.home()}/Downloads/{accountName}.txt', f'Balance: {float(userAccountBalance.balance)}', f'Balance: {userAccountBalance.deposit(depositAmount)}')
                print(f'\n Thank you for your transaction your new balance is {userAccountBalance.balance}, now leaving the ATM\n')
            else:
                print('\n Error entered amount')
        elif transaction in ('Balance', 'balance', 'B', 'b'):
            userAccount = open(f'{Path.home()}/Downloads/{accountName}.txt', 'r')
            userAccountRead = userAccount.readlines()

            for i in userAccountRead: 
                userAccountCurrentBalance = i.split()[1]
                break

            userAccountBalance = AJSVBank(userAccountCurrentBalance)
            print(f'\n Your current Balance is {userAccountBalance.balance}\n')
        else:
            print('\n Error transaction selection\n')
    else:
        print('\n Sorry account does not exist\n')
elif accountVerification in ('No', 'no', 'NO', 'n', 'N'):
    createAccount = input('\n Do you want to create an account? Yes or No: ')

    if createAccount in ('Yes', 'yes', 'YES', 'y', 'Y'):

        createAccountName = input('\n What would you name your account? ')

        if os.path.exists(f'{Path.home()}/Downloads/{createAccountName}.txt'):
            print('\n Sorry but the account name already exist. Exiting ATM \n')
        else:
            newUserAccount = open(f'{Path.home()}/Downloads/{createAccountName}.txt', 'a')
            assignAccountBalance = input(f'\n Thank you we have successfully create a new account. \n\n Welcome {createAccountName}, How much would you like to deposit? ')

            userAccountBalance = AJSVBank(assignAccountBalance)

            if userAccountBalance.isDigit(assignAccountBalance):
                newUserAccount.write(f'Balance: {float(assignAccountBalance)}\n\nTransactions:\n\nSuccesfully deposit an amount of:  {float(assignAccountBalance)} (Date: {dateTime})\n')
                print(f'\n Thank you, your balance on your account is {float(assignAccountBalance)}. Now leaving the ATM \n')
            else:
                print('\n Sorry wrong input. Exiting ATM \n')
        
else:
    print('\n Wrong selection\n')

