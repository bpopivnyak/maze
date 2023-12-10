import pygame
import Character
import Enemy
import gold
import wall

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

fon = pygame.image.load("background3.png")
fon = pygame.transform.scale(fon, (800, 500))

pacman = Character.Character(250, 350, 50, 50, 10, "hero.png")
cyborg = Enemy.Enemy(150, 250, 50, 50, 1, "cyborg.png", 100, 200, 300, 300)
gold = gold.Gold(200, 500, 50, 50, "treasure.png")
walls = []
walls.append(wall.Wall(220, 40, 100, 20, (225, 225, 0)))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    pacman.move()
    cyborg.move()



    window.fill((123,123,123))
    window.blit(fon, (0, 0))
    pacman.render(window)
    cyborg.render(window)
    gold.render(window)
    for wall in walls:
         wall.render(window)
    pygame.display.flip()
    fps.tick(60)