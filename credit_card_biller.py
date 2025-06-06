# credit_card_billing.py

"""
FNZB Credit Card Billing System
Author: Franchezca Natividad Z. Banayad

This program simulates a credit card billing statement generator, including:
- Purchases
- Payments
- Rewards points
- Finance charges
- Late payment fees
- Billing cycles
"""

# Initialization of Variables
O_balance = finance = late_payment = prev_bal = payment = 0
total_due = min_due = total_purchase = prev_points = used_points = current_points = 0
points = 0

print("Welcome to FNZB Credit Card Bank!")
print("This is a bill generator application.\n")

# Input and validate credit limit
while True:
    credit_card_limit = float(input("Credit Limit: "))
    if credit_card_limit > 0:
        break
    print("Invalid input. Please enter amount again.")

_resume = True
i = 0

while _resume:
    billing_cycle = i + 1
    O_balance = prev_bal + total_purchase - payment
    total_credit_points = prev_points + current_points - used_points

    print(f"\nBilling Cycle {billing_cycle}")
    print(f"Credit limit: {credit_card_limit}")
    print(f"Outstanding Balance: {O_balance}")
    print("""What's your transaction?
    1 - Add purchase
    2 - View previous statement
    3 - Make payment
    4 - View rewards points
    5 - Use rewards points
    6 - End billing cycle
    7 - Exit""")

    try:
        choice = int(input("Enter the number of your choice: "))
    except ValueError:
        print("Invalid input. Try again.")
        continue

    # 1. Add Purchase
    if choice == 1:
        try:
            purchase = float(input("Purchase amount: "))
            while purchase < 0:
                purchase = float(input("Invalid Input! Purchase amount: "))
            total_purchase += purchase
            current_points = total_purchase // 30
        except ValueError:
            print("Invalid number.")
    
    # 2. View Previous Statement
    elif choice == 2:
        if i > 0:
            min_due = 850
        else:
            prev_bal = min_due = 0
        print(f"\nPrevious Balance = {prev_bal}")
        print(f"Previous Minimum Amount Due = {min_due}")

    # 3. Make Payment
    elif choice == 3:
        if O_balance <= 0:
            print("Your balance is 0. Make a purchase first.")
        else:
            try:
                payment = float(input("Payment amount: "))
                while payment <= 0:
                    payment = float(input("Invalid Payment! Payment amount: "))
            except ValueError:
                print("Invalid number.")

    # 4. View Reward Points
    elif choice == 4:
        print(f"\nReward Points: {int(total_credit_points)}")

    # 5. Use Reward Points
    elif choice == 5:
        points += current_points
        if points < 1000:
            print("\nNot enough points to claim anything.")
        else:
            print("""
What will be claimed?
1 - Php 100 eGift voucher for 1000 pts
2 - Php 100 credits for 1000 pts
3 - Cancel
""")
            try:
                R = int(input("Enter the number of your choice: "))
                if R == 1:
                    print("eGift voucher code is sent to your registered number.")
                    used_points += 1000
                elif R == 2:
                    print("Credits added to your account.")
                    used_points += 1000
                    payment += 100
                elif R == 3:
                    pass
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

    # 6. End Billing Cycle
    elif choice == 6:
        purchase = 0
        unpaid = 0
        overlimit = 0
        current_points = total_purchase // 30

        if payment < prev_bal:
            unpaid = (prev_bal - payment) * 0.03
        if payment < min_due:
            late_payment = min_due - payment

        if O_balance > credit_card_limit:
            overlimit = 500

        finance = overlimit + unpaid
        total_due = O_balance + finance + late_payment

        if total_due <= 850:
            min_due = total_due
        else:
            min_due = max(total_due * 0.0357, 850)

        print(f"""
__________________________________________________

Billing Cycle {billing_cycle}
FNZB Credit Card Bank -- Statement of Account
Previous Balance: {prev_bal}
(-) Payments / Credits: {payment}
(+) Purchases: {total_purchase}
(+) Finance Charges: {finance}
(+) Late Payment Charges: {late_payment}
Total Amount Due: {total_due}
Minimum Amount Due: {min_due}

FNZB Credit Card Bank -- Rewards Points
Previous Card Points Balance: {prev_points}
(+) Current Points Earned: {current_points}
(-) Points Used: {used_points}
Total Credit Points: {total_credit_points}
__________________________________________________
""")

        # Reset for next cycle
        prev_bal = total_due
        prev_points = total_credit_points
        used_points = total_purchase = payment = 0
        i += 1

        # Add annual fee every 12 billing cycles
        if (i + 1) % 13 == 0:
            total_purchase += 4000

    # 7. Exit
    elif choice == 7:
        print("\nThank you for using FNZB Credit Card Bank!")
        _resume = False
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

# End of Program
#Franchezca Natividad Z. Banayad
