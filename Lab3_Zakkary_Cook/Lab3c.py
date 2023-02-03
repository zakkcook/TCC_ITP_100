# A software company sells a package that retails for $99. Quantity discounts are given according to the following table.
'''
10-19 get 10%
20-49 gets 20%
50-99 gets 30%
100+ gets 40%
'''

def main():
    packagesPurchased = int(input("Enter the number of packages purchased: "))
    printReceipt(packagesPurchased)
    
def getDiscount(packagesPurchased):
    discount = .01
    
    if packagesPurchased > 99:
        discount = .40
    elif packagesPurchased >= 50 and packagesPurchased <= 99:
        discount = .30
    elif packagesPurchased >= 20 and packagesPurchased <= 49:
        discount = .20
    elif packagesPurchased >= 10 and packagesPurchased <= 19:
        discount = .10
    else:
        discount = 0.0

    return discount


def printReceipt(packagesPurchased):
    packageCost = 99
    discountPct = getDiscount(packagesPurchased)
    discountAmount = packagesPurchased * packageCost * discountPct
    totalAmount = packagesPurchased * packageCost - discountAmount
    
    print(f"Discount Given: {discountPct:,.0%}")
    print(f"Discount Amount: ${discountAmount:,.2f}")
    print(f"Total Amount: ${totalAmount:,.2f}")

if __name__ == "__main__":
    main()