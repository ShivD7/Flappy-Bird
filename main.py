#import all needed modules
import pygame
import random
import time
pygame.init()#initilize pygaame module to make use of it
size = (400, 600) #create the screen size
screen = pygame.display.set_mode(size)#create screen

game_state = "intro" #create a variable to track the different screens. Starts at intro as this is where the user deteremines if they want to play

collided = False #create variable to track if the player has collided with poles. Helps with understanding when we should switch to ending screen

main_characterx2 = 60 #create a variable that tracks where the main character is on the x-axis of the screen in the playing screen
main_charactery2 = 250#create a variable that tracks where the main character is on the y-axis of the screen in the playing screen


score = 0 #tracks the score; increments by one each time the olayer goes past a pole
times_clicked = 0 #tracks the amount of time the player has clicked. We use this so when the player clicks to play the game, it doesn't automatically move the player, it waits till they click again for movement.


up_speed = 5.5 #the amount of pixels the character moves up each time they click space
down_speed = 3.5 #gravity speed

moveup = None #variable that tracks if player wants to move up. Turns true if the user clicks or presses space

pipe_frequency = 1500
last_pipe = pygame.time.get_ticks()



#create variables for all of the colours needed
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY_BLUE = (3, 252, 252)
BLACK = (0, 0, 0)

#create variable that tracks the main while loop
done = False

font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)#generate the custom font that will be used throughout the game


background = pygame.image.load("background.jpg") #load image that will be used as background
background = pygame.transform.scale(background, [400, 600]) #change the size of the background

intro_text = pygame.image.load("Screen Shot 2023-06-04 at 11.02.54 AM.png")#load image that will be used as intro text
intro_text = pygame.transform.scale(intro_text, [400, 400])#change the size of the image

skyscraper = pygame.image.load("building2.png") #load image that will be used as one of the poles
skyscraper = pygame.transform.scale(skyscraper, [100, 100]) #change the size of the image
skyscraper2 = pygame.image.load("building2.png")#load image that will be used as one of the poles
skyscraper2 = pygame.transform.scale(skyscraper2, [100, 350])#change the size of the image



sidewalk = pygame.image.load("Sidewalk.jpg") #load image for sidewalk
sidewalk = pygame.transform.scale(sidewalk, [600, 100]) #change size of image

sidewalk_x = 0#create variable that tracks x position of sidewalk
sidewalk_x2 = 600 #create variable that tracks x-position of second sidewalk image; this image will be following the first one to create an "infinite" effect

clock = pygame.time.Clock() #used for tracking fps


def infinite_sidewalk(): #create a function for the infinite sidewalk effect (saves me lines of code)
    screen.blit(sidewalk, [sidewalk_x, 500]) 
    screen.blit(sidewalk, [sidewalk_x2, 500])

skyscraper_xpos = 650 #x position for first skyscraper image
skyscraper_ypos = 0 #y position for first skyscraper image
skyscraper2_xpos = 650  #x position for second skyscraper image
skyscraper2_ypos = 250 #y position for second skyscraper image


drawing_poles = False
pole_pair_status = False
    

#building pipes
pipe_surface = 	pygame.image.load("building2.png") #load image that will be used as one of the poles
pipe_surface = pygame.transform.scale(pipe_surface, [100, 400]) #change the size of the image
pipe_list = [] #create a list for all of the different pairs of skyscrapers - this will be used for randomization
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE , 1300)
pipe_height = [550, 180, 250, 500, 370, 300, 430]




def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 150))
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    global score
    for pipe in pipes:
        pipe.centerx -= 5
        if pipe.centerx == main_characterx2:
            score += 0.5
    
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

game_state_change = False

def check_collsion(pipes):
    global main_character_rect
    global game_state
    for pipe in pipes:
        if main_character_rect.colliderect(pipe):
            game_state = "ending"
            

restart = False

while not done: #create main while loop to do everything
    if game_state == "intro": #check what the game state is
        game_state = "intro"
        #must mean game state is intro
        for event in pygame.event.get(): #check for every event occuring in the pygame window
            if event.type == pygame.QUIT: #check if they want to close the window
                done = True #stop the game
            if event.type == pygame.MOUSEBUTTONDOWN:#check if they clicked the screen
                times_clicked += 1 #increment times clicked by one
                game_state = "playing" #change game state as they now want to play
        main_character = pygame.image.load("jetpackman.png")
        main_character = pygame.transform.scale(main_character, [150, 175])
        main_characterx1 = 120
        main_charactery1 = 280

        screen.blit(background, [0, 0])
        screen.blit(intro_text, [1, 200])
        screen.blit(main_character, [main_characterx1, main_charactery1])
    if game_state == "ending":
        main_characterx2 = 0
        font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)
        font2 = pygame.font.SysFont("Calibri", 50, False, False)
        losing_text = font.render("YOU DIED", True, WHITE)
        score_text = font2.render(str(score), True, WHITE)
        score_text2 = font.render("SCORE", True, WHITE)
        screen.fill(BLACK)
        screen.blit(losing_text, [80, 100])
        screen.blit(score_text2, [120, 250])
        screen.blit(score_text, [178, 325])
        pygame.draw.rect(screen, WHITE, [65, 390, 275, 100], 4)
        pos = pygame.mouse.get_pos()
        mouse_xpos = pos[0]
        mouse_ypos = pos[1]
        if mouse_xpos > 65 and mouse_xpos < 340 and mouse_ypos > 390 and mouse_ypos < 490:
                pygame.draw.rect(screen, SKY_BLUE, [65, 390, 275, 100])
        restart_text = font.render("RESTART", True, WHITE)
        screen.blit(restart_text, [105, 410])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouse_xpos = pos[0]
                mouse_ypos = pos[1]
                if mouse_xpos > 65 and mouse_xpos < 340 and mouse_ypos > 390 and mouse_ypos < 490:
                    restart = True
                    game_state = "intro"
    if game_state == "playing":
        if restart:
            moveup = None
            times_clicked = 0
            times_clicked += 1
            score = 0
            main_characterx2 = 60
            main_charactery2 = 250
            pipe_surface = 	pygame.image.load("building2.png") #load image that will be used as one of the poles
            pipe_surface = pygame.transform.scale(pipe_surface, [100, 400]) #change the size of the image
            pipe_list = [] #create a list for all of the different pairs of skyscrapers - this will be used for randomization
            SPAWNPIPE = pygame.USEREVENT
            pygame.time.set_timer(SPAWNPIPE , 1300)
            pipe_height = [550, 180, 250, 500, 370, 300, 430]
        main_character = pygame.image.load("jetpackman.png")
        main_character = pygame.transform.scale(main_character, [50, 50]) 
        main_character_rect = main_character.get_rect(topleft = (main_characterx2 - 29, main_charactery2 + 10))
        screen.blit(background, [0, 0])
        sidewalk_x -= 2
        sidewalk_x2 -= 2 
        if sidewalk_x < sidewalk.get_width() * -1:
            sidewalk_x = sidewalk.get_width()
        if sidewalk_x2 < sidewalk.get_width() * -1:
            sidewalk_x2 = sidewalk.get_width()
        infinite_sidewalk()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    times_clicked += 1
                    main_character_rect.topleft = (main_characterx2 - 29, main_charactery2 + 10)
                    if times_clicked != 1:
                        moveup = True
                    else:
                        moveup = None
                if event.type == pygame.MOUSEBUTTONUP:
                    if times_clicked != 1:
                        moveup = False
                    else:
                        moveup = None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main_character_rect.topleft = (main_characterx2 - 29, main_charactery2 + 10)
                        times_clicked += 1
                        if times_clicked != 1:
                            moveup = True
                        else:
                            moveup = None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        main_character_rect.topleft = (main_characterx2 - 29, main_charactery2 + 10)
                        times_clicked += 1
                        if times_clicked != 1:
                            moveup = True
                        else:
                            moveup = None
                if event.type == pygame.KEYUP:
                        times_clicked += 1
                        if times_clicked != 1:
                            moveup = False
                        else:
                            moveup = None
                if event.type == SPAWNPIPE:
                    pipe_list.extend(create_pipe())
        restart = False          
        

        if moveup == True:
            if main_charactery2  + 20 >= 0:
                main_charactery2 -= up_speed
            else:
                main_charactery2 -= 0
        if moveup == False: 
            main_charactery2 += down_speed
            if main_charactery2 + 273 >= 800:
                game_state = "ending"      
        if moveup == None:
            main_charactery2 == main_charactery2

        screen.blit(main_character, [main_characterx2, main_charactery2])
        font2 = pygame.font.SysFont("Calibri", 50, False, False)
        score = int(score)
        score_text = font2.render(str(score), True, WHITE)
        screen.blit(score_text, [185, 100])

        #moving pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        check_collsion(pipe_list)
        
        
        

        # Check if poles have moved off the screen
    pygame.display.flip()   
    clock.tick(60)


pygame.quit()
