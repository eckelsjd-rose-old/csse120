"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg
window = rg.TurtleWindow()

Turtle1 = rg.SimpleTurtle()
Turtle2 = rg.SimpleTurtle('turtle')

Turtle1.pen = rg.Pen('red', 10)
Turtle2.pen = rg.Pen('blue', 20)

for k in range(7):

    Turtle1.forward(300)
    Turtle1.pen_up()
    Turtle1.backward(300)
    Turtle1.right(90)
    Turtle1.forward(25)
    Turtle1.left(90)
    Turtle1.pen_down()

for k in range(5):

    Turtle2.forward(100)
    Turtle2.backward(100)
    Turtle2.right(90)
    Turtle2.forward(12.5)
    Turtle2.left(90)

Turtle2.forward(100)

window.close_on_mouse_click()



