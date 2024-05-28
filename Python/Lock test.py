#importing modules
import random
from random import choice

def body():
    #assigning random variables for key
    a=random.randrange(0,9)
    b=choice([i for i in range(0,9) if i not in [a]])
    c=choice([i for i in range(0,9) if i not in [a,b]])
    z=choice([i for i in range(0,9) if i not in [a,b,c]])

    #asking for difficulty level
    print("--------------------------------------------------------------------------------------")
    dif=int(input("Enter difficulty from 1 to 3: "))
    print("--------------------------------------------------------------------------------------")

    #assigning other random variables
    d=choice([i for i in range(0,10) if i not in [a,b,c,z]])
    e=choice([i for i in range(0,10) if i not in [a,b,c,d,z]])
    f=choice([i for i in range(0,10) if i not in [a,b,c,d,e,z]])
    g=choice([i for i in range(0,10) if i not in [a,b,c,d,e,z,f]])
    h=choice([i for i in range(0,10) if i not in [a,b,c,d,e,z,f,g]])

    #creating string for key to get 0's in start
    a_s=str(a)
    b_s=str(b)
    c_s=str(c)
    z_s=str(z)
    if dif==1:
        ans=a_s+b_s+c_s

        num=random.randrange(1,3)
        if num==1:
            #Level 1.1
            print(ans)
            h1=["Hint:",d,g,f," Nothing is right"]
            h2=["Hint:",a,e,b," Two digits are right and but only one is well placed"]
            h3=["Hint:",c,b,d," Two digits are right and but only one is well placed"]
            h4=["Hint:",c,e,b," Two digits are right and but wrongly placed"]
            list=[h1,h2,h3,h4]
            random.shuffle(list)
            for i in list:
                for j in i:
                    print(j,end=" ")
                print("")
            

        if num==2:
            #Level 1.2
            print(ans)
            h1=["Hint:",d,e,c," One digit is right and well placed"]
            h2=["Hint:",d,f,b," One digit is right but wrongly placed"]
            h3=["Hint:",c,a,d," Two digits are right and but wrongly placed"]
            h4=["Hint:",g,h,e," Nothing is right"]
            h5=["Hint:",h,e,a," One digit is right but wrongly placed"]
            list=[h1,h2,h3,h4,h5]
            random.shuffle(list)
            for i in list:
                for j in i:
                    print(j,end=" ")
                print("")

    elif dif==2:
        ans=a_s+b_s+c_s
        #Level 2
        print(ans)
        h1=["Hint:",d,b,g," One digit is right and well placed"]
        h2=["Hint:",d,c,e," One digit is right but wrongly placed"]
        h3=["Hint:",c,h,a," Two digits are right but wrongly placed"]
        h4=["Hint:",e,choice([i for i in range(0,10) if i not in [a,b,c,d,e]]),choice([i for i in range(0,10) if i not in [a,b,c,d,e,f,g,h]])," Nothing is right"]
        h5=["Hint:",e,f,b," One digit right but wrongly placed"]
        list=[h1,h2,h3,h4,h5]
        random.shuffle(list)
        for i in list:
            for j in i:
                print(j,end=" ")
            print("")

    elif dif==3:
        ans=a_s+b_s+c_s+z_s

        num=random.randrange(1,3)
        if num==1:
            #Level 3.1
            #print(ans)
            h1=["Hint:",d,e,b,f," One digit is correct but wrongly placed"]
            h2=["Hint:",z,d,a,g," Two digit are right but wrongly placed"]
            h3=["Hint:",f,e,h,z," One digit is right and well placed"]
            h4=["Hint:",choice([i for i in range(0,10) if i not in [a,b,c,d,e,z,f,g,h]]),f,h,g," Nothng is correct"]
            h5=["Hint:",b,f,e,c," Two digit are right but wrongly placed"]
            list=[h1,h2,h3,h4,h5]
            random.shuffle(list)
            for i in list:
                for j in i:
                    print(j,end=" ")
                print("")

        elif num==2:

            #level 3.2
            #print(ans)
            h1=["H1:",d,z,e,c," Two digit are correct but wrongly placed"]
            h2=["H2:",f,c,g,z," Two digit are right but only one is well placed"]
            h3=["H3:",a,g,z,h," Two digit are right but only one is well placed"]
            h4=["H4:",h,b,f,c," Two digit are right but only one is well placed"]
            h5=["H5:",c,f,a,b," Three digit are right but wrongly placed"]
            list=[h1,h2,h3,h4,h5]
            random.shuffle(list)
            for i in list:
                for j in i:
                    print(j,end=" ")
                print("")

    else:
        print("You Entered Wrong difficulty")
        exit()

    #checking ans
    fans=input("Enter your ans: ")
    if fans==ans:
        print("Your ans is correct")
        print("--------------------------------------------------------------------------------------")
    else:
        print("Your ans is wrong\nCorrect ans is:",ans)
        print("--------------------------------------------------------------------------------------")
        
    start=input("Do you wish to play again\nIf yes then type yes or type no: ")
    if start=="yes":
        body()
    elif start=="no":
        print("Thank You")
    else:
        print("Wrong input")

#about game
print("This is a quiz game\nIn this game you have to open a password protected lock\nYou have only one key code to open it\nYou will be given hints\nIf you write the correct key\n! YOU WIN !")
print("If you type the wrong key\n! YOU LOOSE ! ")
start=input("If you want to start type yes else type no: ")
if start=="yes":
    body()
elif start=="no":
    print("Thank You")
else:
    print("Wrong input")

