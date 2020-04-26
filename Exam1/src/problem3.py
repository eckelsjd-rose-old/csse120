"""
Exam 1, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Joshua Eckels.  December 2017.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the  problem3   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 of problem3:    '
    title += '5 squares, alternating green and blue'
    window = rg.RoseWindow(500, 300, title)

    # Test 1:
    problem3(rg.Circle(rg.Point(50, 50), 40),
             rg.Circle(rg.Point(230, 50), 40),
             5, 'green', 'blue', window)

    window.render()  # In case students forget to do so.
    window.continue_on_mouse_click()


###############################################################################
#
# IMPORTANT:  In the following problem:
#   -- Write ONLY the code for a simple PART of the problem.
#        TEST and get it correct.
#   -- Then add ONLY the code for another PART of the problem.
#        TEST and get it correct.
#   -- Etc. writing chunks of code and testing them ** ONE AT A TIME. **
#
###############################################################################
def problem3(left_circle, right_circle, n, color1, color2, window):
    """
    See    problem3_pictures.pdf     for pictures that may help you
    better understand the following specification:

    What comes in:
      -- Two rg.Circle objects, where they have the same radius and the second
           one is guaranteed to be to directly to the right of the first one.
           (Hence, the two rg.Circle's centers have the same y-coordinate.
           See the PDF.)
      -- A positive integer n.
      -- Two strings that are colors (e.g. 'red' or 'green' or ...)
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. Draws the two given rg.Circle objects on the given rg.RoseWindow.
      2. Draws  n  rg.Square objects on the given rg.RoseWindow such that:
           -- The leftmost rg.Square is directly to the right of the first
                (i.e, leftmost) of the two given rg.Circles.
           -- There is an rg.Square directly to the right of the leftmost
                rg.Square, then another rg.Square directly to the right of it,
                and so forth, with the rightmost rg.Square being directly to
                the left of the second (i.e., rightmost) rg.Circle.
           -- All  n  rg.Squares are the same size.
           -- The rg.Squares alternate fill colors, with color1 being the
                fill color for the leftmost rg.Square.  (See the PDF.)

        ** See  problem3_pictures.pdf  for examples. **

      Must render but   ** NOT close **   the window.

    Type hints:
      :type left_circle:  rg.Circle
      :type right_circle: rg.Circle
      :type n:            int
      :type color1:       str
      :type color2:       str
      :type window:       rg.RoseWindow
    """

    left_circle.attach_to(window)
    right_circle.attach_to(window)

    center1 = left_circle.center
    center2 = right_circle.center

    side_length = (center2.x - center1.x - 2 * left_circle.radius) / n

    x1 = center1.x + left_circle.radius + (side_length / 2)
    y1 = center1.y

    for k in range(n):
        value = k + 1
        point1 = rg.Point(x1, y1)
        square1 = rg.Square(point1, side_length)
        square1.attach_to(window)
        if value % 2 == 1:
            square1.fill_color = color1
        else:
            square1.fill_color = color2

        x1 = x1 + side_length

    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function, TESTING each step as you go.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
