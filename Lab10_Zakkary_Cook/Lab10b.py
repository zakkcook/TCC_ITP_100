'''
Design a class that holds the following personal data: name, address, age, and
phone number. Write appropriate accessor and mutator methods. Also, write a
program that creates three instances of the class. One instance should hold
your information, and the other two should hold your friends' or family
members' information.
'''


class Person:

    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number


def main():
    Zakk = Person('Zakk Cook', 'Virginia Beach, VA', 29, '757-256-5555')
    Dad = Person('Danny Cook', 'Virginia Beach, VA', 52, '757-816-4444')
    Cassidy = Person('Cassidy Penley', 'Virginia Beach, VA', 25, '757-256-8888')

    print('Here is the data that you have entered:')
    print(f'Name: {Zakk.get_name()}')
    print(f'Address: {Zakk.get_address()}')
    print(f'Age: {Zakk.get_age()}')
    print(f'Phone: {Zakk.get_phone_number()}')
    print(' ')
    print(f'Name: {Dad.get_name()}')
    print(f'Address: {Dad.get_address()}')
    print(f'Age: {Dad.get_age()}')
    print(f'Phone: {Dad.get_phone_number()}')
    print(' ')
    print(f'Name: {Cassidy.get_name()}')
    print(f'Address: {Cassidy.get_address()}')
    print(f'Age: {Cassidy.get_age()}')
    print(f'Phone: {Cassidy.get_phone_number()}')


if __name__ == '__main__':
    main()
