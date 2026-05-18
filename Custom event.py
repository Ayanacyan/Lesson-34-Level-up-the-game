import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(
    pygame.image.load("BG.webp"),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.color = color
        self.update_color(color)
        self.rect = self.image.get_rect()

    def update_color(self, color):
        """Repaint sprite with a new color."""
        self.color = color
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, self.width, self.height))

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom color changing")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('blue'), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('green'), 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        # Collision → Change colors instead of removing sprite2
        if sprite1.rect.colliderect(sprite2.rect):
            new_color1 = pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            new_color2 = pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            sprite1.update_color(new_color1)
            sprite2.update_color(new_color2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, (
            (SCREEN_WIDTH - win_text.get_width()) // 2,
            (SCREEN_HEIGHT - win_text.get_height()) // 2
        ))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
