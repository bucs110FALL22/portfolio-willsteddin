def star_pyramid():
    """This is a function that prints a pyramid of asterisks with a certain number of rows based on user input.
  """
    rows = int(
        input(
            "Please enter how many rows you would like your pyramid to have: ")
    )
    for i in range(rows + 1):
        print("*" * i, "\n")

star_pyramid()

def rstar_pyramid():
    """
  This is a function that prints an inverted pyramid of asterisks with a certain number of rows based on user input.
  """
    rrows = int(
        input(
            "Please enter how many rows you would like your pyramid to have: ")
    )
    for i in range((rrows), 0, -1):
        print("*" * i, "\n")

rstar_pyramid()

