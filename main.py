import pygame
import time
pygame.init()
size = (400, 600)
screen = pygame.display.set_mode(size)


main_characterx = 40
main_charactery = 350
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY_BLUE = (3, 252, 252)
BLACK = (0, 0, 0)

done = False

main_character = pygame.image.load("jetpackman.png")
main_character = pygame.transform.scale(main_character, [150, 175])

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, [400, 600])

def starting_screen():
    main_characterx = 120
    main_charactery = 280
    screen.fill(WHITE)
    font = pygame.font.Font("FlappybirdyRegular-KaBW.ttf", 100)
    intro_text = font.render("Flappy Joyride", True, BLACK)
    intro_text2 = font.render("Click to play", True, BLACK)
    screen.blit(intro_text, [25, 200])
    screen.blit(main_character, [main_characterx, main_charactery])
    main_charactery -= 2
    time.sleep(60)
    main_charactery += 2
    screen.blit(intro_text2, [35, 480])
    pygame.display.flip()

def playing_screen():
    screen.fill(BLACK)
    pygame.display.flip()

while not done:
    starting_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            playing_screen()

pygame.quit()