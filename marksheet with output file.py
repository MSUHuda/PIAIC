import csv
print ("Marksheet")
name = str(input("Please enter your name"))
Roll_Num = "12345"
Class = "12th"
print ("Name:" +name)
print ("Roll Number:" +Roll_Num)
print ("Class:" +Class)
Eng_marks = int(input("please enter english marks:"))
Urdu_marks = int(input("please enter urdu marks:"))
Math_marks = int(input("please enter math marks:"))
Phy_marks = int(input("please enter physics marks:"))
CompSc_marks = int(input("please enter compsc marks:"))
Total_Marks = 500
print ("Total Marks = 500")
obt_marks = int(Eng_marks + Urdu_marks + Math_marks + Phy_marks + CompSc_marks)
print ("Obtained Marks:" +str(obt_marks))
Perc = int(obt_marks)/(Total_Marks)*100
print ("Percentage:" +str(Perc) +" %")
if Perc>= 95:
    print ("Grade 'A*'")
elif Perc>=85 and Perc<=94:
    print ("Grade 'A'")
elif Perc>=75 and Perc<=84:
    print ("Grade 'B'")
elif Perc>=65 and Perc<=74:
    print ("Grade 'C'")
elif Perc>=55 and Perc<=64:
    print ("Grade 'D'")
elif Perc>=45 and Perc<=54:
    print ("Grade 'E'")
elif Perc<=44:
    print ("Grade 'F'")
userData = [name,Roll_Num,Class,Eng_marks,Urdu_marks,Math_marks,Phy_marks,CompSc_marks,Total_Marks,obt_marks,Perc]
with open("Marksheet.csv","w" ,newline="") as f:

        file_handler = csv.writer(f, delimiter=',')    
        
        file_handler.writerow(["Name","Roll_Num","Class","English","Urdu","Math","Physics","CompSc","Obtained Marks","Total Marks","Percentage"])
        file_handler.writerow(userData)
