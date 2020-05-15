import numpy as np
#Initialize Variables and Get User Input:
annual_salary = float(input("Enter your annual salary:"))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:​"))

 
portion_down_payment = 0.25*(total_cost)
montly_saving = portion_saved*annual_salary/12

r=0.04/12

cost = total_cost-portion_down_payment
current_savings = 0
n = 0
remaining_payment=cost
amt =0
while portion_down_payment > current_savings:
    n = n+1
    amt = current_savings*r
    current_savings = current_savings+montly_saving+amt

print("Number of months:​",n)