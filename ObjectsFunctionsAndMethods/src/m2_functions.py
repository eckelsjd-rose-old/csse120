"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""

########################################################################
#
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE and...
#
#   Allow this file to use the rosegraphics.py file by marking the src
#   directory as a "Sources Root".  Do that by right clicking on the src folder,
#   then selector  Mark Directory As --> Sources Root
#
#   Expand the import lines below and watch the red underlines disappear as you do that step.
#   You will do that once for every project that uses rosegraphics so get used to it. :)
#
#   Then run this module and look for more TO DO's later in the file.
########################################################################

import rosegraphics as rg
import random


def main():
    """
    Makes a TurtleWindow,
    calls the other functions in this module to demo them, and
    waits for the user to click anywhere in the window to close it.
    """
    # A TurtleWindow works "behind the scenes" to enable Turtle movement
    window = rg.TurtleWindow()

    turtle1()
    turtle4()
    turtle3()
    turtle2()
    turtle2()
    turtle5()

    window.close_on_mouse_click()


def turtle1():
    """
    Constructs a square SimpleTurtle.
    Makes that SimpleTurtle draw a yellow-filled circle.
    """
    ada = rg.SimpleTurtle('square')

    ada.pen = rg.Pen('aquamarine', 30)
    ada.paint_bucket = rg.PaintBucket('yellow')

    ada.begin_fill()
    ada.draw_circle(150)
    ada.end_fill()


def turtle2():
    """
    Constructs a triangle SimpleTurtle.
    Makes that SimpleTurle go to a RANDOM point,
    draws a cool shape, and return to where it started from.
    """
    grace = rg.SimpleTurtle('triangle')

    grace.pen = rg.Pen('blue', 15)
    grace.paint_bucket = rg.PaintBucket('magenta')

    # Keep track of where I am, to go back to it at the end.
    # Then choose a RANDOM starting point for the motion in here.
    i_began_here = rg.Point(grace.x_cor(), grace.y_cor())
    i_am_going_here = rg.Point(random.randrange(-500, 500),
                               random.randrange(-300, 0))
    grace.pen_up()
    grace.go_to(i_am_going_here)
    grace.pen_down()

    # Do the motion.
    grace.left(90)
    grace.forward(200)
    grace.begin_fill()
    grace.draw_circle(25)
    grace.end_fill()

    # Go back to where I was when this function began its run.
    grace.go_to(i_began_here)


def turtle3():
    """
    Constructs a default SimpleTurtle.
    Makes that SimpleTurtle go forward 300 units
    and then draw a black-filled circle.
    """
    maja = rg.SimpleTurtle()
    maja.pen = rg.Pen('black', 10)

    maja.forward(300)

    maja.begin_fill()
    maja.draw_circle(50)
    maja.end_fill()


def turtle4():

    michael = rg.SimpleTurtle()
    michael.pen = rg.Pen('YellowGreen', 25)

    michael.forward(450)

    michael.begin_fill()
    michael.draw_square(50)
    michael.end_fill()


def turtle5():

    james = rg.SimpleTurtle()
    james.pen = rg.Pen('blue',40)

    scott = rg.SimpleTurtle()
    scott.pen = rg.Pen('red', 10)

    james.left(90)
    scott.right(90)
    james.forward(100)
    scott.forward(100)



########################################################################
#
# DONE: 2.
#   READ the code above.  Be sure you understand:
#     -- How many functions are defined above?
#           (Answer: 4)
#     -- For each function definition:
#          -- Where does that function definition begin?
#             Where does it end?
#     -- How many times does   main   call the   turtle1   function?
#            (Answer: 1)
#     -- How many times does   main   call the   turtle2   function?
#            (Hint: the answer is NOT 1.)    twice
#     -- What line of code calls the   main   function?
#            (Answer: look at the LAST line of this module, far below.)   line 225
#
#     ** ASK QUESTIONS if you are uncertain. **
#
#   RELATE what is DRAWN to the CODE above.  Be sure you understand:
#       -- WHEN does the code in   main   run?
#       -- WHEN does the code in   turtle1   run?
#                    the code in   turtle2   run?
#                    the code in   turtle3   run?
#       -- For each of the above, WHY does that code run when it does?
#
#     ** ASK QUESTIONS if you are uncertain. **
#
#   When you believe you understand the answers
#   to all of the above questions, change the above TO DO to DONE.
#
########################################################################

########################################################################
#
# DONE: 3.
#   Define another function,
#   immediately below the end of the definition of   turtle3   above.
#   Name your new function   turtle4.
#
#   The Python "pep8" coding standard says to leave exactly 2 blank
#   lines between function definitions, so be sure to do so.
#
#   Your new function should:
#    1. Define a SimpleTurtle (as   turtle3   as other functions did).
#    2. Set your SimpleTurtle's
#               pen
#       to a new rg.Pen with a color and thickness of your own choosing.
#       See the COLORS.txt  file in this project for a list of legal color-names.
#    3. Make your SimpleTurtle move around a bit.
#
# ----------------------------------------------------------------------
#           ** IMPORTANT:                 **
#           ** Nothing fancy is required. **
#           ** Save fancy stuff for exercises later today. **
# ----------------------------------------------------------------------
#
#   BTW, if you see a RED underline, that means that there is
#     a SYNTAX (notation) error at that line or elsewhere.
#   Get help as needed to fix any such errors.
#
########################################################################

########################################################################
#
# DONE: 4.
#   Add a line to   main   that CALLS your new function immediately
#   AFTER  main  calls turtle1.  So:
#     -- the SimpleTurtle from turtle1 should move,
#     -- then YOUR SimpleTurtle should move,
#     -- then the other 3 SimpleTurtles should move.
#
#   Run this module.  Check that there is another SimpleTurtle (yours)
#   that uses the pen you chose and moves around a bit.
#   If your code has errors (shows RED in the Console window)
#   or does not do what it should, get help as needed to fix it.
#
########################################################################

########################################################################
#
# DONE: 5.
#   The previous two TODOs IMPLEMENTED a function (TO DO 3)
#   and TESTED that function (TO DO 4).
#
#   Now implement AND test one more function, defining it immediately
#   below the definition of your   turtle4   function.
#   Name your new function   turtle5.
#
#   The Python "pep8" coding standard says to leave exactly 2 blank
#   lines between function definitions, so be sure to do so.
#
#   Your new function should define TWO new SimpleTurtles,
#   set their characteristics (i.e., instance variables) as you choose,
#   and make each move a bit.
#
# ----------------------------------------------------------------------
#           ** IMPORTANT:                 **
#           ** Nothing fancy is required. **
#           ** Save fancy stuff for exercises later today. **
# ----------------------------------------------------------------------
#
#  Get help as needed on this (and every!) exercise!
#
#  As always COMMIT and Push your work as often as you want, but for sure after
#  you have tested it and believe that it is correct.
#
#   Reminder of those steps...
#   COMMIT your work by selecting VCS from the menu bar, then select Commit Changes
#   Make sure only the files you want to commit are checked and optionally
#   add a quick Commit message to describe your work.  Then hover over the
#   Commit button and select Commit and Push.  Commit saves the work to
#   your computer.  "and Push" saves a copy of your work up into your Github
#   repository (saving to the cloud is a better way to permanently safe work).
#
########################################################################

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
