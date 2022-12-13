from chart import Chart
from monster import MonstersAPI
import random
from sys import exit
import pygame
pygame.init()

def main():
  print("Click into the Pygame window and press the space bar to recieve the stat breakdown of a random D&D monster!\nEverytime you press space, a new one will generate.")
  
  while True:
    window = pygame.display.set_mode((800,600))
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          exit()
        if event.key == pygame.K_SPACE:
          gen = random.randrange(1, 1470)
          if (gen % 50) == 0:
            pageNum = int(gen/50)
            randMonster = MonstersAPI(pageNum)
            entryNum = gen - ((pageNum - 1) * 50) 
            monName = randMonster.getMonster(entryNum)
            monStats = randMonster.getStats(entryNum)
            chart = Chart(monStats[0],monStats[1],monStats[2],monStats[3],monStats[4],monStats[5],monName) 
            print(f"Your random monster is {monName}!")
          else:
            pageNum = int((gen/50) +1)
            randMonster = MonstersAPI(pageNum)
            entryNum = gen - ((pageNum - 1) * 50) 
            monName = randMonster.getMonster(entryNum)
            monStats = randMonster.getStats(entryNum)
            chart = Chart(monStats[0],monStats[1],monStats[2],monStats[3],monStats[4],monStats[5],monName) 
            print(f"Your random monster is {monName}!")
          window.fill("white")
          chart.showChart(window)
          pygame.display.flip()
        
  

main()
  
