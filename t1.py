import mysql.connector
db=mysql.connector.connect(host="localhost",database="bank",user="root",password="Bank@123")

mc=db.cursor(buffered=True)


print("-"*266)
print("BANKING MANAGEMENT SYSTEM".center(120))
print("-"*266)
print("WELCOME TO KK ONLINE BANK SERVICE".center(120))
def menu():
    print("*"*114) 
    print("MENU".center(120))
    print("*"*114)
    print("1-> Insert Records".center(120))
    print("2-> Display Records".center(120))
    print("3-> Search Records".center(120))
    print("4-> Update  Records".center(120))
    print("5-> Transactions has to be done from the accounts".center(120))
    print("6-> Exit".center(110))
    print("*"*114)

def menusort():
    print("       2.a-> Sort as per Account number".center(120))
    print("       2.b-> Sort as per name".center(120))
    print("       2.c-> Sort as per Amount".center(120))
    print("       2.d-> back".center(120))

def transaction():
    print("       5.a-> credit".center(120))
    print("       5.b-> debit/withdraw".center(120))
    print("       5.c-> back".center(120))

def create():
    try:
        mc.execute("create table Details(number integer(5), name varchar(40), Email varchar(100), Country varchar(50),Amount float(5))")
        insert()
    except:
        insert()

def insert():
    while True:
        acc=int(input("Enter account no: "))
        name=input("Enter name: ")
        email=input("Enter Email address: ")
        country=input("Enter Country name: ")
        bal=float(input("Enter Balance: "))
        rec=[acc,name,email,country,bal]
        ini="insert into details values(%s,%s,%s,%s,%s)"
        mc.execute(ini,rec)
        db.commit()
        a=input("Do you want to enter more records(Y/N): ")
        if a=="N" or a=="n":
            menu()
        
def display_sname():
    try:
        ini="select * from details order by name"
        mc.execute(ini)
        F="%15s %15s %15s %15s %15s"
        print(F%("number","name","email","country","amount"))
        print("="*100)
        for i in mc:
            for j in i:
                print("%14s" %j,end=" ")
            print()
    except:
        print("Table does not exist")

def display_saccno() :
    try:
        ini="select * from details order by number"
        mc.execute(ini)
        F="%15s %15s %15s %15s %15s"
        print(F%("number","name","email","country","amount"))
        print("="*70)
        for i in mc:
            for j in i:
                print("%14s" %j,end=" ")
            print()
        print("="*70)
    except:
        print("Table does not exist")

def display_sbalance():
    try:
        ini="select * from details order by amount"
        mc.execute(ini)
        F="%15s %15s %15s %15s %15s"
        print(F%("number","name","email","country","amount"))
        print("="*100)
        for i in mc:
            for j in i:
                print("%14s" %j,end=" ")
            print()
    except:
        print("Table does not exist")

def search():
    try:
        ini="select * from details"
        mc.execute(ini)
        a=int(input("Enter the account number to be searched: "))
        for i in mc:
            if i[0]==a:
                print("="*70)
                F="%15s %15s %15s %15s %15s"
                print(F%("number","name","email","country","amount"))
                print("="*70)
                for j in i:
                    print("%15s" %j,end=" ")
                print()
                break
           # else:
             #   print("Record not found")
    except:
        print("Table does not exist")

def update():
    ini="select * from details"
    mc.execute(ini)
    a=int(input("Enter the account no, whose details have to be changed"))
    for i in mc:
        i=list(i)
        if i[0]==a:
            ch=input("Do you want to Change name(Y/N): ")
            if ch=="Y" or ch=="y":
                i[1]=input("ENTER NAME: ")

            ch=input("Do you want to Mail id(Y/N): ")
            if ch=="Y" or ch=="y":
                i[2]=input("ENTER email adress: ")
            ini="UPDATE details SET name=%s,email=%s  WHERE number=%s"
            v=(i[1],i[2],i[0])
            mc.execute(ini,v)
            db.commit()
            print("ACCOUNT UPDATED")
            break
        else:
            print("Record not found")

def debit():
    ini="select * from details"
    mc.execute(ini)
    print("Please note rupees 5000 has to be kept as minimum balance")
    a=int(input("Enter the account no, from which amount has to be debited: "))
    for i in mc:
        i=list(i)
        if i[0]==a:
            b=float(input("Enter the amount that has to be withdrawn"))
            if i[4]-b>5000:
                i[4]-=b
                ini="UPDATE details set amount=%s WHERE number=%s"
                v=(i[4],i[0])
                mc.execute(ini,v)
                db.commit()
                print("Amount debited")
                break
            else:
                print("rupees 5000 has to be kept as minimum balance")
        else:
            print("Record not found")

def credit():
    ini="select * from details"
    mc.execute(ini)
    a=float(input("Enter the account no, from which amount has to be credited: "))
    for i in mc:
        i=list(i)
        if i[0]==a:
            b=float(input("Enter the amount that has to be credited"))
            i[4]+=a
            ini="UPDATE details set amount=%s WHERE number=%s"
            v=(i[4],i[0])
            mc.execute(ini,v)
            db.commit()
            print("Amount credited")
            break
        else:
            print("Record not found")
            
    
a=0
while (a!=6):
    menu()
    a=int(input("ENTER YOUR CHOICE (1/2/3/4/5/6): "))
    if a>6:
        print("INVALID CHOICE")
    if a==1:
       create()
    elif a==2:
        while True:
            menusort()
            f=input("enter a choice(a,b,c,d): ")
            if f=="a":
                display_saccno()
            elif f=="b":
                display_sname()
            elif f=="c":
                display_sbalance()
            else:
                break
    elif a==3:
        search()
    elif a==4:
        update()
    elif a==5:
        while True:
            transaction()
            f=input("enter a choice(a,b,c,d): ")
            if f=="a":
                credit()
            elif f=="b":
                debit()
            else:
                break
    if a==6:
         print("SUCCESSFULLY COMPLETED")
         print("*"*114)
