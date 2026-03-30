import pygame 
pygame .init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Rectangle example in pygame")

class rect():
    def __init__(self,color,dimension):
        self.rect_surface = screen
        self.colour = color
        self.rect_dimension = dimension

    
    def draw (self):
        self.draw_rect = pygame.draw.rect(self.rect_surface,self.colour,self.rect_dimension)




run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    R = rect("red",(100,100,50,50))
    R.draw()        
    pygame.display.update()