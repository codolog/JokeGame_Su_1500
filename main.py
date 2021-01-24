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
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self):
        print("Hello from draw()")

btn_yes = Button()

running = True
while running:
    clock.tick(FPS)
    
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()

pg.quit()