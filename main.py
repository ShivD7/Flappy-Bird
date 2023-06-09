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



up_speed = 5 #the amount of pixels the character moves up each time they click space
down_speed = 3 #gravity speed

moveup = None #variable that tracks if player wants to move up. Turns true if the user clicks or presses space

number_of_poles = 0



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

skyscraper3 = pygame.image.load("building2.png")#load image that will be used as one of the poles
skyscraper3 = pygame.transform.scale(skyscraper3, [100, 370])#change the size of the image
skyscraper4 = pygame.image.load("building.png")#load image that will be used as one of the poles
skyscraper4 = pygame.transform.scale(skyscraper4, [100, 120])#change the size of the image

skyscraper5 = pygame.image.load("building2.png")#load image that will be used as one of the poles
skyscraper5 = pygame.transform.scale(skyscraper5, [100, 230])#change the size of the image
skyscraper6 = pygame.image.load("building2.png")#load image that will be used as one of the poles
skyscraper6 = pygame.transform.scale(skyscraper6, [100, 230])#change the size of the image

skyscraper_list = [[skyscraper], [skyscraper2],
                   [skyscraper3], [skyscraper4],
                   [skyscraper5], [skyscraper6]] #create a list for all of the different pairs of skyscrapers - this will be used for randomization

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

def random_poles(): #create function that will repeat the randomization of poles saving lines of code in the future
    global skyscraper_xpos
    global skyscraper_ypos
    global skyscraper2_xpos
    global skyscraper2_ypos
    global number_of_poles
    random_number = random.randrange(1, 4)
    if random_number == 1:
        if number_of_poles == 0:
            screen.blit(skyscraper, [skyscraper_xpos, skyscraper_ypos])
            screen.blit(skyscraper2, [skyscraper2_xpos, skyscraper2_ypos])
            skyscraper_xpos -= 2
            skyscraper2_xpos -= 2
        else:
            if skyscraper_xpos and skyscraper2_xpos < 50:
                screen.blit(skyscraper, [skyscraper_xpos, skyscraper_ypos])
                screen.blit(skyscraper2, [skyscraper2_xpos, skyscraper2_ypos])
                skyscraper_xpos -= 2
                skyscraper2_xpos -= 2

        number_of_poles += 1
    elif random_number == 2:
        if number_of_poles == 0:
            screen.blit(skyscraper3, [skyscraper_xpos, skyscraper_ypos])
            screen.blit(skyscraper4, [skyscraper2_xpos, skyscraper2_ypos])
            skyscraper_xpos -= 2
            skyscraper2_xpos -= 2
        else:
            if skyscraper_xpos and skyscraper2_xpos < 50:
                screen.blit(skyscraper3, [skyscraper_xpos, skyscraper_ypos])
                screen.blit(skyscraper4, [skyscraper2_xpos, skyscraper2_ypos])
                skyscraper_xpos -= 2
                skyscraper2_xpos -= 2

        number_of_poles += 1
    elif random_number == 3:
        if number_of_poles == 0:
            screen.blit(skyscraper5, [skyscraper_xpos, skyscraper_ypos])
            screen.blit(skyscraper6, [skyscraper2_xpos, skyscraper2_ypos])
            skyscraper_xpos -= 2
            skyscraper2_xpos -= 2
        else:
            if skyscraper_xpos and skyscraper2_xpos < 50:
                screen.blit(skyscraper5, [skyscraper_xpos, skyscraper_ypos])
                screen.blit(skyscraper6, [skyscraper2_xpos, skyscraper2_ypos])
                skyscraper_xpos -= 2
                skyscraper2_xpos -= 2

        number_of_poles += 1


while not done: #create main while loop to do everything
    if game_state == "intro": #check what the game state is
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
        pygame.display.flip()
    if game_state == "playing":
        drawing_poles = True
        main_character = pygame.image.load("jetpackman.png")
        main_character = pygame.transform.scale(main_character, [75, 75]) 
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
                        times_clicked += 1
                        if times_clicked != 1:
                            moveup = True
                        else:
                            moveup = None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        times_clicked += 1
                        if times_clicked != 1:
                            moveup = True
                        else:
                            moveup = None
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        times_clicked += 1
                        if times_clicked != 1:
                            moveup = False
                        else:
                            moveup = None
        

        if moveup == True:
            main_charactery2 -= up_speed
        if moveup == False: 
            main_charactery2 += down_speed
            if main_charactery2 + 273 >= 800:
                drawing_poles = False
                game_state = "ending"      
        if moveup == None:
            main_charactery2 == main_charactery2

        screen.blit(main_character, [main_characterx2, main_charactery2])
        font2 = pygame.font.SysFont("Calibri", 50, False, False)
        score_text = font2.render(str(score), True, WHITE)
        screen.blit(score_text, [185, 100])
        random_poles()
        pygame.display.flip()

    if game_state == "ending" :
        font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)
        font2 = pygame.font.SysFont("Calibri", 50, False, False)
        losing_text = font.render("YOU DIED", True, WHITE)
        score_text = font2.render(str(score), True, WHITE)
        score_text2 = font.render("SCORE", True, WHITE)
        screen.fill(BLACK)
        screen.blit(losing_text, [80, 100])
        screen.blit(score_text2, [120, 250])
        screen.blit(score_text, [178, 325])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True    
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
