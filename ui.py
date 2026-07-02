import pygame
pygame.init()
screen = pygame.display.set_mode((1600,900),vsync=1)


def draw_text(text,size,color,pos):
    img = pygame.font.SysFont("Arial",size).render(text, True, color)
    screen.blit(img,pos)

esc_menu = False

def max(a,b,max=0):
    n = a-b
    if n<max:return max
    return n

class button:
    def __init__(self,pos,size,color):
        self.pos = pos
        self.size = size
        self.color = color
    
    def pressed(self):
        self.pressed = False
    
    def pressed_detect(self):
        
            if pygame.mouse.get_pressed()[0] == True:
                self.pressed = True
            else:
                self.pressed = False

    def over_button(self):
        self.over_button = False
    
    def over_button_detect(self):
        if (
        pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[1] >= self.pos[1] and 
        pygame.mouse.get_pos()[0] <= self.pos[0]+self.size[0] and pygame.mouse.get_pos()[1] <= self.pos[1]+self.size[1]
        ):
            self.over_button = True

        else:
            self.over_button = False

            

                    

    def display(self,text,font_size=30):
        button_surface = pygame.transform.scale(pygame.Surface(self.pos),self.size)
        if self.pressed == False:
            button_surface.fill(self.color)
        else:
            button_surface.fill((max(self.color[0],50),max(self.color[1],50),max(self.color[2],50))) 
        screen.blit(button_surface,self.pos)
      
        if self.over_button == False:
            draw_text(text,font_size,(0,0,0),self.pos)
        else:
            draw_text(text,font_size,(128,128,128),self.pos)
test_button = button((500,500),(170,50),(0,255,0))

         
'''def button(pos,size,color,text,font_size = 30):
    button_surface = pygame.transform.scale(pygame.Surface(pos),size)
    
    
    if (
        pygame.mouse.get_pos()[0] >= pos[0] and pygame.mouse.get_pos()[1] >= pos[1] and 
        pygame.mouse.get_pos()[0] <= pos[0]+size[0] and pygame.mouse.get_pos()[1] <= pos[1]+size[1]
        ):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_surface.fill((max(color[0],50),max(color[1],50),max(color[2],50))) 
                print("mosuedown")
                  
            elif event.type == pygame.MOUSEBUTTONUP:
                button_surface.fill(color)  
                print("mousup")
        screen.blit(button_surface,pos)        
        draw_text(text,font_size,(128,128,128),pos)
    else:
        screen.blit(button_surface,pos)  
        draw_text(text,font_size,(0,0,0),pos)
    '''
    
    
        
       
    
def ui():
    pass
    
while True:
    screen.fill((255,255,255))
    test_button.over_button_detect()
    test_button.pressed_detect()
    test_button.display("hello world")



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.K_ESCAPE:
            esc_menu = True
    pygame.display.flip() 