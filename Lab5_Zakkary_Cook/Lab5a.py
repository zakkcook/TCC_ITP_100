def main():
    monthlyLoanAmount = float(input("Enter the monthly loan amount: "))
    monthlyInsuranceAmount = float(input("Enter the monthly insurance amount: "))
    monthlyGasAmount = float(input("Enter the monthly gas amount: "))
    monthlyOilAmount = float(input("Enter the monthly oil amount: "))
    monthlyTiresAmount = float(input("Enter the monthly tires amount: "))
    monthlyMaintenanceAmount = float(input("Enter the monthly maintenance amount: "))
    totalMonthlyExpenses = monthlyLoanAmount + monthlyInsuranceAmount + monthlyGasAmount + monthlyOilAmount + monthlyTiresAmount + monthlyMaintenanceAmount
    totalAnnualExpenses = totalMonthlyExpenses * 12

    print(f' Total monthly expense: ${totalMonthlyExpenses:,.2f}')
    print(f' Total annual expense: ${totalAnnualExpenses:,.2f}')


if __name__ == "__main__":
    main()
