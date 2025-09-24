#Greet users and ask for intent to use the system
print ('Welcome, you can enter student grades for your course.')
go_ahead = input ('Would you like to enter student grades?(yes/no) ')

#confirm intent to use the system
if go_ahead.upper() == "YES":
    start = 1
elif go_ahead.upper() == "NO":
    start = 0
else:
    print("Please enter a valid prompt.")

while start == 1:
    student_name = ()
    
    course = input("Please enter the course name: ")
    number_students = int(input("How many students will you be entering?"))
    for students in number_students:
        print("""Please enter the student name, you will later be asked to enter their grade. 
              This will be done one after the other until all student information has been entered.
              Do not worry about errors, you will be allowed to correct that later.""")
        student = input("Enter a student's name please: ")
        student_name.student = int(input("Please enter their grade: "))




    
#Initize an empty list to store students data

#Start data entry loop

#Calculate grade for the score

#Store student record in the list

#Data entry and calculation of class average

#Display table of student data
 
#Display class average