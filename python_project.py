balance=10000
attempts=0
Correctpin=1234
while True:
    pin=int(input("Enter Pin: "))
    if pin==Correctpin:
        print("Welcome!")
        out=[]
        while True:
            print("""-----MENU-----
1=Balance
2=Withdraw
3=Deposits
4=Exit""")
            a=int(input("Choose options above"))
            if a==1:
                print("Aval Balance", balance)
            elif a==2:
                withdraw=int(input("enter withdraw amount: "))
                if withdraw<balance:
                    out.append((f"withdraw{withdraw}"))
                    balance=balance-withdraw
                    print("aval balance",balance)
                else:
                    print("insufficent balance")
            elif a==3:
                deposit=int(input("Enter Deposit amount: "))
                if deposit>0:
                    balance= balance+deposit
                    out.append((f"deposited{deposit}"))
                    print("aval balance", balance)
                else:
                    print("invalid deposit")
            elif a==4:
                print("Thank You For using!")
                print("transaction history",out)
                break
            else:
                print("invalid input, choose from 1-4")             
        break
    else:
        print("invalid input")
        attempts+=1
        if attempts>2:
            print("card Blocked")
            break

#Q2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
maxavg=0
topper=""
while True:
    print("""-----MENU-----
1=ADD STUDENT
2=VIEW ALL
3=SHOW TOPPER
4=Exit""")
    a=int(input("enter option from menu"))
    if a==1:
        name=input("enter the name of student: ")
        value=list(input("enter marks"))
        if len(value)!=3:
            print("enter three distinct marks")
    elif a==2:
        for keys in students:
            sum=0
            for value in students[keys]:
                sum+=value
            avg=float(f"{sum/len(students[keys]):.2f}")
            if avg>85:
                grade="A"
            elif avg>70:
                grade="B"
            elif avg>55:
                grade="C"
            else:
                grade="D"
        print(keys,avg,grade)
        if avg>maxavg:
                maxavg=avg
                topper=keys
    elif a==3:
        print("maxavg", maxavg)
        print("Topper", topper)
    elif a==4:
        print("GoodBye!")
    else:
        print("take input from 1-4")
