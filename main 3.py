import pygame
import random
import sys

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 50, 50)
BROWN = (139, 69, 19)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка с яблочками (WASD)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",24)

def get_random_food(snake_body):
    while True: 
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake_body:
            return (x, y)

def draw_apple(surface, x, y):
    center_x = x + CELL_SIZE // 2
    center_y = y + CELL_SIZE // 2
    pygame.draw.circle(surface, RED, (center_x, center_y), CELL_SIZE // 2 - 2)
    pygame.draw.line(surface, BROWN, (center_x , center_y - 7), (center_x + 3, center_y - 12), 2)
    pygame.draw.circle(surface, GREEN, (center_x + 5, center_y - 10), 3)

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    dx, dy = CELL_SIZE, 0

    food = get_random_food(snake)
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and dy == 0:
                    dx, dy = 0, -CELL_SIZE
                elif event.key == pygame.K_s and dy == 0:
                    dx, dy = 0, CELL_SIZE
                elif event.key == pygame.K_a and dx == 0:
                    dx, dy = -CELL_SIZE, 0
                elif event.key == pygame.K_d and dx == 0:
                    dx, dy = CELL_SIZE, 0

                if event.key == pygame.K_SPACE and game_over:
                    snake = [(100, 100), (80, 100), (60, 100)]
                    dx, dy = CELL_SIZE, 0 
                    food = get_random_food(snake)
                    score = 0
                    game_over = False

        if game_over: continue
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy) 

        if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT):
            game_over = True 
            continue

        if new_head in snake[:-1]:
            game_over = True
            continue

        snake.insert(0, new_head)
        if new_head == food: 
            score += 1
            food = get_random_food(snake)
        else: 
            snake.pop()
        screen.fill(BLACK)

        draw_apple(screen, food[0], food[1])

        for i, segment in enumerate(snake):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (segment[0]+1, segment[1]+1, CELL_SIZE-2, CELL_SIZE-2), border_radius=4)

        score_text = font.render(f"Счёт: {score}", True, WHITE)
        screen.blit(score_text, (10,10))
        if game_over:
            over_text = font.render("ТЫ ПРОИГРАЛ АХАХАХАХАХАХАХ", True, RED)
            text_rect = over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(over_text, text_rect)

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__": 
    main()




