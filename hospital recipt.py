PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

A = int(input("Enter the number of pennies: "))
B = int(input("Enter the number of nickels: "))
C = int(input("Enter the number of dimes: "))
D = int(input("Enter the number of quarters: "))

total_cents = (A * PENNY_VALUE) + (B * NICKEL_VALUE) + (C * DIME_VALUE) + (D * QUARTER_VALUE)

total_dollars = total_cents / PENNIES_IN_DOLLAR

if total_dollars > 1:
        print("amount is more.")
elif total_dollars < 1:
        print("it is less.")
else:
        print("Congratulations")
        print("1 dollar")
        print("You win the game")