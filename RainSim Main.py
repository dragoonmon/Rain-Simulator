import pygame
import random

class Raindrop(pygame.sprite.Sprite):

    def __init__(self, Colour, Width, Height):

        super().__init__()

        self.image = pygame.Surface([5, 25])
        self.image.fill(Colour)
        self.image.set_alpha(240)

        pygame.draw.rect(self.image, Colour, (0, 0, Width, Height))

        self.rect = self.image.get_rect()

    def Move(self, Vel):
        self.rect.y += Vel





#Define Colours
blue = (166, 212, 227)
white = (240, 240, 240)

#Define variables
ScreenWidth = 700
ScreenHeight = 500
Velocity = 4
Gravity = 1.2
drops = 200
listDrops = []

#initilise pygame
pygame.init()
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Rain Simulation')
clock = pygame.time.Clock()

#Lists for sprites
SpriteList = pygame.sprite.Group()
DropList = pygame.sprite.Group()

#Show Raindrop object
Drop = Raindrop(blue, 1, 25)
Drop.rect.x = random.randrange(0, ScreenWidth)
Drop.rect.y = random.uniform(0, -300) # use uniform to allow for random negative numbers
#Add Drop to the sprite list
SpriteList.add(Drop)

Running = True

while Running:


    DropList.empty()
    for i in range(0, drops):
        NewDrop = Raindrop(blue, 1, 25)
        NewDrop.rect.x = random.randrange(0, ScreenWidth)
        NewDrop.rect.y = random.uniform(0, -300)
        DropList.add(NewDrop)

        for j in DropList:
            if NewDrop.rect.y < ScreenHeight:

                NewDrop.Move(Velocity)


    #Apply gravity to the rain drop
    if Drop.rect.y < ScreenHeight:
        Velocity = Velocity*Gravity
    Drop.Move(Velocity)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False





    Velocity = 4
    SpriteList.update()
    DropList.update()

    Screen.fill(white)

    SpriteList.draw(Screen)
    DropList.draw(Screen)

    pygame.display.update()
    clock.tick(15)
pygame.quit()
quit()