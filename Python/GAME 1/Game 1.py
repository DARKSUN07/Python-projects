import pygame

# initilising pygame
pygame.init()

screen_width = 800
screen_height = 800


#define game variables
tile_size = 80

#Images
BG=pygame.image.load("BG.jpg")

def draw_grid():
    for line in range(0, 11):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


# creating infinite loop with quit button
def run():
    while True:
        
        screen.blit(BG,(0,0))

        draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
        pygame.display.update()

# creating screen
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("First Game")
icon=pygame.image.load("football.png")
pygame.display.set_icon(icon)
run()


