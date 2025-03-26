import pygame
import random

# O'yin oynasi o'lchamlari
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Ranglar
BACKGROUND_COLOR = (30, 30, 30)  # Ko'zga tashlanmaydigan yumshoq rang
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Pygame boshlash
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def get_random_food():
    return (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

def game_loop():
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = (CELL_SIZE, 0)
    food = get_random_food()
    running = True
    game_over = False
    
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    game_loop()
                    return
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
        
        if not game_over:
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            
            # Devor orqali o'tish
            if new_head[0] < 0:
                new_head = (WIDTH - CELL_SIZE, new_head[1])
            elif new_head[0] >= WIDTH:
                new_head = (0, new_head[1])
            elif new_head[1] < 0:
                new_head = (new_head[0], HEIGHT - CELL_SIZE)
            elif new_head[1] >= HEIGHT:
                new_head = (new_head[0], 0)
            
            # O'yin tugash sharti (ilon o'ziga tegsa)
            if new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    food = get_random_food()
                else:
                    snake.pop()
        
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
        
        if game_over:
            text = font.render("Game Over! Press R to Restart", True, WHITE)
            screen.blit(text, (WIDTH // 4, HEIGHT // 2))
        
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()

game_loop()
