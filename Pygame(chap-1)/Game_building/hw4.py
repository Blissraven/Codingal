import pygame
import sys

pygame.init()

# Full-screen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
clock = pygame.time.Clock()

# Load images
pet_image = pygame.image.load("pet.png").convert_alpha()
food_image = pygame.image.load("food.png").convert_alpha()
completion_bg = pygame.image.load("completion_background.jpg").convert()

# Scale background to full screen
completion_bg = pygame.transform.scale(completion_bg, (WIDTH, HEIGHT))

# Pet
pet = pygame.sprite.Sprite()
pet.image = pet_image
pet.rect = pet.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Food group
foods = pygame.sprite.Group()

# Example food positions
for position in [(200, 200), (600, 300), (900, 500)]:
    food = pygame.sprite.Sprite()
    food.image = food_image
    food.rect = food.image.get_rect(center=position)
    foods.add(food)

# Movement speed
speed = 5

# Completion state
completed = False

font = pygame.font.Font(None, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if not completed:
        # Arrow-key movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pet.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            pet.rect.x += speed
        if keys[pygame.K_UP]:
            pet.rect.y -= speed
        if keys[pygame.K_DOWN]:
            pet.rect.y += speed

        # Keep pet on screen
        pet.rect.clamp_ip(screen.get_rect())

        # Remove food when touched
        pygame.sprite.spritecollide(pet, foods, dokill=True)

        # Check whether all food has been collected
        if len(foods) == 0:
            completed = True

    # Draw
    if completed:
        # Full-screen completion background
        screen.blit(completion_bg, (0, 0))

        # Centered completion message
        message = font.render("All Food Collected!", True, (255, 255, 255))
        message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(message, message_rect)

    else:
        screen.fill((30, 30, 30))
        foods.draw(screen)
        screen.blit(pet.image, pet.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()