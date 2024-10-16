# Copyright (c) 2020 MTHS All rights reserved
# Created by: Evan M
# Created on: October 16
# This program will show the distance of an object using sonar.

distance_to_object = 0

# setup
basic.show_icon(IconNames.HEART)

# find distance from sonar
def on_button_pressed_a():
    global distance_to_object
    basic.clear_screen()
    distance_to_object = sonar.ping(
        DigitalPin.P1,
        DigitalPin.P2,
        PingUnit.CENTIMETERS
    )
    basic.show_number(distance_to_object)
    basic.show_string("cm")
    basic.show_icon(IconNames.HAPPY)