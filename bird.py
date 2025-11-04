from pico2d import load_image, get_time, load_font
import game_world
import game_framework
from random import randint

def wall_check(x,dir,face_dir):
    if x < 25:
        x = 25
        dir*= -1
        face_dir *= -1
    elif x > 1600 - 25:
        x = 1600 - 25
        dir *= -1
        face_dir *= -1
    return x,dir,face_dir


#속도는 35km/h, 크기는 20cm*20cm

class Bird:
    image = None
    def __init__(self,x = 200, y = 550):
        self.x, self.y =  x,y
        if Bird.image == None:
             Bird.image = load_image('bird.png')
        self.dir = 1
        self.face_dir = 1

    def update(self):
        self.x,self.dir,self.face_dir =wall_check(self.x,self.dir,self.face_dir)
        pass


    def handle_event(self, event): pass


    def draw(self):
        Bird.image.draw(self.x, self.y)