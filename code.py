#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# Makes a sprite move on circuit python

import ugame
import stage
import constants


def menu_scene():

    image_bank_1 = stage.Bank.from_bmp16("ball.bmp")

    background = stage.Grid(image_bank_1, 10, 8)

    sprites = []

    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text1.move(58, 10)
    text1.text("JOJOS")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text2.move(43, 110)
    text2.text("APPROACH?")
    text.append(text2)

    text3 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text3.move(13, 20)
    text3.text("BIZZARE ADVENTURE")
    text.append(text3)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]

    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)
        if keys & ugame.K_START != 0:
            game_scene()

def game_scene():
    
    image_bank_1 = stage.Bank.from_bmp16("ball.bmp")
    sprites = []
    
    # this sets the background
    a_button = constants.button_state["button_up"]

    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank_1, image # in bank, x, y)
    ball_one = stage.Sprite(image_bank_1, 3, 64, 56)
    sprites.append(ball_one)
    ball_two = stage.Sprite(image_bank_1, 2, 75, 56)
    sprites.insert(0, ball_two)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = sprites + [background]

    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_UP != 0:
            if ball_one.y < 0:
                ball_one.move(ball_one.x, 0)
            else:
                ball_one.move(ball_one.x, ball_one.y - 
                              constants.SPRITE_MOVEMENT_SPEED)
            pass
        if keys & ugame.K_DOWN != 0:
            if ball_one.y > constants.SCREEN_Y - constants.SCREEN_GRID_Y:
                ball_one.move(ball_one.x, constants.SCREEN_Y -
                              constants.SPRITE_SIZE)
            else:
                ball_one.move(ball_one.x, ball_one.y +
                              constants.SPRITE_MOVEMENT_SPEED)
            pass
        if keys & ugame.K_LEFT != 0:
            if ball_one.x < 0:
                ball_one.move(0, ball_one.y)
            else:
                ball_one.move(ball_one.x - constants.SPRITE_MOVEMENT_SPEED,
                              ball_one.y)
            pass
        if keys & ugame.K_RIGHT != 0:
            if ball_one.x > constants.SCREEN_X - constants.SCREEN_GRID_X:
                ball_one.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                              ball_one.y)
            else:
                ball_one.move(ball_one.x + constants.SPRITE_MOVEMENT_SPEED, 
                              ball_one.y)
            pass
        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw sprtie list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()
