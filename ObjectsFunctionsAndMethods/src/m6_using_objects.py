"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """

    two_circles()
    circle_and_rectangle()
    lines()


    # Test your functions by putting calls to them here:


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """

    window = rg.RoseWindow()
    point1 = rg.Point(100, 100)
    point2 = rg.Point(200, 200)
    radius1 = 50
    radius2 = 25
    circle1 = rg.Circle(point1, radius1)
    circle1.fill_color = 'green'
    circle2 = rg.Circle(point2, radius2)

    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window1 = rg.RoseWindow()

    point3 = rg.Point(100, 100)
    radius3 = 50
    circle3 = rg.Circle(point3, radius3)
    circle3.fill_color = 'blue'
    circle3.attach_to(window1)

    point4 = rg.Point(200, 200)
    point5 = rg.Point(250, 250)
    rectangle = rg.Rectangle(point4, point5)
    rectangle.attach_to(window1)

    window1.render()

    print(circle3.outline_thickness)
    print(circle3.fill_color)
    print(circle3.center)
    print(point3.x)
    print(point3.y)

    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    rect_center = rectangle.get_center()
    print(rect_center)
    print(rect_center.x)
    print(rect_center.y)

    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """

    window = rg.RoseWindow()

    point1 = rg.Point(50, 50)
    point2 = rg.Point(100, 100)
    line1 = rg.Line(point1, point2)
    line1.attach_to(window)

    point3 = rg.Point(250, 250)
    point4 = rg.Point(100, 250)
    line2 = rg.Line(point3, point4)
    line2.thickness = 10
    line2.attach_to(window)

    window.render()

    midpoint = line2.get_midpoint()
    print(midpoint)
    print(midpoint.x)
    print(midpoint.y)

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
