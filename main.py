import pygame as pg

FPS = 60
class Window:
    width = 640; height = 480
    def get_size():
        return (Window.width, Window.height)

pg.init()
screen = pg.display.set_mode(Window.get_size())
clock = pg.time.Clock()

class Button:
    # Конструктор
    def __init__(self, color, x, y, width, height, sc):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = sc
        
    def draw(self): # Рисование кнопки
        pg.draw.rect(self.screen, self.color, \
                     (self.x, self.y, self.width, self.height), \
                     0, border_radius=4)
    
    def isEntry(self, m_x, m_y): # Попала ли мышка в кнопку
        return self.x <= m_x <= self.x + self.width and \
               self.y <= m_y <= self.y + self.height

WHITE = (255, 255, 255)
RED = (0, 200, 200)
btn_yes = Button(color=RED, x=100, y=100, width=100, height=30, sc=screen)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
    
    # Обрабатываем движение мышки  
    mouse_x, mouse_y = pg.mouse.get_pos()
    if btn_yes.isEntry(mouse_x, mouse_y):
        print("In BTN")
    else:
        print("Not in BTN")
    
    btn_yes.draw()
    pg.display.update()

pg.quit()