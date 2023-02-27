#payment calculation
def calculate_payment(balance, rate):
  interest = balance * rate / 12
  principal = 0.05 * balance - interest
  payment = interest + principal
  return interest, principal, payment

#User input purchase price
purchase_price = float(input("Enter the purchase price: $"))
down_payment = 0.1 * purchase_price
balance = purchase_price - down_payment
rate = 0.12

#print
print("\nMonth\tBalance\tInterest\tPrincipal\tPayment\tRemaining")
for month in range(1, 13):
  interest, principal, payment = calculate_payment(balance, rate)
  balance = balance - principal
  print(f"{month}\t${balance:.2f}\t${interest:.2f}   \t${principal:.2f}      \t${payment:.2f}  \t${balance:.2f}")
