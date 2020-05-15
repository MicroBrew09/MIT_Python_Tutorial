import numpy as np
#Initialize Variables and Get User Input:
annual_salary = float(input("Enter your annual salary:"))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:​")) 
semi_annual_raise =float(input("Enter the semi­annual raise, as a decimal:​"))
portion_down_payment = 0.25*(total_cost)
r=0.04/12
cost = total_cost-portion_down_payment
current_savings = 0
n = 0
remaining_payment=portion_down_payment
amt =0
while remaining_payment > current_savings:
    n = n+1
    monthly_saving = portion_saved*annual_salary/12
    amt = current_savings*r
    current_savings = current_savings+monthly_saving+amt
    if n%6 == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)
        
print("Number of months:​",n)