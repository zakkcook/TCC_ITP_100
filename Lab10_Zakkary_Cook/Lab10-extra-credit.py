'''
Write a class named Patient that has attributes for the following data:
* First name, middle name, and last name
* Address, city, state, and ZIP code
* Phone number
* Name and phone number of emergency contact

The Patient class's __init__ method should accept an argument for each
attribute. The Patient class should also have accessor and mutator methods for
each attribute.

Next, write a class named Procedure that represents a medical
procedure that has been performed on a patient. The Procedure class should have
attributes for the following data:
* Name of the procedure
* Date of the procedure
* Name of the practicioner who performed the procedure
* Charges for the procedure

The Procedure class's __init__ method should accept an argument for each
attribute. The Procedure class should also have accessor and mutator methods
for each attribute. Next, write a program that creates an instance of the
Patient class, initialized with sample data. Then, create three instances of
the Procedure class, initialized with the following data:

Procedure #1:                 Procedure #2:         Procedure #3:
---------------------------------------------------------------------------
Procedure name: Physical Exam Procedure name: X-ray Procedure name: Blood test
Date: Today's date            Date: Today's date    Date: Today's date
Practitoner: Dr.Irvine        Practitoner: Dr.Bob   Practitoner: Dr.Smith
Charge: 250.00                Charge: 500.00        Charge: 200.00

The program should display the patient's information, information about all
three of the procedures, and the total charges of the three procedures.
'''


class Patient:

    def __init__(self, first_name, middle_name, last_name,
                 address, city, state, zipcode, phone_number,
                 emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zipcode(self):
        return self.__zipcode

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone


class Procedure:

    def __init__(self, procedure_name, date, practicioner, charges):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__practicioner = practicioner
        self.__charges = charges

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_date(self, date):
        self.__date = date

    def set_practicioner(self, practicioner):
        self.__practicioner = practicioner

    def set_charges(self, charges: float):
        self.__charges = charges

    def get_procedure_name(self):
        return self.__procedure_name

    def get_date(self):
        return self.__date

    def get_practicioner(self):
        return self.__practicioner

    def get_charges(self):
        return self.__charges


def main():

    Patient1 = Patient('James', 'Edward', 'Jones', '123 Main Street',
                       'Billings', 'Montana', '59000', '406-555-1212',
                       'Jenny Jones', '406-555-1213')
    Procedure1 = Procedure('Physical Exam', '8-24-2019', 'Dr. Irvine', 250.00)
    Procedure2 = Procedure('X-ray', '8-24-2019', 'Dr. Jamison', 500.00)
    Procedure3 = Procedure('Blood Test', '8-24-2019', 'Dr. Smith', 200.00)
    Total = (Procedure1.get_charges()
             + Procedure2.get_charges()
             + Procedure3.get_charges())

    print(f'First Name: {Patient1.get_first_name()}')
    print(f'Middle Name: {Patient1.get_middle_name()}')
    print(f'Last Name: {Patient1.get_last_name()}')
    print(f'Address: {Patient1.get_address()}')
    print(f'City: {Patient1.get_city()}')
    print(f'State: {Patient1.get_state()}')
    print(f'ZIP: {Patient1.get_zipcode()}')
    print(f'Phone: {Patient1.get_phone_number()}')
    print(f'Emergency Contact: {Patient1.get_emergency_contact_name()}')
    print(f'Emergency Phone: {Patient1.get_emergency_contact_phone()}')
    print(' ')
    print(f'Procedure: {Procedure1.get_procedure_name()}')
    print(f'Date: {Procedure1.get_date()}')
    print(f'Practitioner: {Procedure1.get_practicioner()}')
    print(f'Charge: {Procedure1.get_charges():,.2f}')
    print(' ')
    print(f'Procedure: {Procedure2.get_procedure_name()}')
    print(f'Date: {Procedure2.get_date()}')
    print(f'Practitioner: {Procedure2.get_practicioner()}')
    print(f'Charge: {Procedure2.get_charges():,.2f}')
    print(' ')
    print(f'Procedure: {Procedure3.get_procedure_name()}')
    print(f'Date: {Procedure3.get_date()}')
    print(f'Practitioner: {Procedure3.get_practicioner()}')
    print(f'Charge: {Procedure3.get_charges():,.2f}')
    print(' ')
    print(f'Total Charges: {Total:,.2f}')


if __name__ == '__main__':
    main()
