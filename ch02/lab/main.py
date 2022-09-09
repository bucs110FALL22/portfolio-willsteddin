import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 14
print(classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print("Thank you for attending Binghamton University! Your cost per class this semester will be", f"${cost_per_class}.")

#Part B

list = [47, "Zhalo Supercell", "Sjur Eido", 73, "Lindsay", 3.1415926, "Mass Effect: Andromeda", 950123]
generated = random.choice(list)
print("You have generated a random choice from the list! Your choice is", f"{generated}!", f"This choice's class is {type(generated)}.")

