import pygame

pygame.init()
"""
PART A
"""


def threePlusOne(n):
    """
    This is a function that calculates the Collatz Conjecture for any given n value and prints a list of every step along the way. 
    """
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (3 * n) + 1
            print(n)


"""
PART B
"""


def threePlusOne_count(n):
    """
    This is a function that calculates the Collatz Conjecture for any given n value and prints a list of every step along the way. 
    """
    count = 0
    print(n)
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (3 * n) + 1
            print(n)
    print(f"There are {count} items in the sequence when n is {n}.")


def threePlusOne_range(upperLimit):
    """
    This is a version of the 3n+1 calculation that checks across an entire range of numbers and returns them in a dictionary.
    """
    threePlusOne_dict = {}
    for i in range(2, upperLimit + 1):
        count = 0
        n = i
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
        threePlusOne_dict[i] = count
    print(threePlusOne_dict)


"""
PART C
"""


def threePlusOne_graph(upperLimit):
    """
    This is a continuation of the previous function that also tracks the current maximum count and graphs the number of iterations for each integer.
    """
  
    graph = pygame.display.set_mode()

    threePlusOne_dict = {}
    maxSoFar = 0
    for i in range(2, upperLimit + 1):
        count = 0
        n = i
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
        if count > maxSoFar:
            maxSoFar = count
        threePlusOne_dict[i] = count
    #coordinates = threePlusOne_dict.items()
    coordinates = []
    for i in threePlusOne_dict.items():
        coordinates.append((i[0]*10, i[1]*10))
    print(coordinates)
    graph = pygame.transform.flip(graph, False, True)
    pygame.draw.lines(graph, "snow", False, (coordinates))
    graph.blit(graph, (0, 0))
    pygame.display.flip()
    pygame.time.wait(1000)

    # coordinates = [(0,0)]
    # coordinates.append(threePlusOne_dict.items())
    # for i in coordinates:
    #     pygame.draw.lines(graph, "white", False, i, (i+1))
    # newGraph = pygame.transform.flip(graph, False, True)
    # pygame.display.flip()


threePlusOne_graph(10)
