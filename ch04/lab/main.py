import pygame
pygame.init

window = pygame.display.set_mode((400,400))
windowSize = pygame.display.get_window_size()
print(windowSize)

pygame.draw.circle(window, "crimson", (200,200), 100, 0)
pygame.display.flip()
pygame.time.wait(1000)