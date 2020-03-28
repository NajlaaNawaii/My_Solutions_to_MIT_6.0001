#PART A: House Hunting
total_cost=float(input("Enter The total cost of the house:"))
annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the portion saved of your salary(MUST BE DECIMAL):"))
monthly_salary=annual_salary/12
current_savings=0.0
months=0
while current_savings < .25*total_cost :
    invesment= (current_savings*.04)/12
    current_savings += invesment + (portion_saved*monthly_salary)
    months+=1
    
print (" YOU HAVE MADE IT! IT TOOK YOU " , months , "months")
    