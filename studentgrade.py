#Brody Rines
#studentgrade.py
#My app will determine if a student made it to the deans list, the honor or, or neither

studentName = 0
gpa = 0
deanList = 3.5
honorRoll = 3.25


while True:
    print("Enter Student's Name:")
    studentName = input()

    if (studentName == "ZZZ"):
        print("Done with program")
        break
    print("Enter students G.P.A")
    gpa = float(input())
     
    if gpa >= deanList: 
        print("You made it on the Dean's List!")
    elif gpa >= honorRoll:
        print("You made it on the Honor Roll List!")
    elif gpa < honorRoll:
        print("I'm sorry, you have not made it on any list.")
    

