"""
Exam 1, problem 2.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Joshua Eckels.  December 2017.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2()


def run_test_problem2():
    """ Tests the   problem2   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem2  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 and 2 of problem2'
    window = rg.RoseWindow(400, 250, title)

    # Test 1:
    circle1 = rg.Circle(rg.Point(100, 100), 75)
    circle1.outline_thickness = 5
    circle1.outline_color = 'blue'
    problem2(circle1, 'forest green', window)

    window.render()  # In case students forget to do so.
    window.continue_on_mouse_click()

    # Test 2:
    circle2 = rg.Circle(rg.Point(250, 100), 40)
    circle2.fill_color = 'grey'
    circle2.outline_thickness = 3
    problem2(circle2, 'red', window)

    window.render()  # In case students forget to do so.
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem2'
    window = rg.RoseWindow(300, 300, title)

    # Test 3:
    circle3 = rg.Circle(rg.Point(150, 150), 100)
    circle3.outline_thickness = 15
    circle3.outline_color = 'purple'
    circle3.fill_color = 'yellow'
    problem2(circle3, 'blue', window)

    window.render()  # In case students forget to do so.
    window.close_on_mouse_click()


###############################################################################
#
# IMPORTANT:  In the following problem:
#   -- Write ONLY the code for Step 1 of the Side Effects below.
#        TEST and get it correct.
#   -- Then add ONLY the code for Step 2 of the Side Effects below.
#        TEST and get it correct.
#   -- Etc. for Steps 3, 4 and 5, ** ONE AT A TIME. **
#
# NOTE:
#   Step 6 below (printing a "bounding box") counts only 1 point!
#   If you are having trouble with Step 6, move on and come back later.
#
###############################################################################
def problem2(circle, color, win):
    """
    See   problem2_pictures.pdf   for pictures that may help you
    better understand the following specification:

    What comes in:
      -- An rg.Circle.
      -- A string suitable for a RoseGraphics color, e.g. 'red'
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).

    Side effects:

      1. Draws the given rg.Circle on the given rg.RoseWindow.

      2. Draws an rg.Rectangle such that [SEE THE PDF for a helpful picture]:
           -- its left edge goes from the top of the given rg.Circle
                to the bottom of the given rg.Circle
           -- its right edge is  100  pixels to the right of its left edge

      3.   Where the outline thickness of the rg.Rectangle is 8,

      4.   And its outline color is the given color,

      5.   And its FILL color is the same as the OUTLINE color
             of the given rg.Circle.

      6. Then, using ONE LINE OF CODE, print (on the console) what is called
           the "bounding box" of the given rg.Circle.
           [STEP 6 COUNTS ONLY 1 POINT.  DON'T GET STUCK ON THIS STEP!]

      Must render but   ** NOT close **   the window.

    Type hints:
      :type circle: rg.Circle
      :type color:  str
      :type win:    rg.RoseWindow
    """

    circle.attach_to(win)

    center1 = circle.center

    point_top = rg.Point(center1.x, center1.y - circle.radius)
    point_bottom = rg.Point(center1.x + 100, center1.y + circle.radius)

    rectangle = rg.Rectangle(point_top, point_bottom)
    rectangle.attach_to(win)
    rectangle.outline_thickness = 8
    rectangle.outline_color = color
    rectangle.fill_color = circle.outline_color

    print(circle.get_bounding_box())

    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function, TESTING each step as you go.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
