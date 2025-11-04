from pico2d import *

from boy import Boy
from grass import Grass
from bird import Bird
import game_world

import game_framework


boy = None

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global running

    global bird
    bird_x,bird_y = 1600//2,550

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    for i in range(10):
        if i%2 == 1:
            bird_x = 1600//2 + 25
            bird_y -= 25
        else:
            bird_x = 1600//2
        bird = Bird(bird_x,bird_y)
        game_world.add_object(bird,1)

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

