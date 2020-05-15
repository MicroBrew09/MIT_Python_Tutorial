#Initialize Variables and Get User Input:
annual_salary0 = float(input("Enter your annual salary:"))
total_cost = 1000000
semi_annual_raise =0.07
r=0.04/12
portion_down_payment = 0.25*(total_cost)
n = 0
min_rate =0
max_rate = 10000
portion_saved = (min_rate+max_rate)/2
Found = False
while abs(min_rate-max_rate) > 1:
    n = n+1 
    annual_salary = annual_salary0
    current_savings = 0
    monthly_saving = (portion_saved/10000)*annual_salary/12
    amt =0
    i=1
    for i in range(1,37,1):
        amt = current_savings*r
        monthly_saving = (portion_saved/10000)*annual_salary/12
        current_savings = current_savings+monthly_saving+amt
        if i%6 == 0:
            annual_salary = annual_salary*(1+semi_annual_raise)
    
        if abs(current_savings - portion_down_payment) < 100:
            min_rate = max_rate
            Found = True
            break
        elif current_savings > portion_down_payment + 100:
            break

    if current_savings < portion_down_payment-100:
        min_rate = portion_saved
    if current_savings > portion_down_payment + 100:
        max_rate = portion_saved
        
    portion_saved = (min_rate + max_rate)/2
            
if Found:
    print("Best savings rate:", portion_saved/10000)
    print("Steps in bisection search", n)
else:
    print("Is is not possible to pay the down payment in three years")