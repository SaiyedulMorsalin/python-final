from Users import Customer, Admin
from Bank import Bank

def main():
    bank = Bank('american bank', 1000000000000000)
    admin = Admin("saiyedul", "saiyedul@gmail.com")
    admin.create_account(bank)
    while True:
        print("1. Customer")
        print("2. Admin")
        op = int(input("Enter an option: "))
        if op == 1: 
            print("1. Register")  
            print("2. Login")
            uop = int(input("Enter an option: "))
            if uop == 1:
                u_name = input("Enter Your Name: ")
                u_email = input("Enter Your Email: ")
                a_type = input("Enter Account Type: ")
                user = Customer(name=u_name,email=u_email,account_type=a_type)
                user.create_account(bank)
                print("Successfully Registered!!!")
                print(" -----------------------------")
                while True:
                    uu_name = input("Enter User Name: ")
                    uu_email = input("Enter User Email: ")
                    ck = False
                    for item in bank.users.items():
                        if uu_email == item[0] and uu_name == item[1].name:
                            print("Login Successfull!!")
                            print(" -----------------------------")
                            
                            ck = True
                    if ck == False:
                        print("Please Provide Valid Name and Email.......")
                    elif ck == True:
                        break
                
            elif uop == 2:
                nums = 3
                while True:
                    if len(bank.users) >0:
                        uu_name = input("Enter User Name: ")
                        uu_email = input("Enter User Email: ")
                        ck = False
                        for item in bank.users.items():
                            if uu_email == item[0] and uu_name == item[1].name:
                                print("Login Successfull!!")
                                print(" -----------------------------")
                                ck = True
                        if ck == False:
                            nums = nums -1
                            print("Please Provide Valid Name and Email.......")
                            if nums == 0:
                                break
                            print(f"{nums} more times attemps")
                        elif ck == True:
                            break
                    else:
                        print("Please Create One Account this Bank")
                        break
            while True:
                if len(bank.users) <= 0:
                    break
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. View Balance")
                print("4. View Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7 Exit")
                n = int(input("Enter an option: "))
                if n == 1:
                    dep = int(input("Enter deposit amount: "))
                    user.deposit(dep)
                elif n == 2:
                    draw = int(input("Enter withdraw amount: "))
                    user.withdraw(draw)
                elif n == 3:
                    user.view_balance()
                elif n == 4:
                    user.view_transaction_history()
                elif n == 5:
                    amount = int(input("Enter loan amount: "))
                    user.take_loan(amount)
                elif n == 6:
                    if len(bank.users) >1:
                        t_user = input("Enter User Email: ")
                        for item in bank.users.items():
                            if item[0] == t_user:
                                amount = int(input("Enter transfer amount: "))
                                user.transfer(item[1],amount)
                    else:
                        print("Not found another account")         
                elif n == 7:
                    break
                else:
                    print("Enter valid option")
        elif op == 2:
            nums = 3
            ck = False
            while True:
                if len(bank.admins) >0:
                    ad_name = input("Enter Admin Name: ")
                    ad_email = input("Enter Admin Email: ")
                    for item in bank.admins.items():
                        if ad_name == item[0] and ad_email == item[1].email:
                            print("Login Successfull!!")
                            print(" -----------------------------")
                            ck = True
                    if ck == False:
                        nums = nums -1
                        print("Please Provide Valid Name and Email.......")
                        if nums == 0:
                            break
                        print(f"{nums} more times attemps")
                    elif ck == True:
                        break
                else:
                    print("Please Create Admin Account in this Bank")
                    break
            while True:
                if ck == False:
                    break
                print("1. Create a user Account")
                print("2. Delete User Account")
                print("3. View All Users")
                print("4. View total bank balance")
                print("5. View total bank loan")
                print("6. Off Loan Feature")
                print("7. Exit")
                choice = int(input("Enter an option admin: "))
                if choice == 1:
                    u_name = input("Enter Your Name: ")
                    u_email = input("Enter Your Email: ")
                    a_type = input("Enter Account Type: ")
                    user = Customer(name=u_name,email=u_email,account_type=a_type)
                    user.create_account(bank)
                    print("Successfully Registered!!!")
                    print(" -----------------------------")
                elif choice == 2:
                    de_email = input("Enter User Email: ")
                    admin.delete_user_account(de_email,bank)
                elif choice == 3:
                    admin.view_users()
                    
                elif choice == 4:
                    admin.view_total_balance()
                elif choice == 5:
                    admin.view_total_loan()
                elif choice == 6:
                    dicision = input("Enter Decision (y/n): ")
                    if dicision == 'y':
                        admin.switch_loan_feature(True)
                    else:
                        admin.switch_loan_feature(False)
                elif choice == 7:
                    break
                else:
                    print("Enter a valid option")
            
if __name__ == '__main__':
    main()