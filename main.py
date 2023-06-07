import pygame
import random
import time
pygame.init()
size = (400, 600)
screen = pygame.display.set_mode(size)

game_state = "intro"

collided = False
drawing_poles = False

main_characterx2 = 60
main_charactery2 = 250

score = 0
times_clicked = 0



up_speed = 5
down_speed = 3

moveup = None

skyscraper_xpos = 650
skyscraper_ypos = 0

skyscraper2_xpos = 650
skyscraper2_ypos = 250

skyscraper3_xpos = 650
skyscraper3_ypos = 0

skyscraper4_xpos = 650
skyscraper4_ypos = 480

skyscraper5_xpos = 650
skyscraper5_ypos = 0

skyscraper6_xpos = 650
skyscraper6_ypos = 400


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY_BLUE = (3, 252, 252)
BLACK = (0, 0, 0)

playing = False
done = False

font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)


background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, [400, 600])

intro_text = pygame.image.load("Screen Shot 2023-06-04 at 11.02.54 AM.png")
intro_text = pygame.transform.scale(intro_text, [400, 400])

skyscraper = pygame.image.load("building2.png")
skyscraper = pygame.transform.scale(skyscraper, [100, 100])
skyscraper2 = pygame.image.load("building2.png")
skyscraper2 = pygame.transform.scale(skyscraper2, [100, 350])

skyscraper3 = pygame.image.load("building2.png")
skyscraper3 = pygame.transform.scale(skyscraper3, [100, 370])
skyscraper4 = pygame.image.load("building.png")
skyscraper4 = pygame.transform.scale(skyscraper4, [100, 120])

skyscraper5 = pygame.image.load("building2.png")
skyscraper5 = pygame.transform.scale(skyscraper5, [100, 230])
skyscraper6 = pygame.image.load("building2.png")
skyscraper6 = pygame.transform.scale(skyscraper6, [100, 230])

skyscraper_list = [[skyscraper], [skyscraper2],
                   [skyscraper3], [skyscraper4],
                   [skyscraper5], [skyscraper6]]

sidewalk = pygame.image.load("Sidewalk.jpg")
sidewalk = pygame.transform.scale(sidewalk, [600, 100])

sidewalk_x = 0
sidewalk_x2 = sidewalk.get_width()

clock = pygame.time.Clock()


def infinite_sidewalk():
    screen.blit(sidewalk, [sidewalk_x, 500])
    screen.blit(sidewalk, [sidewalk_x2, 500])



while not done:
    if game_state == "intro":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                times_clicked += 1
                game_state = "playing"
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
