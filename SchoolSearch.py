import time

def main_menu():
        print("----------Menu----------")
        print("Choose one of the following options: ")
        print("Student")
        print("Teacher")
        print("Classroom")
        print("Bus")
        print("Quit")
        print("------------------------")
        
        option = input("Choose one from the suggested options(e.g S(tudent)): ").upper()
    
        return option
        
        
def school_search(option,F1):
    if(option == "S"):
        surname = input("Enter student's surname: ").upper()
        print("Would you like to find all details or only bus number based on entered surname ?")
        print("1. Find all details\n2. Find bus number")
        subOption = input(("Enter 1 or 2: "))
        if (subOption == "1" or subOption == "2"):
            surname_search(F1,surname, subOption)
        else:
            print("Invalid option. Try again")
    elif (option == "T"):
        surname = input("Enter teacher's surname: ").upper()
        teacher_search(F1,surname)
    elif (option == "B"):
        busNumber = input("Enter bus number: ")
        bus_search(F1, busNumber)
    elif (option == "C"):
        classromNumber = input("Enter classroom number: ")
        print("Classroom: ", classromNumber)
        classroom_search(F1, classromNumber)
    elif(option == "G"):
        gradeNumber = input("Enter grade: ")
        print("Grade: ", gradeNumber)
        bus_search(F1, gradeNumber)
    else:
        print("\nUnknown option. Try Again.\n")
        main_menu()
               
        
def surname_search(fileName, studentSurname, subOption):
    st = time.time()
    with open(fileName, "rt") as f:
        for x in f:
            if studentSurname.strip() in x:
                    values = x.split(",")
                    if(subOption == "1"):
                        print("Student: " + values[0]+ " " + values [1])
                        print("Bus: " + values[4])
                        print("Classroom: " + values[3])
                        print("Teacher: " + values[5]+ " " + values [6])
                        print("\n")
                    else:
                        print("Student: " + values[0]+ " " + values [1])
                        print("Bus: " + values[4])
                        print("\n")
                        
        elapsed_real_time(st)
                    
                   
    
def teacher_search(fileName, teacherSurname):
    st = time.time()
    with open(fileName, "rt") as f:
        lines = f.readlines()
        for x in lines:
            if teacherSurname.strip() in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
        elapsed_real_time(st)


def bus_search(fileName, busNumber):
    st = time.time()
    with open(fileName, "rt") as f:
        for x in f:
            if busNumber in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
        elapsed_real_time(st)
                
          
          
def classroom_search(fileName, classromNumber):
    st = time.time()
    with open(fileName, "rt") as f:
        for x in f:
            if classromNumber in x:
                    values = x.split(",")
                    if(classromNumber == "0"):
                        print("Student: " + values[0]+ " " + values [1])
                        print("Kindergarden")
                    else:
                       print("Student: " + values[0]+ " " + values [1])
                       print("Classroom: " + values[3])
        elapsed_real_time(st)       
                       

def grade_search(fileName, gradeNum):
    st = time.time()
    with open(fileName, "rt") as f:
        for x in f:
            if gradeNum in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
        elapsed_real_time(st)   
        

def elapsed_real_time(startTime):
    endTime = time.time()
    elapsed_time = endTime - startTime
    print('\nExecution time:', elapsed_time.round(2), 'seconds')  
    
 

F1 = 'students.txt'
while(True):
    option = main_menu()
    if option == "Q":
        break
    else:
        school_search(option,F1)
       
