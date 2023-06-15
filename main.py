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


up_speed = 7 #the amount of pixels the character moves up each time they click space
down_speed = 5 #gravity speed

moveup = None #variable that tracks if player wants to move up. Turns true if the user clicks or presses space



#create all necessary variables for timer
frame_count = 0
frame_rate = 60
start_time = -1

#change the python icon in the top left corner
pygame_icon = pygame.image.load("jetpackman.png")
pygame.display.set_icon(pygame_icon)

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




    

#building pipes
pipe_surface = 	pygame.image.load("building2.png") #load image that will be used as one of the poles
pipe_surface = pygame.transform.scale(pipe_surface, [100, 400]) #change the size of the image
pipe_list = [] #create a list for all of the different pairs of skyscrapers - this will be used for randomization
SPAWNPIPE = pygame.USEREVENT#create a user event for drawing pipes
pygame.time.set_timer(SPAWNPIPE , 1400)#create a time gap between when the poles should be put in the screen
pipe_height = [550, 180, 250, 500, 370, 300, 430] #create a list for random pole heigths




def create_pipe(): #create a funciton for create a pipe that will later be blit onto screen
    random_pipe_pos = random.choice(pipe_height)#pick random pipe height
    #create a rectangle around these pipes
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 150))
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    return bottom_pipe, top_pipe#return the two images created 

def move_pipes(pipes):
    global score
    for pipe in pipes:#go through a list of pipes
        pipe.centerx -= 5#change the x-position to create animation
        if pipe.centerx == main_characterx2: #check if character has passed the poles
            score += 0.5#increment score
    
    return pipes

def draw_pipes(pipes): #drawing pipes function
    for pipe in pipes:#go through a list of pipes
        if pipe.bottom >= 600:#check if the pipe is going to blit on bottom or top
            screen.blit(pipe_surface, pipe)
        else:#the pole must need to be on the top
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

game_state_change = False#check if game state has changed

def check_collsion(pipes):#create function to check for collision
    global main_character_rect
    global game_state
    for pipe in pipes:#go through list of event
        if main_character_rect.colliderect(pipe):
            game_state = "ending"
            

restart = False#create variable that tracks if the player wants to restart

#set up the sound for the game
pygame.mixer.init()
pygame.mixer.music.load("backgroundsound.mp3")
pygame.mixer.music.play() 

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
        main_character = pygame.image.load("jetpackman.png")#load main character image 
        main_character = pygame.transform.scale(main_character, [150, 175])#change size of image
        main_characterx1 = 120#set variable for character x-position in intro screen
        main_charactery1 = 280#set variable for character y-position in intro screen

        screen.blit(background, [0, 0])#blit background image onto screen
        screen.blit(intro_text, [1, 200])#blit the intrp text image onto screen
        screen.blit(main_character, [main_characterx1, main_charactery1])#blit the main character image onto screen
    if game_state == "ending":#check if game state is ending
        #set up music and play it
        pygame.mixer.init()
        pygame.mixer.music.load("backgroundsound.mp3")
        pygame.mixer.music.play()          
        main_characterx2 = 0#main character shouldn't be on screen
        font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)#create a custom font that will be used
        font2 = pygame.font.SysFont("Calibri", 50, False, False)#create another font for numbers and special character
        losing_text = font.render("YOU DIED", True, WHITE)#create text for dying
        score_text = font2.render(str(score), True, WHITE)#create text for score
        score_text2 = font.render("SCORE", True, WHITE)#create text for score
        screen.fill(BLACK)#fill screen with black to cover other things
        screen.blit(losing_text, [93, 100])#blit losing text onto screen
        screen.blit(score_text2, [133, 250])#blit score text onto screen
        screen.blit(score_text, [184, 325])#blit other score text onto screen
        pygame.draw.rect(screen, WHITE, [65, 390, 275, 100], 4)#draw an unfilled rectangle for restart button
        pos = pygame.mouse.get_pos()#get mous position
        mouse_xpos = pos[0]#set variable x mouse position 
        mouse_ypos = pos[1]#set variable y mouse position
        if mouse_xpos > 65 and mouse_xpos < 340 and mouse_ypos > 390 and mouse_ypos < 490:#check if mouse position is hoveing over button
                pygame.draw.rect(screen, SKY_BLUE, [65, 390, 275, 100])#draw rectangle over the other rectangle to create hover effect
        restart_text = font.render("RESTART", True, WHITE)#create the text that will go inside restart button
        screen.blit(restart_text, [105, 410])#blit restart text onto screen
        output_string = "Time played: {0:02}:{1:02}".format(minutes, seconds)#create string for timer
     
    
        text = font2.render(output_string, True, WHITE)#create text for timer
     
        screen.blit(text, [10, 520])#blit timer onto screen
        for event in pygame.event.get():#check for events occuring on window
            if event.type == pygame.QUIT:#check if they leave the window
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:#check if mouse has been clicked
                pos = pygame.mouse.get_pos()#get mouse position
                mouse_xpos = pos[0]#set variable x mouse position 
                mouse_ypos = pos[1]#set variable y mouse position
                if mouse_xpos > 65 and mouse_xpos < 340 and mouse_ypos > 390 and mouse_ypos < 490:#check if mouse clicked the button
                    restart = True#they want to restart so make restart variable true
                    game_state = "intro"#make game_state to intro
    if game_state == "playing":
        if restart:#as they want to restart, reinitialize all of the variables needed for the playing screen      
            moveup = None
            frame_count = 0
            frame_rate = 60
            start_time = -1            
            times_clicked = 0
            times_clicked += 1
            score = 0
            main_characterx2 = 60
            main_charactery2 = 250
            pipe_surface = pygame.image.load("building2.png") 
            pipe_surface = pygame.transform.scale(pipe_surface, [100, 400]) 
            pipe_list = [] 
            SPAWNPIPE = pygame.USEREVENT
            pygame.time.set_timer(SPAWNPIPE , 1300)
            pipe_height = [550, 180, 250, 500, 370, 300, 430]      
        main_character = pygame.image.load("jetpackman.png")#load main character image
        main_character = pygame.transform.scale(main_character, [50, 50]) #change size of the image
        main_character_rect = main_character.get_rect(topleft = (main_characterx2 - 15, main_charactery2 + 4))#create rectangle around main character for collision detection
        screen.blit(background, [0, 0])#blit background image onto the screen
        sidewalk_x -= 2#change sidewalk x pos to create animation
        sidewalk_x2 -= 2 #change sidewalk2 x pos to create animation
        if sidewalk_x < sidewalk.get_width() * -1:#check if first sidewalk is off the screen
            sidewalk_x = sidewalk.get_width()#reassign value so its continuous
        if sidewalk_x2 < sidewalk.get_width() * -1:#check if second sidewalk is off the screen
            sidewalk_x2 = sidewalk.get_width()#reassign value so its continuous
        infinite_sidewalk()#call function for infinite sidewalk
        for event in pygame.event.get():#check for all events on the screen
                if event.type == pygame.QUIT:#check if user wants to leave
                    done = True#break out of while loop
                if event.type == pygame.MOUSEBUTTONDOWN:#check if mouse button was clicked
                    times_clicked += 1#increase times clicked by one
                    main_character_rect.topleft = (main_characterx2 - 15, main_charactery2 + 4)#put rectangle around the main character
                    if times_clicked != 1:#check if they've clicked either less or more than one
                        moveup = True#change moveup variable to True as they now want to moveup
                    else:#doesn't want to move so don't move character
                        moveup = None#change moveup to none as the player hasn't clicked yet, so gravity shouldn't effect them yet
                if event.type == pygame.MOUSEBUTTONUP:#check if mouse button was released
                    if times_clicked != 1:#check if they've clicked either less or more than one
                        moveup = False#change moveup variable to False as they now don't want to moveup
                    else:#hasn't even clicked
                        moveup = None#change moveup to none as the player hasn't clicked yet, so gravity shouldn't effect them yet
                if event.type == pygame.KEYDOWN:#check if key is pressed
                    if event.key == pygame.K_SPACE:#check if the key pressed is space
                        main_character_rect.topleft = (main_characterx2 - 15, main_charactery2 + 4)#create rectangle around main character
                        times_clicked += 1#increment times clicked by one
                        if times_clicked != 1:#check if they've clicked either less or more than one
                            moveup = True#change moveup variable to True as they now want to moveup
                        else:#doesn't want to move so don't move character
                            moveup = None#change moveup to none as the player hasn't clicked yet, so gravity shouldn't effect them yet
                if event.type == pygame.KEYDOWN:#check if key is pressed
                    if event.key == pygame.K_UP:
                        main_character_rect.topleft = (main_characterx2 - 15, main_charactery2 + 4)#create rectangle around main character
                        times_clicked += 1#increment times clicked by one
                        if times_clicked != 1:#check if they've clicked either less or more than one
                            moveup = True#change moveup variable to True as they now want to moveup
                        else:#doesn't want to move so don't move character
                            moveup = None#change moveup to none as the player hasn't clicked yet, so gravity shouldn't effect them yet
                if event.type == pygame.KEYUP:#check if key was released
                        times_clicked += 1#increment times clicked by one
                        if times_clicked != 1:#check if they've clicked either less or more than one
                            moveup = False#change moveup variable to False as they now don't want to moveup
                        else:#hasn't even clicked
                            moveup = None#change moveup to none as the player hasn't clicked yet, so gravity shouldn't effect them yet
                if event.type == SPAWNPIPE:#if the 1300 miliseconds has past
                    pipe_list.extend(create_pipe())#spawn the pipes
        restart = False#make restart false so variables don't keep reassigning    
        

        if moveup == True:#check if player wants to move up
            if main_charactery2  + 20 >= 0:#check if the player isn't near the top of the screen
                main_charactery2 -= up_speed#move the character up by up speed
            else:#player is by the top of the screen
                main_charactery2 -= 0#don't change the y position
        if moveup == False: #player is moving down because of gravity
            main_charactery2 += down_speed#increase y position by down speed
            if main_charactery2 + 245 >= 800:#check if player has hit the ground
                game_state = "ending"#change game state      
        if moveup == None:#check if the moveup is None, meaning the player hasn't clicked yet
            main_charactery2 == main_charactery2#don't change anything

        screen.blit(main_character, [main_characterx2, main_charactery2])#blit the main character onto screen
        font2 = pygame.font.SysFont("Calibri", 50, False, False)#create font for text
        score = int(score)#reintialize the score variable to a different data type
        score_text = font2.render(str(score), True, WHITE)#create text fo the score
        screen.blit(score_text, [185, 100])#blit score text onto screen

        #moving pipes
        pipe_list = move_pipes(pipe_list)#put new position of pipes into pipe list
        draw_pipes(pipe_list)#draw all of the pipes in pipe list
        check_collsion(pipe_list)#check for collision with all of the pipes in pipe list
        
        #start of timer
        total_seconds = frame_count // frame_rate
     
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
    
        # --- Timer going down ---
        # Calculate total seconds
        total_seconds += 1

     
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
     
        # Use python string formatting to format in leading zeros
     
        frame_count += 1  #increment frame count by one
    
        # Check if poles have moved off the screen
    pygame.display.flip()  #update screen 
    clock.tick(60)#control fps


pygame.quit()#quit out of pygame if while loop stops
