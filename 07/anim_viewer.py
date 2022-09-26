from pico2d import *
open_canvas()
character = load_image('character2.png')

x = 0
frame = 0
while(x < 800):
    clear_canvas()
    character.clip_draw(frame*100, 0, 110, 400, x, 200)
    update_canvas()
    frame = (frame + 1) % 12
    x += 3
    delay(0.05)
    get_events()


close_canvas()

