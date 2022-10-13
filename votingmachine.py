import csv,pwinput
import os
from time import sleep

class vm:
    voted=False
    a=[]
    u=""
    p=""

    def __init__(self):
        with open("signup.csv","r") as f: 
            f1=csv.reader(f)
            for i in f1:
                self.a.append(i)
        
    
    def signup(self):
        while True:
            u=input("username:")
            p=pwinput.pwinput("password:")
            self.u=u
            self.p=p
            with open("signup.csv","r") as su: #su=sign up
                ru=csv.reader(su)
                for j in ru: #ru=read in sign up(su)
                    if(j[0]==u):
                        print("name already taken..try another one.....")
                        break
                else:
                    break
        self.a.append([u,p,"f"])
       

    def castvote(self):
        while True:
            print("""                    ______________________________________
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
                self.voted=True
                for p in self.a:
                    if(self.u==p[0]):
                        p[2]='t'
                
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

    def addintofile(self):
        if self.voted==True:
            with open("signup.csv","w",newline='') as f:
                f1=csv.writer(f)
                for j in self.a:
                    f1.writerow(j)
                 

    def livecount(self):
        print("[@,#,$,&,NOTA]")
        with open("votecount.csv","r") as f:
            f2=csv.reader(f)  
            for i in f2:
                print(i,end='')
                print('\n') 
        



print("""            ______________________________________________
            |                                             |
            |            WELCOME TO ELECTIONS             |
            |                                             |
            |_____________________________________________|""")

input("                        [press enter to proceed]")
os.system('cls')
flag=False
v1=vm()
while True: 
    opt=input("press '1' to sign up\npress '2' to sign in\nenter option:")
    if opt=='1':
        os.system('cls')
        v1.signup()
        print("_______NOW SIGN-IN AND PROCEED TO VOTE_______")
        sleep(2)
    elif opt=='2':
        #sign in
        while True:
            u=input("username:")
            p=pwinput.pwinput("password:")
            for d in v1.a:
                if u==d[0] and p==d[1]:
                    print("\nSUCCESSFULLY SIGNED IN___THANK YOU :)")
                    sleep(2)
                    os.system('cls')
                    v1.u=u
                    v1.p=p
                    if d[2]=='t':
                        v1.voted=True
                    flag=True
                    break
            else:
                print("INCORRECT MATCH____TRY AGAIN :|\n")
            if flag==True:
                break
    else:
        print('WRONG INPUT.....TRY AGAIN')
    if flag==True:
        break

while True:
    print("1 to cast vote\n2 to see live counting\n3 to exit")
    opt=input("enter option:")
    if(opt=='1'):
        if(v1.voted==False):
            v1.castvote()
            v1.addintofile()
        else:
            print("_____________\nALREADY VOTED\n______________")
    elif(opt=='2'):
        v1.livecount()
    elif(opt=='3'):
        print("""                      ______________________________________________
                     |                                             |
                     |          SEE YOU AFTER RESULTS (^_^)        |
                     |                                             |
                     |_____________________________________________|""");
        break
    else:
        print("__________________________\nwrong option given___TRY AGAIN :\n___________________________")

