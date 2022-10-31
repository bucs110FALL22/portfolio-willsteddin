from socketserver import StreamRequestHandler
import time
import animal

animal1 = animal.Animal()

animal1.name = "Seamus"
animal1.type = "Canine"
print(animal1.name, animal1.type)
