import pygame
import Character
import Enemy

pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

fon = pygame.image.load("background3.png")
fon = pygame.transform.scale(fon, (800, 500))

pacman = Character.Character(250, 350, 50, 50, 10, "hero.png")
cyborg = Enemy.Enemy(150, 250, 50, 50, 1, "cyborg.png", 100, 200, 300, 300)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    pacman.move()
    Enemy.move()



    window.fill((123,123,123))
    window.blit(fon, (0, 0))
    pacman.render(window)
    cyborg.render(window)
    pygame.display.flip()
    fps.tick(60)