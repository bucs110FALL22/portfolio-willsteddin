from socketserver import StreamRequestHandler
import time
import animal

dog = animal.Animal()


# dog.name = "Seamus"
# dog.type = "Canine"
print(dog.name, dog.type, type(dog))