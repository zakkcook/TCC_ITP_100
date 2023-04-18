class Animal:

    def __init__(self, name, age, color, breed):
        _name = name,
        _age = age,
        _color = color,
        _breed = breed

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        self._age = age

    def setColor(self, color):
        self._name = color

    def setBreed(self, breed):
        self._breed = breed

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getColor(self):
        return self._color

    def getBreed(self):
        return self._breed

    # declaring methods
    def speak(self):
        if self.getBreed() == 'dog':
            return 'bark!'
        elif self.getBreed() == 'cat':
            return 'meow!'
        elif self.getBreed() == 'human':
            return 'hello!'
        else:
            return 'sniff.'


'''doing stuff for example'''
pet = Animal('Zakk', 32, 'blue', 'human')
print(pet.speak())




















