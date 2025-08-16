## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Please enter your yearly salary: \n"))
portion_saved = float(input("Please enter the portion of your salary that you saved in decimal form: \n"))
cost_of_dream_home = float(input("Please enter the cost of your dream home: \n"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

monthly_salary = yearly_salary / 12.0 #Users monthly salary
portion_down_payment = 0.25
cost_of_down_payment = cost_of_dream_home * portion_down_payment #Actual cost of down payment
amount_saved = 0
r = 0.05 
annual_return = amount_saved * (r/12)
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved != cost_of_down_payment:
    if months > 0:
        monthly_salary += monthly_salary * 0.1

    else:
        monthly_salary = monthly_salary
    
    amount_saved += monthly_salary * portion_saved
    annual_return = amount_saved * (r/12)
    amount_saved += annual_return
    months += 1 
        


