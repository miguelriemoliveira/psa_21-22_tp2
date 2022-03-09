#!/usr/bin/env python3
import pygame

# --------------------------------
# Initialization
# --------------------------------
pygame.init()
pygame.joystick.init() # Initialize the joysticks.

# --------------------------------
# Execution (in cycle)
# --------------------------------
while True:

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()
    print('Number of joysticks ' + str(joystick_count))

    # Assuming that we have only one joystick connected
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Get the name from the OS for the controller/joystick.
    name = joystick.get_name()
    print('Joystick name is ' + name)

    number_of_axes = joystick.get_numaxes()
    print('Joystick has ' + str(number_of_axes) + ' axes.')

    values = []
    for axis_idx in range(number_of_axes):
        axis_value = joystick.get_axis(axis_idx)
        values.append(axis_value)

    print('Axes values = ' + str(values))

# --------------------------------
# Termination
# --------------------------------
pygame.quit()