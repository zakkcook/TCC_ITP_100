""" 
print("The number of shares that Joe purchased was 2,000.")
print("He paid $40.00 per share.")
print("Commission amount paid is 3 percent of the amount he paid for the stock.")
print("The number of shares Joe sold was 2,000")
print("Sold the stocks for $42.75 per share")
print("Another commission amount paid is 3 percent of the amount he received for the stock.")

print("The amount of money Joe paid for the stock.")
print("The amount of commission Joe paid his broker when he bought the stock.")
print("The amount for which Joe sold the stock.")
print("The amount of commission Joe paid his broker when he sold the stock.")
print("Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this amount is positive, then Joe made a profit. If the amount is \
       negative, then Joe lost money.")

print("Amount paid for the stock: $80,000.00")
print("Commission paid on the purchase: $2,400.00")
print("Amount the stock sold for: $85,500.00")
print("Commission paid on the sale: $2,565.00")
print("Profit (or loss if negative): $535.00")
 """

from decimal import Decimal
 
def main():
    totalSharesPurchased = float(input("How many shares would you like to purchase (2000?) at $40/ea? "))
    purchasePricePerShare = 40.00
    salePricePerShare = 42.75
    purchaseCommission = .03
    saleCommission = .03

    stockPurchasePrice = totalSharesPurchased * purchasePricePerShare
    purchaseCommissionAmount = stockPurchasePrice * purchaseCommission
    stockSellPrice = totalSharesPurchased * salePricePerShare
    saleCommissionAmount = stockSellPrice * saleCommission
    profit = stockSellPrice - stockPurchasePrice - purchaseCommissionAmount - saleCommissionAmount

    print(f"Amount paid for the stock: {f'${stockPurchasePrice:,.2f}'}")
    print(f"Commission paid on the purchase: {f'${purchaseCommissionAmount:,.2f}'}")
    print(f"Amount the stock sold for: {f'${stockSellPrice:,.2f}'}")
    print(f"Commission paid on the sale: {f'${saleCommissionAmount:,.2f}'}")
    print(f"Profit (or loss if negative): {f'${profit:,.2f}'}")

if __name__ == "__main__":
    main()
