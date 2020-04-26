"""
This module lets you experience the POWER of FUNCTIONS and PARAMETERS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_draw_circles()
    # Un-comment the next lines when you are ready to use them.
    run_test_better_draw_circles()
    run_test_even_better_draw_circles()


# ----------------------------------------------------------------------
# READ THIS:
#  The next two functions:
#       draw_circles    run_test_draw_circles
#  are both complete.  Do NOT change them.
#  In a previous exercise, YOU implemented very similar functions.
#
#  In the REST of this exercise (see below), you will implement
#  MORE POWERFUL versions of the   draw_circles   function.
# ----------------------------------------------------------------------

def run_test_draw_circles():
    """ Tests the   draw_circles   function. """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing  draw_circles:  See graphics window')
    print('--------------------------------------------------')
    draw_circles()


def draw_circles():
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
         -- Pauses 0.05 seconds after rendering each.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)

    center = rg.Point(200, 200)
    for k in range(21):
        circle = rg.Circle(center, 10 * k)
        circle.attach_to(window)
        window.render(0.05)  # Pauses for 0.05 seconds after rendering.

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# DONE: 2.
#   First, RUN this program.  You will see that draw_circles draws
#   concentric circles whose radii vary by 10.
#
#   A function that did the same thing as draw_circles, but allowed
#   for the radii to vary by ANY desired amount would be MORE POWERFUL.
#
#   So, implement TWO functions immediately below this comment.
#   They should be called:
#      run_test_better_draw_circles
#      better_draw_circles
#
#   Your   better_draw_circles  function should have a single PARAMETER
#   that is the amount by which the radii of the circles increase.
#   For example, if that parameter is given the value 10,
#   then the circles have radii:  0  10  20  30  40 ... 200, respectively,
#   just as in   draw_circles1.  But if that parameter is given the
#   value 3, the circles have radii:  0  3  6  9  12  ... 60.
#
#   Your  run_test_better_draw_circles function should TEST your new
#   better_draw_circles function, by calling it with different values
#   for its argument.  Don't forget to put a call to
#   run_test_better_draw_circles  in  main.
#
#   You may find that COPY-AND-PASTE of the  draw_circles  and its
#   run_test_draw_circles  may get you started more quickly on your new
#   better_draw_circles  and  run_test_better_draw_circles.
# ----------------------------------------------------------------------


def run_test_better_draw_circles():
    """ Tests the   better_draw_circles   function. """

    print()
    print('--------------------------------------------------')
    print('Testing  better_draw_circles:  See graphics window')
    print('--------------------------------------------------')

    # Test 1: Radius increase by 3
    better_draw_circles(3)

    # Test 2: Radius increase by 10
    better_draw_circles(10)

    # Test 3: Radius increase by 20
    better_draw_circles(20)


def better_draw_circles(number):

    window = rg.RoseWindow(400, 400)

    center = rg.Point(200, 200)
    for k in range(15):
        circle = rg.Circle(center, number * k)
        circle.attach_to(window)
        window.render(0.05)  # Pauses for 0.05 seconds after rendering.

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# DONE: 3.
#   In the previous exercise, you made a MORE POWERFUL version
#   of draw_circles by introducing a PARAMETER for the amount by
#   which the radii of the concentric circles increase.
#
#   In this exercise, implement TWO MORE functions immediately below
#   this comment. They should be called:
#      run_test_even_better_draw_circles
#      even_better_draw_circles
#
#   Your new   even_better_draw_circles  function should have
#   SEVERAL parameters, for allowing the caller to vary what YOU
#   choose to have the caller vary.  For example, you could have
#   parameters for any or all of the following:
#     -- The amount by which the radii vary (as you did above)
#     -- The number of concentric circles drawn
#     -- The center of the concentric circles
#     -- The outline_color of the concentric circles
#     -- The speed at which the animation runs
#    and more.
#
#   A total of any THREE parameters (of your choosing) is enough,
#   although you may have more.
#
#   In testing your even_better_draw_circles function,
#   can you make some fun pictures?
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------


def run_test_even_better_draw_circles():
    """ Tests the   even_better_draw_circles   function. """

    print()
    print('--------------------------------------------------')
    print('Testing  even_better_draw_circles:  See graphics window')
    print('--------------------------------------------------')

    # Test 1: Radius increase by 3, 10 circles, blue color
    even_better_draw_circles(3, 10, 'blue')

    # Test 2: Radius increase by 10, 5 circles, red color
    even_better_draw_circles(10, 5, 'red')

    # Test 3: Radius increase by 20, 10 circles, green color
    even_better_draw_circles(20, 10, 'green')


def even_better_draw_circles(rad_increase, number, color):

    window = rg.RoseWindow(400, 400)

    center = rg.Point(200, 200)
    for k in range(number):
        circle = rg.Circle(center, rad_increase * k)
        circle.outline_color = color
        circle.attach_to(window)
        window.render(0.05)  # Pauses for 0.05 seconds after rendering.

    window.close_on_mouse_click()


main()
