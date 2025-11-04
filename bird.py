from pico2d import load_image, get_time, load_font
import game_framework
from random import randint
import json

with open("bird_animation_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

sprites = data["sprites"]

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

#크기는 90cm*90cm
#속도는 35km/h
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 35.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH* 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

#날개짓 속도 1초에 10번
TIME_PER_ACTION =0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION =14
FRAMES_PER_SECOND = FRAMES_PER_ACTION * ACTION_PER_TIME

class Bird:
    image = None
    def __init__(self,x = 1600//2, y = 550):
        self.x, self.y =  x,y
        if Bird.image == None:
             Bird.image = load_image('bird_animation.png')
        self.dir = 1
        self.face_dir = 1
        self.frames = 0

    def update(self):
        self.x,self.dir,self.face_dir =wall_check(self.x,self.dir,self.face_dir)
        self.frames = (self.frames + FRAMES_PER_SECOND *game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time


    def handle_event(self, event): pass

    def draw(self):
        frame_y = Bird.image.h - sprites[int(self.frames)]["y"] - sprites[int(self.frames)]["height"]

        if self.face_dir == 1:
            Bird.image.clip_draw(int(sprites[int(self.frames)]["x"]),int(frame_y),int(sprites[int(self.frames)]["width"]),int(sprites[int(self.frames)]["height"]),self.x, self.y,30,30)
        elif self.face_dir == -1:
            Bird.image.clip_composite_draw(int(sprites[int(self.frames)]["x"]),int(frame_y),int(sprites[int(self.frames)]["width"]),int(sprites[int(self.frames)]["height"]),3.141592, 'v', self.x, self.y,30,30)



