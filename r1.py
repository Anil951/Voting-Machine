import os
from time import sleep
import pwinput,csv



def welcome():
    print("""            ______________________________________________
            |                                             |
            |            WELCOME TO ELECTIONS             |
            |                                             |
            |_____________________________________________|""")

    input("                        [press enter to proceed]")
    
    os.system('cls')

def signup():
    while True:
        username=input("enter username:")
        password=pwinput.pwinput("enter password:",'*')
        with open("signup.csv","r") as su: #su=sign up
            ru=csv.reader(su)
            for j in ru: #ru=read in sign up(su)
                if(j[0]==username):
                    print("name already taken..try another one.....")
                    break
            else:
                with open("signup.csv","a+",newline='') as su:
                    su1=csv.writer(su)    #su1=object in su for writing into  su file
                    det=[username,password] #det=details
                    su1.writerow(det)
                break
    print("_______NOW SIGN-IN AND PROCEED TO VOTE_______")
    sleep(2)
    os.system('cls')


def signin():
    flag=False
    while True:
        cusername=input("enter username:") #c=confirm
        cpassword=pwinput.pwinput("enter password:",'*')
        with open("signup.csv","r") as su:
            ru1=csv.reader(su)
            for k in ru1:
                if(k[0]==cusername and k[1]==cpassword):
                    print("\nSUCCESSFULLY SIGNED IN___THANK YOU :)")
                    sleep(2)
                    flag=True
                    break
            else:
                sleep(1.5)
                os.system('cls')
                print("INCORRECT MATCH____TRY AGAIN :|\n")
        if flag==True:
            break
    os.system('cls')

def castvote():
    
    while True:
        print("""             ______________________________________
                |___________CAST YOUR VOTE____________|
                |_____________________________________|\n""")
        print("LIST OF PARTICIPATING CANDITATES :")
        print("_______________________________")
        print("CANDITATE 1 -- SYMBOL '@'")
        print("CANDITATE 2 -- SYMBOL '#'")
        print("CANDITATE 3 -- SYMBOL '$'")
        print("CANDITATE 4 -- SYMBOL '&'")
        print("NOTA --  ANY OTHER SYMBOL")
        print("_______________________________")
        print("TO CAST YOUR VOTE PLEASE TYPE THE RESPECTIVE SYMBOL MENTIONED AS ABOVE\n")
        choice=input("enter choice:")
        choice1=input("VERIFICATION--\nagain enter choice:")
        if choice==choice1: 
            print("____________ THANKS FOR VOTING____________")
            break
        else:
            print("VERFICATION FAILED----TRY AGAIN")
    with open("votecount.csv","r") as f:
        f1=csv.reader(f)
        d=[]
        for i in f1:
            for x in i:
                d.append(int(x))    
            if(choice=='@'):
                d[0]+=1
            elif(choice=='#'):
                d[1]+=1
            elif(choice=='$'):
                d[2]+=1
            elif(choice=='&'):
                d[3]+=1
            else:
                d[4]+=1
        with open("votecount.csv","w",newline='') as f:
            f2=csv.writer(f)  
            f2.writerow(d)


def livecount():
    print("[@,#,$,&,NOTA]")
    with open("votecount.csv","r") as f:
        f2=csv.reader(f)  
        for i in f2:
            print(i,end='')
            print('\n')



welcome()
while True:
    opt=int(input("press '1' to sign up\npress '2' to sign in\nenter option:"))
    os.system('cls')
    if opt==1:
        signup()
    elif opt==2:
        signin()
        break
    else:
        print('WRONG INPUT.....TRY AGAIN')
while True:
    print("1 to cast vote\n2 to see live counting\n3 to exit")
    opt=int(input("enter option:"))
    
    if(opt==1):
        castvote()
    elif(opt==2):
        livecount()
    elif(opt==3):
        print("""                      ______________________________________________
                     |                                             |
                     |          SEE YOU AFTER RESULTS (^_^)        |
                     |                                             |
                     |_____________________________________________|""");
        break
    else:
        print("wrong option given___TRY AGAIN :|")