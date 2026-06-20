class Dog:
    species = "Canis familiaris"   # class variable (shared by all dogs)

    def __init__(self, name):
        self.name = name           # instance variable (unique per dog)

    # INSTANCE METHOD — knows about the specific object (self)
    def bark(self):
        print(f"{self.name} says Woof!")

    # CLASS METHOD — knows about the class (cls), NOT the specific object
    @classmethod
    def get_species(cls):
        print(f"All dogs are: {cls.species}")

    # STATIC METHOD — knows about NEITHER the object nor the class
    @staticmethod
    def is_domestic():
        print("Dogs are domestic animals")

dog=Dog("Buddy")
dog2=Dog("Buddy2")
print(Dog.get_species())
print(Dog.is_domestic())
print(dog.bark())  # Output: Buddy says Woof!
print(dog2.bark())  # Output: Buddy2 says Woof!