import pygame
import random

# Initialize pygame
pygame.init()

# Game window
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Ball")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Ball
ball_x = 50
ball_y = HEIGHT // 2
ball_radius = 15
gravity = 0.6
velocity = 0
jump = -10

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_vel = 4
pipes = []

# Score
score = 0

def draw_window():
    win.fill(WHITE)
    
    # Draw ball
    pygame.draw.circle(win, BLUE, (ball_x, int(ball_y)), ball_radius)
    
    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(win, GREEN, pipe)
    
    # Draw score
    text = font.render(f"Score: {score}", True, RED)
    win.blit(text, (10, 10))
    
    pygame.display.update()

def create_pipe():
    y = random.randint(100, HEIGHT - 100)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, y - pipe_gap // 2)
    bottom_pipe = pygame.Rect(WIDTH, y + pipe_gap // 2, pipe_width, HEIGHT - y)
    return top_pipe, bottom_pipe

def main():
    global ball_y, velocity, pipes, score
    run = True
    
    # Initial pipes
    pipes = []
    pipes.extend(create_pipe())
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                velocity = jump

        # Ball physics
        velocity += gravity
        ball_y += velocity
        
        # Pipe movement
        for pipe in pipes:
            pipe.x -= pipe_vel
            
        # Add new pipes
        if pipes[-1].x < WIDTH - 200:
            pipes.extend(create_pipe())
        
        # Remove off-screen pipes
        if pipes[0].x + pipe_width < 0:
            pipes.pop(0)
            pipes.pop(0)
            score += 1
        
        # Collision detection
        ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
        for pipe in pipes:
            if ball_rect.colliderect(pipe):
                run = False
        
        # Check if ball hits ground or sky
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
            run = False
        
        draw_window()
    
    pygame.quit()
    print(f"Game Over! Final Score: {score}")

if __name__ == "__main__":
    main()
 