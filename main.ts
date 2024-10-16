//  Copyright (c) 2020 MTHS All rights reserved
//  Created by: Evan M
//  Created on: October 16
//  This program will show the distance of an object using sonar.
let distance_to_object = 0
//  setup
basic.showIcon(IconNames.Heart)
//  find distance from sonar
function on_button_pressed_a() {
    
    basic.clearScreen()
    distance_to_object = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.Centimeters)
    basic.showNumber(distance_to_object)
    basic.showString("cm")
    basic.showIcon(IconNames.Happy)
}

