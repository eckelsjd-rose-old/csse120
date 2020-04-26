"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math

# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_draw_squares_from_circle()
    run_test_draw_circles_from_rectangle()
    run_test_draw_lines_from_rectangles()


def run_test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_squares_from_circle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: '
    title = title + ' 7 little squares from green circle, 4 big squares'
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = 'green'
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_SQUARES_FROM_CIRCLE: '
    title += ' 20 teeny squares from blue circle!'
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = 'blue'
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n: int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """

    start_point = circle.center
    x = start_point.x
    y = start_point.y
    length = 2 * circle.radius

    circle.attach_to(window)

    for k in range(n):
        center_square = rg.Point(x, y)
        square = rg.Square(center_square, length)
        square.attach_to(window)

        x = x + circle.radius
        y = y + circle.radius

    window.render()

    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------


def run_test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_circles_from_rectangle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_CIRCLES_FROM_RECTANGLE: '
    window1 = rg.RoseWindow(720, 500, title)

    # Test 1:
    rectangle = rg.Rectangle(rg.Point(400, 250), rg.Point(440, 325))
    rectangle.fill_color = 'green'
    rectangle.outline_thickness = 5
    rectangle.outline_color = 'black'
    draw_circles_from_rectangle(4, 5, rectangle, window1)

    # Test 2:
    rectangle = rg.Rectangle(rg.Point(500, 450), rg.Point(600, 400))
    rectangle.fill_color = 'blue'
    rectangle.outline_thickness = 3
    rectangle.outline_color = 'red'
    draw_circles_from_rectangle(8, 3, rectangle, window1)

    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_CIRCLES_FROM_RECTANGLE: '
    window2 = rg.RoseWindow(620, 380, title)

    # Test 3:
    rectangle = rg.Rectangle(rg.Point(350, 280), rg.Point(375, 330))
    rectangle.fill_color = 'yellow'
    rectangle.outline_thickness = 5
    rectangle.outline_color = 'brown'
    draw_circles_from_rectangle(6, 10, rectangle, window2)

    window2.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 3. Implement this TEST function.
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #
    ####################################################################
    # HINT: Consider using the same test cases as suggested by the
    #   pictures in  draw_circles_from_rectangle.pdf   in this project.
    #   Follow the same form as the example in a previous problem.
    ####################################################################
    # ------------------------------------------------------------------


def draw_circles_from_rectangle(m, n, rectangle, window):
    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m: int
      :type n: int
      :type rectangle: rg.Rectangle
      :type window: rg.RoseWindow
    """

    rectangle.attach_to(window)

    start_point = rectangle.get_center()
    x = start_point.x
    y = start_point.y

    corner1 = rectangle.corner_1  # corner 1 needs to be left most corner in
    # test case
    xC1 = corner1.x
    yC1 = corner1.y

    corner2 = rectangle.corner_2   # corner 2 needs to be right most corner
    # in test case
    xC2 = corner2.x
    yC2 = corner2.y

    radius_left = math.fabs(yC1 - yC2)/2
    radius_top = math.fabs(xC1 - xC2)/2

    xCL = xC1 - radius_left
    yCL = y

    xCT = x
    yCT = y - math.fabs((yC1 - yC2)/2) - radius_top

    for k in range(m):
        center_left = rg.Point(xCL, yCL)
        circle1 = rg.Circle(center_left, radius_left)
        circle1.fill_color = rectangle.fill_color
        circle1.outline_color = rectangle.outline_color
        circle1.attach_to(window)

        xCL = xCL - (2 * radius_left)

    for k in range(n):
        center_top = rg.Point(xCT, yCT)
        circle = rg.Circle(center_top, radius_top)
        circle.outline_color = rectangle.outline_color
        circle.attach_to(window)

        yCT = yCT - (2 * radius_top)

    window.render()

    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------


def run_test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines_from_rectangles  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:'
    title += '  5 lines, 8 lines!'
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = 'red'
    rectangle2.outline_color = 'blue'
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1)

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = 'green'
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1)

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!'
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = 'brown'
    rectangle2.outline_color = 'cyan'
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2)

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window):
    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
      """

    rectangle1.attach_to(window)
    rectangle2.attach_to(window)

    center_1 = rectangle1.get_center()
    corner1_rect1 = rectangle1.corner_1
    corner2_rect1 = rectangle1.corner_2

    center_2 = rectangle2.get_center()

    dx = math.fabs(corner2_rect1.x - corner1_rect1.x)/2
    dy = math.fabs(corner2_rect1.y - corner1_rect1.y)/2

    x1 = center_1.x
    y1 = center_1.y

    x2 = center_2.x
    y2 = center_2.y

    for k in range(n):
        center1 = rg.Point(x1, y1)
        center2 = rg.Point(x2, y2)
        line = rg.Line(center1, center2)
        line.thickness = 5
        if (k+1) % 2 == 0:
            line.color = rectangle2.outline_color
        else:
            line.color = rectangle1.outline_color

        line.attach_to(window)

        x1 = x1 - dx
        x2 = x2 - dx
        y1 = y1 + dy
        y2 = y2 + dy

    window.render()

    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
