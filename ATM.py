import time
Balance=int(input("Enter Amount:"))
Password=1234
print("Welcome to SBI Bank")
time.sleep(1)
print("Insert your Card")
print("1.Yes\n2.No")
choice=int(input())
if choice==1:
    print("Select Language:")
    print("1.English\n2.Kannada\n3.Telugu")
    lang=int(input())
    if lang==1:
        pin=int(input("Enter your Password:"))
        if pin==Password:
            print("Select your Option")
            print("1.Balance\n2.Withdrawal")
            option=int(input())
            if option==1:
                print("Balance Amount is",Balance)
            elif option==2:
                print("Enter the Amount:")
                amountToWithdrawal=int(input())
                if amountToWithdrawal <= Balance:
                    if amountToWithdrawal % 100 == 0:   
                        print("Transaction is processing")
                        time.sleep(4)
                        print("Please collect your Amount")
                        time.sleep(2)
                        print("Do you want to check your Balance")
                        print("1.Yes\n2.No")
                        choice1=int(input())
                        if choice1==1:
                            print("Your available balance is:",Balance-amountToWithdrawal)
                            print("Thankyou, Visit again")
                        else:
                            print("Thankyou, Visit again")
                    else:
                        print("Enter correct amount")
                else:
                    print("You don't have that much amount")
            else:
                print("Select the Correct Option")
        else:
            print("Enter Correct Password")
    else:
        print("Select Language English")
else:
      print("Insert your card properly")
