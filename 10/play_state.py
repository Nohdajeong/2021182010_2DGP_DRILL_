from pico2d import *

import logo_state
import item_state
import add_delete_state
import game_framework


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1    # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.boys = None
        self.item = None


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)

        if self.boys == 'Plus':
            boy.draw()
        elif self.boys == 'Delete':
            del boy

        self.boy_character()

    def boy_character(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_b:
                    game_framework.push_state(add_delete_state)
                case pico2d.SDLK_LEFT:
                    boy.dir -= 1
                case pico2d.SDLK_RIGHT:
                    boy.dir += 1
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    boy.dir += 1
                    boy.face_dir = -1
                case pico2d.SDLK_RIGHT:
                    boy.dir -= 1
                    boy.face_dir = 1




boy = None #굳이 c로 따지면 NULL
grass = None
running = True

#초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

# finalization code
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    boy.draw()


def pause():
    pass

def resume():
    pass
