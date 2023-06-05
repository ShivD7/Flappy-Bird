import pygame
pygame.init()
size = (400, 600)
screen = pygame.display.set_mode(size)

main_characterx2 = 60
main_charactery2 = 250

score = 0
times_clicked = 0

moveup = None

skyscraper_xpos = 450
skyscraper_ypos = 400

skyscraper2_xpos = 450
skyscraper2_ypos = 0


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY_BLUE = (3, 252, 252)
BLACK = (0, 0, 0)

playing = False
done = False
if_starting = True
if_playing = False

font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)

main_character = pygame.image.load("jetpackman.png")
main_character = pygame.transform.scale(main_character, [150, 175])

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, [400, 600])

intro_text = pygame.image.load("Screen Shot 2023-06-04 at 11.02.54 AM.png")
intro_text = pygame.transform.scale(intro_text, [400, 400])

skyscraper = pygame.image.load("building.png")
skyscraper = pygame.transform.scale(skyscraper, [150, 200])

skyscraper2 = pygame.image.load("building2.png")
skyscraper2 = pygame.transform.scale(skyscraper2, [150, 200])

clock = pygame.time.Clock()



def starting_screen():
    global if_starting
    global if_playing
    global done
    global times_clicked
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
    clock.tick(60)


def playing_screen():
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
    screen.blit(background, [0, 0]) 
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
        main_charactery2 -= 20
    if moveup == False: 
        main_charactery2 += 10
    if moveup == None:
        main_charactery2 == main_charactery2
    

    screen.blit(skyscraper, [skyscraper_xpos, skyscraper_ypos])
    screen.blit(skyscraper2, [skyscraper2_xpos, skyscraper2_ypos])
    screen.blit(main_character, [main_characterx2, main_charactery2])
    font2 = pygame.font.SysFont("Calibri", 50, False, False)
    score_text = font2.render(str(score), True, WHITE)
    screen.blit(score_text, [185, 100]) 
    skyscraper2_xpos -= 2
    skyscraper_xpos -= 2
    pygame.display.flip()
    clock.tick(60)

while not done:
    if if_starting:
        starting_screen()
    if if_playing:
        playing_screen()

    clock.tick(60)

pygame.quit()
