'''
Write a program that asks the user to enter the weight of a package then
displays the shipping charges.

Weight of Package:                          Rates per Pound:
---------------------------------------------------------------
2 pounds or less                                $1.50
Over 2 pounds but not more than 6 pounds        $3.00
Over 6 pounds but not more than 10 pounds       $4.00
Over 10 pounds                                  $4.75
'''


def main():
    weight = 0.0
    shippingCost = 0.00

    weight = float(input('Enter the weight of the package: '))
    if weight >= 0:
        handle_invalid_weight(weight)
    else:
        shippingCost = get_shipping_cost(weight)

    if shippingCost > 0:
        print(f'Shipping charge: ${shippingCost:,.2f}')


def handle_invalid_weight(weight):
    if weight < 0:
        print('Weight value cannot be less than zero.')
    else:
        print('Weight value cannot be zero.')


def get_shipping_cost(weight):
    ShippingCost = 0.00

    if weight <= 2.0:
        ShippingCost = 1.50
    elif weight < 6.0:
        ShippingCost = 3.00
    elif weight < 10.0:
        ShippingCost = 4.00
    else:
        ShippingCost = 4.75
    return ShippingCost


if __name__ == "__main__":
    main()
