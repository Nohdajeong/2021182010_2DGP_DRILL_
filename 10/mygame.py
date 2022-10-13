import pico2d
import game_framework

import play_state
import logo_state
import item_state
import add_delete_state

pico2d.open_canvas()
#game_framework.run(item_state)
game_framework.run(play_state)
#game_framework.run(add_delete_state)
pico2d.close_canvas()
