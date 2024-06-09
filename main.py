
from bank import Bank

def  main():
    bank = Bank("Abc Bank")
    curr_user = "admin"

    while True:
        if curr_user == "admin":
            msg = """
            ===== Admin User =====
            1. Create an account                                                                        
            2. Delete account                                                              
            3. View accounts list                                                            
            4. Check available balance                            
            5. Check the total loan amount.                                                       
            6. Change loan status
            7. Change bankrupt status
            8. Exit
            0. Change User
            """

            print(msg)
            choice = int(input("Enter your choice: "))

            if choice == 1:
                holder_name = input("Enter account holder name:")
                email = input("Enter holder email:")
                address = input("Enter address:")
                account_type = input("Enter account type (savings/current):")
                bank.add_account(holder_name, email, address, account_type)
                

            elif choice == 2:
                acc_no = input("Enter account no to delete: ")
                bank.delete_account(acc_no)

            elif choice == 3:
                bank.view_accounts()

            elif choice == 4:
                bank.view_total_balance()

            elif choice == 5:
                bank.view_total_loan()

            elif choice == 6:
                loan_status = input("Enter loan status (on/off): ")
                bank.change_loan_status(loan_status)

            elif choice == 7:
                status = input("Enter new bankrupt status (True/False): ")
                bank.change_bankrupt_status(status)

            elif choice == 8:
                print("Thank you!")
                break

            elif choice == 0:
                new_user = input("Enter new user type (customer/admin)")
                if new_user not in ["customer", "admin"]:
                    print("Invalid input. Try again.")
            
                curr_user = new_user

            else:
                print("Invalid choice. Please choose again.")
        else:
            
            msg = """
            ======= Customer ========
            1. Create an
            account                                                                        
            2. Deposit                                                              
            3. withdraw                                                           
            4. Check available balance                            
            5. Check transaction history                                                      
            6. Take loan
            7. Transfer
            8. Exit
            0. Change User
            """
        

            print(msg)
            choice = input("Enter your choice: ")
            
            if choice == "1":
                holder_name = input("Enter account holder name:")
                email = input("Enter holder email:")
                address = input("Enter address:")
                account_type = input("Enter account type (savings/current):")
                bank.add_account(holder_name, email, address, account_type)
            
            elif choice == "2":
                acc_no = input("Enter acc no:")
                account = bank.get_account(acc_no)
                if account:
                    amount = float(input("Enter deposit amount:"))
                    account.deposit(amount)

            elif choice == "3":
                if bank.is_bankrupt:
                    print(f"Sorry, {bank.name} is bankrupt !!")
                    return
                
                acc_no = input("Enter acc no:")
                account = bank.get_account(acc_no)
                if account:
                    amount = float(input("Enter withraw amount:"))
                    account.withdraw(amount)

            elif choice == "4":
                acc_no = input("Enter acc no:")
                account = bank.get_account(acc_no)
                if account:
                    account.check_balance()

            elif choice == "5":
                acc_no = input("Enter acc no:")
                account = bank.get_account(acc_no)
                if account:
                    account.check_transaction_history()
            
            elif choice == "6":
                acc_no = input("Enter acc no:")
                amount = float(input("Enter amount:"))
                bank.take_loan(acc_no, amount)
            
            elif choice == "7":
                from_acc_no = input("Enter from acc no:")
                to_acc_no = input("Enter to acc no:")
                amount = float(input("Enter amount:"))
                bank.transfer(from_acc_no, to_acc_no, amount)
                
            elif choice == "8":
                print("Thank you!")
                break

            elif choice == "0":
                new_user = input("Enter new user type (customer/admin)")
                if new_user not in ["customer", "admin"]:
                    print("Invalid input. Try again.")
                
                curr_user = new_user

            else:
                print("Invalid choice. Please choose again.")


main()