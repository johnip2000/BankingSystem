#----------Asssignment 1 Coding by Wai Ki Ip Jason 8689247----------------#
import sys


def menu():
    print("##########################################")
    print("#                                        #")
    print("#  Welcome to the online banking system. #")
    print("#  Please input your choice (1,2,3,4,5). #")
    print("#  1. Create Bank Accounts.              #")
    print("#  2. Perform Account Deposits.          #")
    print("#  3. Perform Account Withdraws.         #")
    print("#  4. Create Account Transfer.           #")
    print("#  5. View your Account.                 #")
    print("#  6. Quit Application.                  #")
    print("#                                        #")
    print("##########################################")

class Customer:
    deposits = 0
    name = ""

cus = Customer()

def createAccount():
    print("Please enter your account name: ", end ="")
    name = input()
    cus.name = name
    cus.deposits = 0
    print("You have successfully create an account. Please continue your operation.")
    print("")
    main()

def performDeposit():
    try:
        print("How much you would like to deposit to your account?: ", end="")
        depo = float(input())
        cus.deposits = cus.deposits + depo
        print("You have successfully deposit", depo, end= "")
        print(" to your account. Please continue...")
        print("")
        main()
    except:
        print("You should input the correct information")
        performDeposit()

def performWithdraw():
    try:
        if cus.deposits == 0:
            print("You don't have any money in your account. Please deposit some money first.")
            main()
        else:
            print("How much you would like to withdraw from your account?: ", end="")
            withd = float(input())
            if withd > cus.deposits:
                print("You don't have enough money to withdraw. Please try again. "
                "If you don't want to withdraw any money, you may input 0 to return to the menu.")
                performWithdraw()
            else:
                cus.deposits = cus.deposits - withd
                print("You have successfully withdraw", withd, end="")
                print(" from your account. Please continue...")
                print("")
                main()
    except:
        print("You should input the correct information")
        performWithdraw()

def performTransfer():
    try:
        if cus.deposits == 0:
            print("You don't have any money in your account. Please deposit some money first.")
            main()
        else:
            print("Please enter the account you would like to transfer the money: ", end = "")
            trans = input()
            print("Please enter how much you would like to transfer to ", trans, end="")
            print(": ")
            transMoney = float(input())
            if transMoney > cus.deposits:
                print("You don't have enough money to transfer. Please deposit some money or try again. ")
                main()
            else:
                cus.deposits = cus.deposits - transMoney
                print("You have successfully transfer", transMoney, end="")
                print(" to", trans)
                print("Please continue...")
                print("")
                main()
    except:
        print("You should input the correct information")
        performTransfer()

def viewAccount():
    print("Your account: ", cus.name)
    print("Your deposit: ",cus.deposits)
    print("Please continue...")
    main()

def performQuit():
    print("Thanks for using this application")

def noAccount():
    print("You haven't created any account. Please create one. Thanks.")
    print("")
    main()

def havingAccount():
    print("You have created an account. Please choose other options")
    print("")
    main()

def main():

    menu()
    print("")
    print("Please enter your choice: ", end="")
    cusChoice = int(input())
    print("")
    if cusChoice == 1:
        # if cus.name != "":
        #     havingAccount()
        # else:
        createAccount()
    elif cusChoice == 2:
        if cus.name != "":
            performDeposit()
        else:
            noAccount()
    elif cusChoice == 3:
        if cus.name != "":
            performWithdraw()
        else:
            noAccount()
    elif cusChoice == 4:
        if cus.name != "":
            performTransfer()
        else:
            noAccount()
    elif cusChoice == 5:
        if cus.name == "":
            noAccount()
        else:
            viewAccount()
    elif cusChoice == 6:
        performQuit()
    else:
        print("Please try again to enter a correct choice")
        print("")
        main()          #recursive to main if choice is not correct


if __name__ == "__main__":
    main()