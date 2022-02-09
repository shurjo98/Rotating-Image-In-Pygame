import pygame, sys


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=[400, 400])

    return rotated_surface, rotated_rect


pygame.init()
screen = pygame.display.set_mode((800, 800))
pikachu = pygame.image.load("Pikachu.jpeg")
pikachu_rect = pikachu.get_rect(center=[400, 400])
angle = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    angle += 1
    screen.fill((255, 255, 255))
    pikachu_rotated, pikachu_rotated_rect = rotate(pikachu, angle)

    screen.blit(pikachu_rotated, pikachu_rotated_rect)
    pygame.display.flip()
