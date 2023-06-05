import pygame
pygame.init()
size = (400, 600)
screen = pygame.display.set_mode(size)

collided = False

main_characterx2 = 60
main_charactery2 = 250

score = 0
times_clicked = 0

sidewalk_x = 0

up_speed = 10
down_speed = 3

moveup = None

skyscraper_xpos = 450
skyscraper_ypos = 0

skyscraper2_xpos = 450
skyscraper2_ypos = 250


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY_BLUE = (3, 252, 252)
BLACK = (0, 0, 0)

playing = False
done = False
if_starting = True
if_playing = False
if_ending = False

font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)


background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, [400, 600])

intro_text = pygame.image.load("Screen Shot 2023-06-04 at 11.02.54 AM.png")
intro_text = pygame.transform.scale(intro_text, [400, 400])

skyscraper = pygame.image.load("building.png")
skyscraper = pygame.transform.scale(skyscraper, [150, 100])

skyscraper2 = pygame.image.load("building2.png")
skyscraper2 = pygame.transform.scale(skyscraper2, [150, 350])

sidewalk = pygame.image.load("Sidewalk.jpg")
sidewalk = pygame.transform.scale(sidewalk, [600, 100])

clock = pygame.time.Clock()


def ending_screen():
    global done
    global font
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


def starting_screen():
    global if_starting
    global if_playing
    global done
    global times_clicked
    main_character = pygame.image.load("jetpackman.png")
    main_character = pygame.transform.scale(main_character, [150, 175])
    main_characterx1 = 120
    main_charactery1 = 280
    screen.blit(background, [0, 0])
    screen.blit(intro_text, [1, 200])
    screen.blit(main_character, [main_characterx1, main_charactery1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            times_clicked += 1
            if_starting = False
            if_playing = True

    pygame.display.flip()


def playing_screen():
    global collided
    global skyscraper_xpos
    global skyscraper2_xpos
    global skyscraper2_ypos
    global skyscraper2_ypos
    global times_clicked
    global score
    global done
    global moveup
    global main_characterx2
    global main_charactery2
    global if_playing
    global if_ending
    global sidewalk_x
    screen.blit(background, [0, 0])
    screen.blit(sidewalk, [sidewalk_x, 500])
    sidewalk_x -= 1
    if sidewalk_x + 600 < 600:
        sidewalk_x = 0
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
      
    if moveup == True:
        main_charactery2 -= up_speed
    if moveup == False: 
        main_charactery2 += down_speed
        if main_charactery2 + 290 >= 800:
            if_playing = False 
            if_ending = True       
    if moveup == None:
        main_charactery2 == main_charactery2
    screen.blit(skyscraper, [skyscraper_xpos, skyscraper_ypos])
    screen.blit(skyscraper2, [skyscraper2_xpos, skyscraper2_ypos])
    screen.blit(main_character, [main_characterx2, main_charactery2])
    font2 = pygame.font.SysFont("Calibri", 50, False, False)
    score_text = font2.render(str(score), True, WHITE)
    screen.blit(score_text, [185, 100]) 
    if collided != True:
        skyscraper2_xpos -= 2
        skyscraper_xpos -= 2
    pygame.display.flip()


while not done:
    if if_starting:
        starting_screen()
    if if_playing:
        main_character = pygame.image.load("jetpackman.png")
        main_character = pygame.transform.scale(main_character, [100, 100]) 
        playing_screen()
    if if_ending:
        ending_screen()
    clock.tick(60)

pygame.quit()
