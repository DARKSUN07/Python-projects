#importing modules
from tkinter import*
import random
from random import choice

answer=""

#function of the whole quiz
def body():
    
    myButton.config(state="disabled")
    
    #assigning random variables for key
    a=random.randrange(0,9)
    b=choice([i for i in range(0,9) if i not in [a]])
    c=choice([i for i in range(0,9) if i not in [a,b]])
    z=choice([i for i in range(0,9) if i not in [a,b,c]])

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
    

    #asking for difficulty level
    myLabel2=Label(root, text="Enter difficulty from 1 to 3: ",pady="20")
    myLabel2.pack()
    entry=Entry(root)
    entry.pack()
    
    
    def dif():

        global answer
        
        myButton2.config(state="disabled")
        
        dif=entry.get()
        myLabel3=Label(root, text="  ")
        myLabel3.pack()
        if dif=="1":
            ans=a_s+b_s+c_s
            answer=ans
            num=random.randrange(1,3)
            if num==1:
                #Level 1.1
                myLabel4=Label(root, text=ans)
                myLabel4.pack()
                h1=["Hint:",d,g,f," Nothing is right\n"]
                h2=["Hint:",a,e,b," Two digits are right but only one is well placed\n"]
                h3=["Hint:",c,b,d," Two digits are right but only one is well placed\n"]
                h4=["Hint:",c,e,b," Two digits are right but wrongly placed\n"]
                list=[h1,h2,h3,h4]
                random.shuffle(list)
                myText=Text(root,height="4")
                myText.pack()
                for i in list:
                    for j in i:
                        myText.insert(END,j)

            elif num==2:
                #Level 1.2
                myLabel4=Label(root, text=ans)
                myLabel4.pack()
                h1=["Hint:",d,e,c," One digit is right and well placed\n"]
                h2=["Hint:",d,f,b," One digit is right but wrongly placed\n"]
                h3=["Hint:",c,a,d," Two digits are right but wrongly placed\n"]
                h4=["Hint:",g,h,e," Nothing is right\n"]
                h5=["Hint:",h,e,a," One digit is right but wrongly placed\n"]
                list=[h1,h2,h3,h4,h5]
                random.shuffle(list)
                myText=Text(root,height="5")
                myText.pack()
                for i in list:
                    for j in i:
                        myText.insert(END,j)

        elif dif=="2":
            ans=a_s+b_s+c_s
            answer=ans
            myLabel4=Label(root, text=ans)
            myLabel4.pack()
            #Level 2
            h1=["Hint:",d,b,g," One digit is right and well placed\n"]
            h2=["Hint:",d,c,e," One digit is right but wrongly placed\n"]
            h3=["Hint:",c,h,a," Two digits are right but wrongly placed\n"]
            h4=["Hint:",e,choice([i for i in range(0,10) if i not in [a,b,c,d,e]]),choice([i for i in range(0,10) if i not in [a,b,c,d,e,f,g,h]])," Nothing is right\n"]
            h5=["Hint:",e,f,b," One digit right but wrongly placed\n"]
            list=[h1,h2,h3,h4,h5]
            random.shuffle(list)
            myText=Text(root,height="5")
            myText.pack()
            for i in list:
                for j in i:
                    myText.insert(END,j)

        elif dif=="3":
            ans=a_s+b_s+c_s+z_s
            answer=ans
            myLabel4=Label(root, text=ans)
            myLabel4.pack()
            num=random.randrange(1,3)
            if num==1:
                #Level 3.1
                h1=["Hint:",d,e,b,f," One digit is correct but wrongly placed\n"]
                h2=["Hint:",z,d,a,g," Two digit are right but wrongly placed\n"]
                h3=["Hint:",f,e,h,z," One digit is right and well placed\n"]
                h4=["Hint:",choice([i for i in range(0,10) if i not in [a,b,c,d,e,z,f,g,h]]),f,h,g," Nothng is correct\n"]
                h5=["Hint:",b,f,e,c," Two digit are right but wrongly placed\n"]
                list=[h1,h2,h3,h4,h5]
                random.shuffle(list)
                myText=Text(root,height="5")
                myText.pack()
                for i in list:
                    for j in i:
                        myText.insert(END,j)


            elif num==2:
                myLabel4=Label(root, text=ans)
                myLabel4.pack()
                num=random.randrange(1,3)
                #level 3.2
                h1=["Hint:",d,z,e,c," Two digit are correct but wrongly placed"]
                h2=["Hint:",f,c,g,z," Two digit are right but only one is well placed"]
                h3=["Hint:",a,g,z,h," Two digit are right but only one is well placed"]
                h4=["Hint:",h,b,f,c," Two digit are right but only one is well placed"]
                h5=["Hint:",c,f,a,b," Three digit are right but wrongly placed"]
                list=[h1,h2,h3,h4,h5]
                random.shuffle(list)
                myText=Text(root,height="5")
                myText.pack()
                for i in list:
                        for j in i:
                            myText.insert(END,j)

        else:
            myLabel4=Label(root, text="You Entered Wrong difficulty")
            myLabel4.pack()
            quit()


        myLabel5=Label(root, text="  ")
        myLabel5.pack()
        
        myLabel6=Label(root, text="Enter your answer below")
        myLabel6.pack()
        
        myLabel7=Label(root, text="  ")
        myLabel7.pack()
        
        entry2=Entry(root)
        entry2.pack()

        myLabel8=Label(root, text="  ")
        myLabel8.pack()

        def ans():

            global answer
            
            myButton3.config(state="disabled")
            
            fans=entry2.get()
            myLabel=Label(root)
            myLabel.pack()
            #checking ans
            if fans==answer:
                myLabel2=Label(root, text="YOU OPENED THE LOCK\nヽ(^o^)ノ")
                myLabel2.pack()
            else:
                myLabel2=Label(root, text="YOU FAILED TO OPEN THE LOCK\nヽ(ヅ)ノ")
                myLabel2.pack()        
            
            
        
        myButton3=Button(root, text="Enter",command=ans,padx="30",pady="10",fg="white",bg="#2A2A2A")
        myButton3.pack()

        
                            
                

        
    myLabel3=Label(root, text="  ")
    myLabel3.pack()
    myButton2=Button(root, text="Enter",command=dif,padx="30",pady="10",fg="white",bg="#2A2A2A")
    myButton2.pack()
    
    
    
    
    
    

root=Tk()


myButton=Button(root, text="Start",command=body,padx="30",pady="10",fg="white",bg="#2A2A2A")
myLabel1=Label(root, text="This is a quiz game,In this game you have to open a password protected lock. You have only one key code to open it\nYou will be given hints, If you write the correct key\n! YOU WIN !\nIf you type the wrong key\n! YOU LOOSE !\nPress start to start the game",pady="30")
myLabel1.pack()
myButton.pack()


root.mainloop()

