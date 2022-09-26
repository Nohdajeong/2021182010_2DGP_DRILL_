from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0


while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)
        
while(y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y+90)
        y = y + 2
        delay(0.01)

while(x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x = x - 2
        delay(0.01)

while(y > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y+90)
        y = y - 2
        delay(0.01)

while(x > 0, y > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x+400,y+90)
        x = x + math.sin( 270 / 360 * 2 * math.pi)
        y = y - math.sin( 270 / 360 * 2 * math.pi)
        delay(0.01)
    
        
close_canvas()
