#1 HR 13 MINS https://www.youtube.com/watch?v=jO6qQDNa2UY&ab_channel=TechWithTim
import pygame
import os
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FPS = 60
VEL = 4
BULLET_VEL = 7
MAX_BULLETS = 10
BORDER = pygame.Rect((WIDTH//2)-5, 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 120,100

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

resource_path = os.path.abspath(os.getcwd())

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
        os.path.join(resource_path, 'Assets\Yellowspaceship.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
        os.path.join(resource_path, 'Assets\Redspaceship.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

def yellow_handle_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width: # LEFT
                yellow.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH + 20: # RIGHT
                yellow.x += VEL
        if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: # UP
                yellow.y -= VEL
        if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT: # DOWN
                yellow.y += VEL        

def red_handle_movement(keys_pressed, red):
        if keys_pressed[pygame.K_a] and red.x - VEL > 0: # LEFT
                red.x -= VEL
        if keys_pressed[pygame.K_d] and red.x + VEL + red.width < BORDER.x + 20: # RIGHT
                red.x += VEL
        if keys_pressed[pygame.K_w] and red.y - VEL > 0: # UP
                red.y -= VEL
        if keys_pressed[pygame.K_s] and red.y + VEL + red.height < HEIGHT: # DOWN
                red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
        for bullet in yellow_bullets:
                bullet.x -= BULLET_VEL
                if red.colliderect(bullet): #if true, has hit.
                        pygame.event.post(pygame.event.Event(RED_HIT))
                        yellow_bullets.remove(bullet)
        for bullet in red_bullets:
                bullet.x += BULLET_VEL
                if yellow.colliderect(bullet): #if true, has hit.
                        pygame.event.post(pygame.event.Event(YELLOW_HIT))
                        red_bullets.remove(bullet)
                        

def draw_window(red,yellow, red_bullets, yellow_bullets):
        WIN.fill(BLACK)
        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
        WIN.blit(RED_SPACESHIP, (red.x, red.y))
        pygame.draw.rect(WIN, WHITE ,BORDER)
        

        for bullet in red_bullets:
                pygame.draw.rect(WIN, RED, bullet)
        for bullet in yellow_bullets:
                pygame.draw.rect(WIN, YELLOW, bullet)

        pygame.display.update()

def main():
        red_bullets = []
        yellow_bullets = []
        
        
        red = pygame.Rect(100,(HEIGHT/2) - SPACESHIP_HEIGHT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
        yellow = pygame.Rect(700,(HEIGHT/2) - SPACESHIP_HEIGHT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)  

        clock = pygame.time.Clock()
        run = True
        while run:
                print(red_bullets, yellow_bullets)
                clock.tick(FPS)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False

                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                                bullet = pygame.Rect(yellow.x, yellow.y + yellow.height//2 + 6, 10, 5)
                                yellow_bullets.append(bullet)

                        if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                                bullet = pygame.Rect(
                                        red.x + red.width - 30, red.y + red.height//2 + 6, 10, 5)
                                red_bullets.append(bullet)

                keys_pressed = pygame.key.get_pressed()
                yellow_handle_movement(keys_pressed, yellow)
                red_handle_movement(keys_pressed, red)

                handle_bullets(yellow_bullets, red_bullets, yellow, red)

                draw_window(red,yellow, red_bullets, yellow_bullets)

        pygame.quit()

if __name__ == "__main__":
    main()
        
