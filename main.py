import pygame


pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
BALL_SPEED = 20

ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball movement")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and ball_y - BALL_RADIUS > 0:
        ball_y -= BALL_SPEED
    if keys[pygame.K_s] and ball_y + BALL_RADIUS < SCREEN_HEIGHT:
        ball_y += BALL_SPEED
    if keys[pygame.K_a] and ball_x - BALL_RADIUS > 0:
        ball_x -= BALL_SPEED
    if keys[pygame.K_d] and ball_x + BALL_RADIUS < SCREEN_WIDTH:
        ball_x += BALL_SPEED


    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()