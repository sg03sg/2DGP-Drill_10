from pico2d import load_image, get_time, load_font
import game_world
import game_framework
from random import randint

#속도는 35km/h, 크기는 20cm*20cm

class Bird:
    image = None
    def __init__(self,x = 200, y = 550):
        self.x, self.y =  x,y
        if Bird.image == None:
             Bird.image = load_image('bird.png')
        self.speed = 100

    def update(self): pass


    def handle_event(self, event): pass


    def draw(self):
        Bird.image.draw(self.x, self.y)