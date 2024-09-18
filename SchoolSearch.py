import time

# функція головного меню
def main_menu():
        print("----------Menu----------")
        print("Student")
        print("Teacher")
        print("Classroom")
        print("Bus")
        print("Quit")
        print("------------------------")
        
        option = input("Choose one from the suggested options(e.g S(tudent)): ").upper() 
    
        return option
        
#функція для введення інформації(прізвища, автобусного маршруту тд.)        
def school_search(option,F1):
    
    #В цю функцію передається вибір(option) з головного меню, і за допомогою if statement викликаються окремі функції для виведення шуканої інформації
    
    if(option == "S"):
        surname = input("Enter student's surname: ").upper()
        print("Would you like to find all details or only bus number based on entered surname?")
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
    else:
        print("\nUnknown option. Try Again.\n")
        main_menu()
               
#Функція, котра виводить інформацію базуючись на введенному прізвищі студента       
def surname_search(fileName, studentSurname, subOption):
    st = time.time() #відлік початку виконання подальшого коду функції
    with open(fileName, "rt") as f:  #відкриття текстового файлу students.txt в моді читання 
        for x in f: #цикл, що проходить кожний рядок файлу
            if studentSurname.strip() in x: 
                    values = x.split(",")  #збереження прізвища, імені, класу і тд поточного рядка, як елементи листа 
                    if(subOption == "1"):
                        #values[цифра] дає мені доступ до конкретного елементу листа, для того щоб вивести на екран шукану інформацію
                        print("Student: " + values[0]+ " " + values [1]) 
                        print("Bus: " + values[4])
                        print("Grade: " + values[2])
                        if(values[3] == 0):
                            print("Kindergarden")  #якщо клас дорівнює нулю, дитина не відвідує школу
                        else:
                            print("Classroom: " + values[3])
                        print("Teacher: " + values[5]+ " " + values [6])
                        print("\n")
                    else:
                        print("Student: " + values[0]+ " " + values [1])
                        print("Bus: " + values[4])
                        print("\n")
                        
        elapsed_real_time(st) #виклик функції, що вираховує час за котрий виконується запрос
                    
                   
#Подальші функцію працюють по такому самому принципу що й surname_search() але виводиться інша інформація з листу values               
                   
#Функція, котра виводить інформацію про студентів базуючись на введенному прізвищі вчителя     
def teacher_search(fileName, teacherSurname):
    st = time.time()
    print("\nList of " + teacherSurname +"'s students:")
    with open(fileName, "rt") as f:
        lines = f.readlines()
        for x in lines:
            if teacherSurname.strip() in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
        elapsed_real_time(st)


#Функція, котра виводить інформацію про студентів базуючись на введенному автобусному маршруті    
def bus_search(fileName, busNumber):
    st = time.time()
    if (busNumber == 0):
        print("\nList of students who don't use a bus: ")
        with open(fileName, "rt") as f:
            for x in f:
                if busNumber in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
                    print("Classroom: " + values[3])
    else:
        print("\nBus: "+ busNumber)
        with open(fileName, "rt") as f:
            for x in f:
                if busNumber in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
                    print("Classroom: " + values[3])        
            
    elapsed_real_time(st)
                
          
          
#Функція, котра виводить інформацію про студентів базуючись на введенному класі студента            
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
                         
#Функція, що вираховує час виконання і процесу функцій
       
def elapsed_real_time(startTime): #передається стартовий час з поточної функції
    endTime = time.time() #зберігається нинішний час в змінній endTime
    elapsed_time = endTime - startTime #вираховування часу віднімаючи від нинішнього часу початковий
    print('\nExecution time:', elapsed_time, 'seconds')  #виведення часу
    
 

F1 = 'students.txt' #зберігання імені файлу в змінній F1
#Цикл буде виконуватися поки Q(uit) не буде введеним 
while(True):
    option = main_menu() #виклик головного меню
    if option == "Q":
        break
    else:
        school_search(option,F1) 
       
