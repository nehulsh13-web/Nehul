import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Sprites")

player = pygame.Rect(100, 150, 50, 50)
enemy = pygame.Rect(400, 150, 50, 50)
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
