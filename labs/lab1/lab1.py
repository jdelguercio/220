def monthlyinterest():
    print("Enter values to get your monthly interest charge.")
    air = eval(input("What is your annual interest rate? Please input as decimal."))
    billing_cycle = eval(input("How many days are in your billing cycle?"))
    net_bal = eval(input("What is your net balance?"))
    payment_amount = eval(input("What is your payment amount?"))
    day_of_billing_cycle = eval(input("What day of the billing cycle did you pay?"))

    step1 = net_bal * billing_cycle
    step2 = payment_amount * (billing_cycle - day_of_billing_cycle)
    step3 = step1 - step2
    avg_daily_bal = step3 / billing_cycle
    monthly_rate = air / 12
    monthly_interest_charge =  monthly_rate * avg_daily_bal
    print("Your monthly interest charge is ${:.2f}".format(monthly_interest_charge))
