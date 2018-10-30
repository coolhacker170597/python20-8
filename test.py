class Pet:
    pass

class Cat(Pet):
    pass

print(isinstance(Cat(), Pet))
print(issubclass(Cat, object))
print(issubclass(Cat, Pet))
print(issubclass(Pet, Cat))
print(isinstance(Cat(), Cat))