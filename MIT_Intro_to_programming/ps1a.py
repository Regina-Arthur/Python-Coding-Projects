## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Please enter your yearly salary: \n"))
portion_saved = float(input("Please enter the portion of your salary that you saved: \n"))
cost_of_dream_home = float(input("Please enter the cost of your dream home: \n"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

amount_saved = portion_saved * yearly_salary
portion_down_payment = 0.25
r = 0.05 
annual_return = amount_saved * (r/12)


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
