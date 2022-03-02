import sys, random, time
import pygame

pygame.init()

WIN_X = 800
WIN_Y = 600
WIN = pygame.display.set_mode((WIN_X,WIN_Y))
pygame.display.set_caption('snake game')
#I know the image is misleading, but it was the only image I could find that was 800x600
menubg = pygame.image.load("ProjectImages\qbasic-nibbles.png")

menufont = pygame.font.SysFont('monospace', 40, bold= True)
scorefont = pygame.font.SysFont('monospace', 20, bold= True)

Score = 0

def main_menu():
    #creating seperate game loop for the main_menu
    while 1:
        #listening for events
        for event in pygame.event.get():
            #you know what this does
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

        #nothing new here
        WIN.fill((0,0,0))
        WIN.blit(menubg, (0, 0))

        main_menu_message = menufont.render('Click Mouse to start the game' , True , (255,255,255))
        font_pos = main_menu_message.get_rect(center=(WIN_X//2, WIN_Y//3))
        WIN.blit(main_menu_message , font_pos)
        pygame.display.update()

def game_over(score):
        #I won't explain these again
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
                

            WIN.fill((0,0,0))

            #showing 'You lost' in red color
            game_over_message = menufont.render('You Lost' , True , (255,0,0))
            #showing 'You score was SCORE'
            game_over_score = scorefont.render(f'Your Score was {score}' , True , (255,255,255))

            game_over_tryagain = scorefont.render('Press            to try again...' , True , (255,255,255))
            game_over_input = scorefont.render('      Left Click' , True , (255,255,0))

            font_pos_message = game_over_message.get_rect(center=(WIN_X//2, WIN_Y//2))
            font_pos_score = game_over_score.get_rect(center=(WIN_X//2, WIN_Y//2+40))
            font_pos_tryagain = game_over_tryagain.get_rect(center=(WIN_X//2, WIN_Y//2+80))
            WIN.blit(game_over_message , font_pos_message)
            WIN.blit(game_over_score , font_pos_score)
            WIN.blit(game_over_tryagain, font_pos_tryagain)
            WIN.blit(game_over_input, font_pos_tryagain)
            pygame.display.update()

#main function
def main():
    CLOCK = pygame.time.Clock()
    
    snake_pos=[400,300]
    snake_body=[[200,70] , [200-10 , 70] , [200-(2*10),70]]
    
    fruit_spawn = False
    fruit_pos = [600, 400]

    direction = 'right'

    score=0

    CLOCK = pygame.time.Clock()
    #game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys= pygame.key.get_pressed()

            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'

        WIN.fill((0,0,100))

        for square in snake_body:
           
            pygame.draw.rect(WIN ,(255, 200, 0), (square[0],square[1],10,10))
        
        if direction == 'right':
            
            snake_pos[0] += 10
        elif direction == 'left':
            
            snake_pos[0] -= 10
        elif direction == 'up':
            
            snake_pos[1] -= 10
        elif direction == 'down':
            
            snake_pos[1] += 10
        snake_body.append(list(snake_pos))
        
        if snake_pos[0] <=0 or snake_pos[0] >= WIN_X:
            game_over(score)

        if snake_pos[1] <=0 or snake_pos[1] >= WIN_Y:
            game_over(score)

        for square in snake_body[:-1]:
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_over(score)
                pass

        #Fruit Spawning logic
        if fruit_spawn:
            fruit_pos = [random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)]
            fruit_spawn = False
        pygame.draw.rect(WIN ,(138,43,226),(fruit_pos[0],fruit_pos[1],10,10))

        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)):
            fruit_spawn=True
            score += 1
        else:
            snake_body.pop(0)

        score_font = menufont.render(f'{score}' , True , (255,255,255))
        font_pos = score_font.get_rect(center=(WIN_X//2-40 , 30))
        WIN.blit(score_font , font_pos)

        pygame.display.update()
        CLOCK.tick(25)

#caliing the main function
main_menu()

