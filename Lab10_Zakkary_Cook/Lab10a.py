'''
Write a class named Pet, which should have the following data attributes:
* __name (for the name of a pet)
* __animal_type (Example values are 'Dog', 'Cat', and 'Bird')
* __age (for the pet's age)
The Pet class should have an __init__method that creates these attributes.

It should also have the following methods:
* set_name() => This method assigns a value to the __name field.
* set_animal_type() => This method assigns a value to the __animal_type field.
* set_age() => This method assigns a value to the __age field.
* get_name() => This method assigns a value to the __name field.
* get_animal_type() => This method assigns a value to the __animal_type field.
* get_age() => This method assigns a value to the __age field.

Once you have written the class, write a program that creates an object of the
class and prompts the user to enter the name, type, and age of his or her pet.
This data should be stored as the object's attributes. Use the object's
accessor methods to retrieve the pet's name, type, and age and display this
data on the screen.
'''


class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    pet_name = input('Enter the name of the pet: ')
    pet_type = input('Enter the type of animal: ')
    pet_age = int(input('Enter the age of the pet: '))

    my_pet = Pet(pet_name, pet_type, pet_age)

    print('Here is the data that you have entered')
    print(f'Pet name: {my_pet.get_name()}')
    print(f'Animal type: {my_pet.get_animal_type()}')
    print(f'Age of pet: {my_pet.get_age()}')


if __name__ == '__main__':
    main()
