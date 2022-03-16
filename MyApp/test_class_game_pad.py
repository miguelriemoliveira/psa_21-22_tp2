#!/usr/bin/env python3
import time
from ClassGamePad import ClassGamePad

# --------------------------------
# Initialization
# --------------------------------
game_pad = ClassGamePad()
game_pad.connect(0)

# --------------------------------
# Execution (in cycle)
# --------------------------------
while True:

    game_pad.getData()

    print('Axix0 = ' + str(game_pad.axis0) + ' Axis1 = ' + str(game_pad.axis1))

    time.sleep(0.01)

# --------------------------------
# Termination
# --------------------------------
