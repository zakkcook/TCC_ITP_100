""" 
print("Enter the charge for food:")
print("Tip: $18.00")
print("Tax: $7.00")
print("Total: $125.00")

from decimal import Decimal
round(Decimal('3.14159265359'), 3)
Decimal('3.142')
 """
from decimal import Decimal


charge = float(input("Enter the charge for food: "))
tip = charge * 0.18
tax = charge * 0.07
total = charge + tip + tax

print(f"Tip: ${round(Decimal(tip), 2)}")
print(f"Tax: ${round(Decimal(tax), 2)}")
print(f"Total: ${round(Decimal(total), 2)}")

