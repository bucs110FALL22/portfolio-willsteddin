import pygame

pygame.init()

screen = pygame.display.set_mode()


screen.fill([255, 0, 0])
pygame.display.flip()
pygame.time.wait(500)
screen.fill([0, 255, 0])
pygame.display.flip()
pygame.time.wait(500)
screen.fill([0, 0, 255])
pygame.display.flip()
pygame.time.wait(500)
