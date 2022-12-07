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
displayImage = pygame.image.load(".\game\demoGreen.jpg") 

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

keyboard = keyboard()

while True : 
  
    surface.fill((255,255,255))   
    pygame.draw.rect(surface, (0,0,0), (rectanglePosition[0], rectanglePosition[1], rectangleSize[0], rectangleSize[1]))
  
    for event in pygame.event.get() : 
   
        if event.type == pygame.QUIT : 
  
   
            pygame.quit()  
            quit() 
    
    movement = keyboard.getMovement()
    rectanglePosition[0] += movement[0]
    rectanglePosition[1] += movement[1]


    pygame.display.update()  