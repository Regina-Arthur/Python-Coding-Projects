#Greet users and ask for intent to use the system
print ('Welcome, you can enter student grades for your course.')
go_ahead = input ('Would you like to enter student grades?(yes/no)\n')

#confirm intent to use the system
if go_ahead.upper() == "YES":

    course = input("Please enter the course name: ")
    number_students = int(input("How many students will you be entering?"))
    
    student_name = {}
    for students in range(number_students):
        print("""Please enter the student name, you will later be asked to enter their grade. 
            This will be done one after the other until all student information has been entered.
            Do not worry about errors, you will be allowed to correct that later.""")
        student = input("Enter a student's name please: ")
        student_name["student"] = int(input("Please enter their grade: "))

elif go_ahead.upper() == "NO":
    print("We will be here when you need us.")

else:
    print("Please enter a valid prompt.")


    
#Initize an empty list to store students data

#Start data entry loop

#Calculate grade for the score

#Store student record in the list

#Data entry and calculation of class average

#Display table of student data
 
#Display class average