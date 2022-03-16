#sql database will be made directly on linking
#first sign-in as admin and add voters
#then sign-up as voter and entries will be updated in in the database 
#finally the the voter can login and vote

#this is a menu driven program

#mysql will be connected to the local host on changing credentials

# master password for admin is:
#'smriddhi'


import mysql.connector
mydb=mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="smriddhi"
          )
mycursor=mydb.cursor()
mycursor.execute("create database if not exists vote")


import sys

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="smriddhi",
    database="vote")

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS admin(admin_id int(5) primary key,admin_name varchar(20),password varchar(10))")

mycursor.execute("CREATE TABLE IF NOT EXISTS voter(voting_number varchar(20) primary key,voter_name varchar(20), age int(2))")

mycursor.execute("create table if not exists houses(prahlad int, shravan int, dhruv int, eklavya int)")

#------------------------------------------------------------------------------------------
#This menu is shown to the voter/admin upon initiation of the program.
#It allows voter/admin to login or sign up
#------------------------------------------------------------------------------------------

def main_menu():
    print("***WELCOME TO THE VOTING MANAGEMENT SYSTEM. PLEASE SELECT ONE OF THE FOLLOWING OPTIONS TO CONTINUE*** : \n")

    print("")
    
    print("TO LOGIN AS ADMIN ENTER 1",end="\n")

    print("")
    
    print("TO LOGIN AS VOTER ENTER 2",end="\n")

    print("")
    
    print("TO SIGN-UP ENTER 3",end="\n")

    print("")
    
    print("TO EXIT ENTER 4",end="\n")
    
    print("")

    option1=int(input("ENTER YOUR OPTION : "))
    
    print("")

    if(option1==1):
        
        return admin_login()

    elif(option1==2):
        
        return voter_login()

    elif(option1==3):
        
        return sign_up()

    else:
        
        print("^*^*^Thank you for visiting.^*^*^")

#----------------------------------------------------------------------------------
#This function allows admin to sign up(only admin can sign up)
#----------------------------------------------------------------------------------

def sign_up():

    print("To sign up as admin enter masterpassword")
    
    print("")
    
    pd=input("Enter masterpassword")
    
    print("")
    
##------------------------------------------
    #Administrator sign up
##------------------------------------------
    if(pd=="smriddhi"):
        
        print("Access authorised")
        
        name=input("Enter your Name : ")
        print("")
        
        adminid=int(input("Enter your ID(numeric) : "))
        print("")
        
        password=input("Enter your Password(alphanumeric) : ")
        
        print("")

        input_val=(name,adminid,password)
        
        admin_new="INSERT INTO admin(admin_name,admin_id ,password)VALUES(%s,%s,%s)"
        

        mycursor.execute(admin_new,input_val)
        
        mydb.commit()
        
        print("Account created successfully")
        
        print("")
        
        return main_menu()
    
    else:
        
        print ("ACCESS DENIED; RETURNING TO MAIN MENU")
        print ("")

        return main_menu()

#------------------------------------------------------
#This function allows administator to login
#------------------------------------------------------

def admin_login():
    
    admin_id=int(input("Enter your ADMIN ID : "))

    print("")
    
    password=input("Enter your PASSWORD : ")
    
    print("")

    mycursor.execute("SELECT * FROM admin")
    
    check1=mycursor.fetchall()

    
    for y in range(0,len(check1)):
        
        if(check1[y][0]==admin_id and check1[y][2]==password):
            
            print("LOGIN SUCCESSFUL")
            
            print("")

            print ("Access Authorised,Welcome to administration of Voting Management System",check1[y][1])
            
            return admin_menu(admin_id,check1[y][1])

        
        elif(check1[y][0]==admin_id and check1[y][2]!=password):
            
            print("**PASSWORD INCCORECT.TRY AGAIN**")
            
            print("")
            
            return admin_login()

    #Incorrect admin_id(admin does not exist)
        
    print("admin not found",end="\n")
    
    print("Press 1 to to return to admin login",end="\n")
    
    print("Press 2 to return to main menu",end="\n")
    
    print("")

    option2=int(input("Enter your choice"))
    
    print("")

    if(option2==1):
        
        return admin_login()

    else:
        
        return main_menu()
    
#------------------------------------------------------
## This function allows the Voter to Login
#------------------------------------------------------

def voter_login():
    vo=input("Enter your voting Number")
    name=input("Enter your name")
    print ("")
    mycursor.execute("Select * from voter")
    check4=mycursor.fetchall()
    for y in range(0,len(check4)):
        
        if(check4[y][0]==vo and check4[y][1]==name):
            
            print("LOGIN SUCCESSFUL")
            
            print("")

            return voter_menu(vo,name) 
        
        elif(check4[y][0]!=vo and check4[y][2]==name):
            
            print("** VOTING NUMBER INCORECT.TRY AGAIN**")
            
            print("")
            
            return voter_login()

    #Incorrect voting_number(user doesn't exist)
        
    print("User not found",end="\n")
    
    print("Press 1 to to return to login",end="\n")
    
    print("Press 2 to return to main menu",end="\n")
    
    print("")

    print("TO EXIT ENTER 3",end="\n")
    
    print("")

    option2=int(input("Enter your choice"))
    
    print("")

    if(option2==1):
        
        return voter_login()

    else:
        
        return main_menu()
    
     

#-------------------------------
#-----Admin Menu-----
#-------------------------------

def admin_menu(admin_id,name):


    print ("Enter 1 to ^^^ADD NEW VOTER^^^")
    print("")

    print ("Enter 2 to ^^^COUNT VOTES^^^")
    print("")

    print ("Enter 3 to ^^^RETURN TO MAIN MENU^^^")
    print("")
    option3=int(input("Enter your option:"))

    print ("")

    if (option3==1):
        return new_voter()
    
    elif (option3==2):
        return votecount()
    
    elif(option3==3):
        return main_menu()
    

#-----------------------------------------------------------------------
##This function allows the Admin to add a New Voter##
#-----------------------------------------------------------------------

def new_voter():


    voting_number=int(input("Enter voting number of voter "))

    print("")

    name=input("Enter name of the voter ")

    print("")

    age=int(input("Enter age of voter"))
    
    if (age<18):
        print("Not eligible for voting.")
   
    else:
        val=(voting_number,name,age)

        command="INSERT INTO voter(voting_number,voter_name,age) VALUES(%s,%s,%s)"

        mycursor.execute(command,val)

        mydb.commit()

        print("voter information Added")

        print("")
    
    return main_menu()


#------------------------------
#-----Voter Menu-----
#------------------------------

def voter_menu(vo,name):
    
    print ("Welcome to the Elections")
    print("")
    print ("Enter 1 to ^^^VIEW VOTING OPTIONS^^^")
    print("")
    print ("Enter 2 to ^^^RETURN TO MAIN MENU^^^")
    print("")
    
    x=int(input("Enter your choice:"))
    
    if (x==2):
        return main_menu()


    elif (x==1):
        
        print("To Vote for the following, Press the valid number")
        print("")
        print("PRAHLAD:  **Press  1**")
        print(  "")
        print("SHRAVAN:  **Press  2**")
        print("")
        print("DHRUV:  **Press  3**")
        print("")
        print("EKLAVYA:  **Press   4**")
        print("")

        

        ch=int(input("Enter your choice"))
       
        if (ch==1):
             
            val=(1,null,null,null)
            
            new="INSERT INTO houses(prahlad,shravan,dhruv,eklavya)VALUES(%s,%s,%s,%s)"
        

            mycursor.execute(new,val)
        
            mydb.commit()


        elif(ch==2): 
            
            val=(null,1,null,null)
            new="INSERT INTO houses(prahlad,shravan,dhruv,eklavya)VALUES(%s,%s,%s,%s)"

            mycursor.execute(new,val)
        
            mydb.commit()
            
        elif(ch==3):
            
            val=(null,null,1,null)
            new="INSERT INTO houses(prahlad,shravan,dhruv,eklavya)VALUES(%s,%s,%s,%s)"

            mycursor.execute(new,val)
        
            mydb.commit()
            
        elif(ch==4):
            
            val=(null,null,null,1)
            new="INSERT INTO houses(prahlad,shravan,dhruv,eklavya)VALUES(%s,%s,%s,%s)"

            mycursor.execute(new,val)
        
            mydb.commit()
    

def votecount():
    
    
    print("PRAHLAD VOTES=  ")
    
    mycursor.execute("select prahlad,count (*) from houses where prahlad=1 group by prahlad")
    check9=mycursor.fetchall()
    print(check9)
    
    print("")
    
    print("SHRAVAN =  ")
    mycursor.execute("select shravan, count (*) from houses where shravan=1 group by shravan")
    check8=mycursor.fetchall()
    print(check8)
    
    print("")
    
    print("DHRUV = ")
    mycursor.execute("select dhruv, count (*) from houses where dhruv=1 group by dhruv")
    check7=mycursor.fetchall()
    print(check7)
    
    print("")
    
    print("EKLAVYA =  ")
    mycursor.execute("select eklavya, count (*) from houses where eklavya=1 group by eklavya")
    check6=mycursor.fetchall()
    print(check6)
    

    
    
#MAIN

main_menu()
