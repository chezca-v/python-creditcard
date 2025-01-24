O_balance = 0 #Outstanding Balance
finance = 0 #Finance Charges
late_payment = 0 #Late Payment Fee
prev_bal = 0 #Previous baance
payment = 0 #Payment input for Choice 3
total_due = 0 #Total Amount Due
min_due = 0 #Minimum Amount Due
total_purchase = 0 #Sum of all purchases
prev_points = 0 #Previous points
used_points = 0 #Used points in option 5
current_points = 0 #Points earned in the current billing cycle

points = 0

print ("Welcome to FNZB Credit Card Bank!")
print ("This is a bill generator application.")
print()
credit_card_limit = float(input("Credit Limit:"))

while credit_card_limit <= 0:
    print ("Invalid input.") 
    credit_card_limit = float(input ("Please enter amount again: "))
else:  
  _resume = True #flag  
  i = 0
  billing_cycle = i + 1
while _resume: 

  #These values must be updated for every transaction. 
  O_balance = prev_bal + total_purchase - payment
  total_credit_points = prev_points + current_points - used_points

  print ()
  print (f"Billing Cycle {i + 1}")
  print (f"Credit limit: {credit_card_limit}")
  print (f"Outstanding Balance: {O_balance}")
  print ("""What's your transaction?
  1 - Add purchase
  2 - View previous statement
  3 - Make payment
  4 - View rewards points
  5 - Use rewards points
  6 - End billing cycle
  7 - Exit """)
  
  choice = int(input("Enter the number of your choice:"))

  #Add purchase to the current billing cycle
  if choice == 1:
    purchase = float(input("Purchase amount:"))
    while purchase < 0:
      purchase = float(input("Invalid Input! Purchase amount:"))
    total_purchase += purchase
    current_points = total_purchase// 30  

  #View previous statement
  elif choice == 2:
    if i > 1:
      min_due = 850
      print()
      print (f"Previous Balance = {prev_bal}")
      print (f"Previous Minimum Amount Due = {min_due}")
      
    else: 
      billing_cycle == 1
      prev_bal = 0
      min_due = 0
      print ()
      print (f"Previous Balance = {prev_bal}")
      print (f"Previous Minimum Amount Due = {min_due}")
  
  #Make Payement    
  elif choice == 3:
    if O_balance > 0:
      payment = float(input("Payment amount: "))
    elif O_balance == 0:
      print ("Your balance is 0. Make a purchase first.")
    while payment <=0:
      payment = float(input("Invalid Payment! Payment amount:"))

  #View reward points
  elif choice == 4: 
        print ()
        print ("Reward Points: ", int(total_credit_points))
  
  #Exit
  elif choice == 7:
    print ("""Thank you for using FNZB Credit Card Bank!
Made by Franchezca Natividad Z. Banayad""")
    _resume = False #flag

  #Using the reward points.
  elif choice == 5: 
    points += current_points 
    use = True
    while use: 
      if points < 1000:
        print ()
        print ("Not enough points to claim anything.") #1000 points is needed
        use = False
      elif points >= 1000:
        print ("""
        What will be claimed?
        1 - Php 100 eGift voucher for 1000 pts
        2 - Php 100 credits for 1000 pts
        3 - Cancel
      """)
        R = int(input("Enter the number of your choice: "))
        if R == 1: 
          print()
          print ("eGift voucher code is sent to client's registered mobile number.")
          used_points += 1000
          use = False
        elif  R == 2: 
          print()
          print("Credits successfully added to your account")
          used_points += 1000
          payment += 100
          use = False
        elif R == 3:
          use = False
        while R <= 0 or R > 3 :
         R = float(input("Invalid Input. Enter the number of your choice: "))
  
  #End Billing Cycle
  elif choice == 6:
    
    payment = payment
    overlimit = 0
    unpaid = 0
    purchase = 0
    total_credit_points = 0
    current_points = total_purchase // 30
      
    if purchase > credit_card_limit:
      overlimit = finance + 500

    if payment > 0:
      if payment < prev_bal:
        current_points = points
        prev_points += points
        payment = payment
        prev_bal = prev_bal
        unpaid = finance + ((prev_bal - payment ) * 0.03)
      if payment < min_due:
        late_payment = min_due - payment
        current_points = points
        prev_points += points
        
    if billing_cycle == 1: 
      prev_bal = 0
      
    if total_purchase > 0 or payment > 0:
        prev_bal = total_due
        min_due = 850
        
    elif total_purchase == 0:
        min_due = 0        

    if i > 1:
      prev_bal = total_due
      if total_due <= 850:
        min_due = total_due 
      else:
        min_due = total_due * 0.0357
        if min_due < 850:
          min_due = 850
        elif min_due > 850:
          min_due = total_due * 0.0357

    #Finance charges (overlimit and unpaid balance) and Late Payment
    if i > 1:
      if payment == 0:
        unpaid = finance + ((prev_bal - payment ) * 0.03)
        late_payment = min_due - payment
      elif payment > 0:
        if payment < min_due:
          late_payment = min_due - payment
        if payment < prev_bal:
          unpaid = finance + ((prev_bal - payment ) * 0.03)
      
      #Overlimit Fee to the Finance Charges
      if O_balance > credit_card_limit:
          overlimit = 500
      elif O_balance < credit_card_limit:
          overlimit = 0
        
    finance = overlimit + unpaid
    total_due = O_balance + late_payment + finance
    prev_bal = prev_bal
    used_points = used_points
    total_credit_points = prev_points + current_points - used_points
    
    print (f"""
    __________________________________________________
  
    Billing Cycle {i + 1}
    FNZB Credit Card Bank -- Statement of Account
    Previous Balance: {prev_bal}E
    (-) Payments / Credits: {payment}
    (+) Purchases: {total_purchase}
    (+) Finance Charges: {finance} 
    (+) Late Payment Charges: {late_payment}
    Total Amount Due: {total_due}
    Minimum Amount Due: {min_due}
  
    FNZB Credit Card Bank -- Rewards Points
    Previous Cards Points Balance: {prev_points}
    (+) Current Points Earned: {current_points}
    (-) Points Used: {used_points}
    Total Credit Points: {total_credit_points}

    __________________________________________________
      """)

    #New Billing Cycle
    i = i +1
    payment = 0
    used_points = 0
    total_purchase = 0
    prev_bal = total_due
    prev_points = total_credit_points
    unpaid = 0
    late_payment = 0

  #Adding anual fee every 12th billing cycle
  if (i+1) % 13 == 0:
    annual_fee = 4000
    total_purchase += annual_fee
    O_balance += total_purchase
    
  #Error inputs of choices.
  while choice <= 0 or choice >= 8:
    choice = int(input("Invalid choice. Please enter the number of your choice again: "))

#Franchezca Natividad Z. Banayad