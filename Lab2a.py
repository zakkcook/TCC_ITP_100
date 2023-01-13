""" 
print("The car will travel the following distances:")
print("420 miles in 6 hours.")
print("700 miles in 10 hours.")
print("1050 miles in 15 hours.") 
"""
def main():
    mph = 70
    print("The car will travel the following distances:")
    printDistance(mph, 6)
    printDistance(mph, 10)
    printDistance(mph, 15)

def printDistance(speedInMPH, hours):
    distance = speedInMPH * hours
    print(f"{distance} miles in {hours} hours.")

if __name__ == "__main__":
    main()