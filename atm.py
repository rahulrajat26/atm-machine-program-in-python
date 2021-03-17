import time

print('Please Enter Your Card')
time.sleep(5)

password = 1234

pin=int(input('Enter your pin:'))
balance = 5000

if pin == password:
    while True:
        print("""
            1 == Balance
            2 == Withdraw balance
            3 == Deposite balance
            4 == Exit
            """
            )
        try:
            option = int(input("Please enter your choice : "))
        except:
            print('\n Please enter valid option!')
            print('===================================')
            
        if option == 1:
            print(f"\n Your balance is {balance}")
            print('===================================')
            
        if option == 2:
            time.sleep(2)
            withdraw_amt=int(input("\n Enter withdraw amount : "))
            balance = balance - withdraw_amt
            time.sleep(2)
            print(f"\n {withdraw_amt} is debited from your account.\n")
            time.sleep(2)
            print(f"Your updated balance is {balance}")
            print('===================================')
            
        if option == 3:
            deposite_amt = int(input('\n Please enter deposite amount : '))
            balance = balance + deposite_amt
            time.sleep(2)
            print(f'\n {deposite_amt} is credited to your account.\n')
            time.sleep(2)
            print(f'your updated balance is {balance}')
            print('===================================')
            
        if option == 4:
            break

else:
    print('Wrong pin please try again!!')