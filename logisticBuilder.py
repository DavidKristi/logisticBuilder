import pygame
import msvcrt
import time

pygame.init()

displayWidth = 800
displayHeight = 600

rectangleSize = [50,50]
rectanglePosition = [0,0]
speed = 200

surface = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("Image")
straightRail = pygame.image.load("game\Rail Road Straight-1.png")

time0 = time.time()
time1 = 0

def get_dt():
    global time0, time1
    time1 = time.time()
    dt = time1 - time0
    time0 = time1
    return dt

class keyboard():

    def getMovement(self):
        dt = get_dt()
        vertical = 0
        horizontal = 0
        if pygame.key.get_pressed()[pygame.K_UP]:
            vertical -= speed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            vertical += speed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            horizontal -= speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            horizontal += speed
        vertical = vertical*dt
        horizontal = horizontal*dt
        return (horizontal, vertical)

class entityElement():
    
    def __init__(self, typeNumber, position):
        self.typeNumber = typeNumber
        self.position = position

class entityController():

    def __init__(self):
        self.list = []

    def append(self,object):
        if type(object) is entityElement:
            self.list.append(object)

    def getList(self):
        return self.list

dictionary = [straightRail]
keyboard = keyboard()
entity = entityController()

while True : 
  
    surface.fill((255,255,255))  

    for eachEntity in entity.getList():
        surface.blit(dictionary[eachEntity.typeNumber], eachEntity.position)
         
    pygame.draw.rect(surface, (0,0,0), (rectanglePosition[0], rectanglePosition[1], rectangleSize[0], rectangleSize[1]))
  
    for event in pygame.event.get() : 
   
        if event.type == pygame.QUIT : 
            pygame.quit()  
            quit() 
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_x]:
                entity.append(entityElement(0, (rectanglePosition[0]+rectangleSize[0], rectanglePosition[1]+rectangleSize[1])))
    
    
    
    movement = keyboard.getMovement()
    rectanglePosition[0] += movement[0]
    rectanglePosition[1] += movement[1]


    pygame.display.update()  