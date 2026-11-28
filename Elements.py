import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

rect = pygame.Rect(0, 0, 120, 60)
rect.center = (320, 240)

font = pygame.font.Font(None, 36)
text = font.render("Hello Pygame!", True, (0, 0, 0))
text_rect = text.get_rect(center=(320, 150))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), rect)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
