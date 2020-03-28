#PART B:SAVING, WITH A RAISE
total_cost=float(input("Enter The total cost of the house:"))
annual_salary=float(input("Enter your annual salary:"))
semi_annual_raise=float(input("Enter your semi annual raise(MUST BE DECIMAL): "))
portion_saved=float(input("Enter the portion saved of your salary(MUST BE DECIMAL):"))
monthly_salary=annual_salary/12
current_savings=0.0
months=0
while current_savings < .25*total_cost : 
    invesment= (current_savings*.04)/12
    current_savings += invesment + (portion_saved*monthly_salary)
    months+=1
    if months%6==0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary =(annual_salary/12)
    
print (" YOU HAVE MADE IT! IT TOOK YOU " , months , "months")
    