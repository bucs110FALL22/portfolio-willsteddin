import pygame
import math
import random

pygame.init

window = pygame.display.set_mode((400,400))
windowSize = pygame.display.get_window_size()
print(windowSize)

color1 = "lime"
color2 = "dodgerblue"
center = (200,200)
hitCount = 0
game = True

while game:  
  pygame.display.flip()
  window.fill("lightsteelblue")
  pygame.draw.circle(window, "crimson", (200,200), 200, 0)
  pygame.draw.line(window, "black", (200,0), (200,400))
  pygame.draw.line(window, "black", (0,200), (400,200))
  pygame.display.flip()

  for x in ["game"]*10:
    pygame.time.wait(1000)
    xcor = random.randrange(0,400)
    ycor = random.randrange(0,400)
    distance_from_center = math.hypot((xcor-200), (ycor-200))
    is_in_circle = distance_from_center <= 200
    if is_in_circle:
      pygame.draw.circle(window, "lime", (xcor, ycor), 5, 0)
      pygame.display.flip()
      print("Hit!")
      hitCount += 1
    else:
      pygame.draw.circle(window, "snow", (xcor, ycor), 5, 0)
      pygame.display.flip()
      print("Miss!")
  print(f"You've completed the game! You landed {hitCount} darts on the board out of 10!")
  pygame.time.wait(2000)
  game = False

window.fill("black")
pygame.display.flip()

print("Click on the color of the player that you believe will win the dart competition. ")
selection = True

while selection:
  Rect1 = ((50,175), (125, 50))
  Rect2 = ((225, 175), (125, 50))
  hitBoxWidth = 125
  hitBoxHeight = 50
  limeButtonBox = pygame.Rect(Rect1)
  dodgerblueButtonBox = pygame.Rect(Rect2)
  pygame.draw.rect(window, "lime", Rect1)
  pygame.draw.rect(window, "dodgerblue", Rect2)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouseClickPos = event.pos
      if limeButtonBox.collidepoint(mouseClickPos): 
        print("You have selected the Lime player!")
        pygame.time.wait(500)
        window.fill("black")
        playerChoice = "Lime"
        selection = False
        # Rect1 = ((0,0)(0,0))
        # Rect2 = ((0,0)(0,0))
      elif dodgerblueButtonBox.collidepoint(mouseClickPos):
        print("You have selected the Blue player! ")
        pygame.time.wait(500)
        window.fill("black")
        playerChoice = "Blue"
        selection = False

versus = True
limeHits = 0
blueHits = 0

while versus:
  pygame.display.flip()
  window.fill("lightsteelblue")
  pygame.draw.circle(window, "crimson", (200,200), 200, 0)
  pygame.draw.line(window, "black", (200,0), (200,400))
  pygame.draw.line(window, "black", (0,200), (400,200))
  pygame.display.flip()
  for i in range(1,11):
    print(f"ROUND {i}!")
    for _ in [color1, color2]:
      pygame.time.wait(500)
      xcor = random.randrange(0,400)
      ycor = random.randrange(0,400)
      distance_from_center = math.hypot((xcor-200), (ycor-200))
      is_in_circle = distance_from_center <= 200
      if is_in_circle:
        pygame.draw.circle(window, _, (xcor, ycor), 5, 0)
        pygame.display.flip()
        print(f"{_} gets a hit! ")
        if _ == color1:
          limeHits += 1
        elif _ == color2:
          blueHits += 1
      else:
        pygame.draw.circle(window, "snow", (xcor, ycor), 5, 0)
        pygame.display.flip()
        print(f"{_} misses! ")
  pygame.time.wait(2000)
  if limeHits == blueHits:
    print(f"The game ended as a tie! Both players received {blueHits} points. You technically guessed incorrectly. ")
    versus = False
  elif limeHits > blueHits:
    print(f"The Lime player won the game, with {limeHits} points! ")
    if playerChoice == "Lime":
      print("You guessed correctly! ")
      versus = False
    else:
      print("You guessed incorrectly. Better luck next time!")
      versus = False
  elif limeHits < blueHits:
    print(f"The Blue player has won the game, with {blueHits} points! ")
    if playerChoice == "Blue":
      print("You guessed correctly! ")
      versus = False
    else: 
      print("You guessed incorrectly. Better luck next time! ")
      versus = False
pygame.time.wait(3000)