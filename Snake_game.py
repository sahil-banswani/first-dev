import pygame
import random

from pygame import color
pygame.init()

# colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,200,0)

# Creating window 
screen_widht= 900
screen_height= 600
gameWindow = pygame.display.set_mode((screen_widht,screen_height))

# Game Title
pygame.display.set_caption("Snakes Game Disinged by SAHIL")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)#agar font define nhi kiya toh error demga note it

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# game loop
def gameloop():
    # Game Specificaton
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list=[]
    snk_lenght = 3

    food_x = random.randint(20,screen_widht/2)
    food_y = random.randint(20,screen_widht/2)
    score= 0
    init_velocity = 5
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(black)
            text_screen("Game Over! Press Enter to Continue",red,100,275)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0 

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0 

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0 

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0 

            snake_x = snake_x + velocity_x    
            snake_y = snake_y + velocity_y    

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score +=1
                print("Score: ",score *10)
                
                food_x = random.randint(20,screen_widht/2)
                food_y = random.randint(20,screen_widht/2)
                snk_lenght +=5

            gameWindow.fill(white)
            text_screen("Score: "+ str(score *10),green , 5 , 5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_lenght:
                del snk_list[0]
            
            # if head in snk_list[:-1]:
            #     game_over = True check why error is coming
            

            if snake_x<0 or snake_x>screen_widht or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("Game Over")
            plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()