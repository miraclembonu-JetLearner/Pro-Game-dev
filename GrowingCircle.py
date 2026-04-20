import pygame
pygame.init()

window = pygame.display.set_mode((400,400))

window.fill("white")

class GrowingCircle():
    def __init__(self,color,position,radius,width):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(window,self.color,self.position,self.radius,self.width)

    def grow(self,r):
        self.radius += r
        pygame.draw.circle(window,self.color,self.position,self.radius,self.width)

c = GrowingCircle("red",(200,200),20,3)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.fill("white")
            c.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            window.fill("white")
            c.grow(10)
            pygame.display.update()
        elif event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
           
    