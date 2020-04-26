"""
Demonstrates using (calling) FUNCTIONS and using (calling) METHODS:
  -- what is similar
  -- how they differ.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
#
# DONE: 2.
#   READ this comment, ASKING QUESTIONS as needed to understand it.
#
#   For objects that are CONSTRUCTED, we use the DOT notation
#   to ask them to do things or to change their characteristics.
#   For example:
#      nadia = rg.SimpleTurtle()
#      nadia.pen = rg.Pen('blue', 1)
#      nadia.forward(100)
#
#   In the above example:
#
#      pen      is an   INSTANCE VARIABLE   (aka DATA ATTRIBUTE, FIELD)
#                 of SimpleTurtles.  It is a CHARACTERISTIC of
#                 SimpleTurtles. Each SimpleTurtle has its own VALUE
#                 of that characteristic.
#
#      forward  is a   METHOD   (aka FUNCTION ATTRIBUTE)
#                 of SimpleTurtles.  It is something that any
#                 SimpleTurtle can DO.  It is just like a FUNCTION
#                 except for details about the way that it is called.
#
#   The statement
#        nadia.forward(100)
#   CALLS the   forward   METHOD on nadia, sending that method the number 100 and making the method run (execute).
#
#   We   ** define **   FUNCTIONS to give NAMES to blocks of code (note FUNCTIONS and METHODS are different).
#   For example:
#
#      def turtle3():
#          maja = rg.SimpleTurtle()
#          maja.pen = rg.Pen('green', 10)
#          maja.paint_bucket = rg.PaintBucket('black')
#            ...
#
#   We   ** call **   FUNCTIONS (that is, we make them run) in a way that is similar to how we call METHODS,
#   but WITHOUT the DOT notation.  For example
#      def main():
#          turtle3()
#
#   Run this module and review the existing code.  Can you identify the functions calls and methods calls?
#
#   When you believe you understand the differences and similarities
#   between calling a FUNCTION and calling a METHOD, change the above TO DO to DONE.
#
########################################################################

# ----------------------------------------------------------------------
# There are MORE TODOs further down in this module!
# ----------------------------------------------------------------------

import rosegraphics as rg


def main():
    """
    Makes a TurtleWindow,
    calls the other functions in this module to test/demo them,
    and waits for the user to click anywhere in the window to close it.
    """
    window = rg.TurtleWindow()

    # Make the animation go much faster.
    #   First number:  bigger means faster.
    #   Second number: bigger means slower.
    window.tracer(1, 1)

    jump_and_move_turtle(100, 50, 200, -100)
    turtle = rg.SimpleTurtle('square')
    draw_many_squares(turtle, 3, 75, 15)
    turtle3()

    # When the TODOs ask you to test YOUR code, put YOUR tests here:
    try_methods()
    try_functions()
    try_methods_and_functions()

    window.close_on_mouse_click()


def jump_and_move_turtle(x1, y1, x2, y2):
    """
    Constructs a thick, slow, magenta SimpleTurtle.
    Jumps that SimpleTurtle (without drawing) to (x1,  y1),
    then moves that Turtle (while drawing) to (x2, y2).
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    # ------------------------------------------------------------------
    jumper = rg.SimpleTurtle()
    jumper.pen = rg.Pen('magenta', 20)
    jumper.speed = 1

    jumper.pen_up()
    jumper.go_to(rg.Point(x1, y1))

    jumper.pen_down()
    jumper.go_to(rg.Point(x2, y2))


def draw_many_squares(my_turtle, number_of_squares, size, twist):
    """
    Makes the given   SimpleTurtle   object draw:
      -- many squares (how many? answer: NUMBER_OF_SQUARES)
    where each square:
      -- has the same size (what size? answer: SIZE)
    and each square is:
      -- "twisted" a bit from the previous one (how much? TWIST degrees)

    NOTE: The 3 lines below that begin with   :type   are called
    "type hints".  They make the "dot" trick work more effectively.
    We will include them in function specifications routinely.
      :type  my_turtle:          rg.SimpleTurtle
      :type  number_of_squares:  int
      :type  size:               int
      :type  twist:              int
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    # ------------------------------------------------------------------
    for _ in range(number_of_squares):
        my_turtle.draw_square(size)
        my_turtle.left(twist)


def turtle3():
    """
    Constructs a classic SimpleTurtle and asks it to draw a
      "ball on pole" shape.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    # ------------------------------------------------------------------
    maja = rg.SimpleTurtle()
    maja.pen = rg.Pen('green', 10)
    maja.paint_bucket = rg.PaintBucket('black')

    maja.right(135)
    maja.forward(300)

    maja.begin_fill()
    maja.draw_circle(50)
    maja.end_fill()


def try_methods():
    """
    Constructs a SimpleTurtle and sets its   pen   to a new rg.Pen
    that is 'brown' with thickness 5.
    Then makes the SimpleTurtle move as follows (in the order listed):
      -- forward   150 units
      -- left       90 degrees
      -- forward    50 units
      -- backward  100 units
    """

    michael = rg.SimpleTurtle()
    michael.pen = rg.Pen('brown', 5)
    michael.forward(150)
    michael.left(90)
    michael.forward(50)
    michael.backward(100)

    ####################################################################
    # DONE: 3. Implement this function, per its doc-string above.
    #    Put a statement in   main   to test this function
    #    (by calling this function).
    ####################################################################


def try_functions():
    """
    Causes several SimpleTurtles to do the following:
     -- One jumps to (200, 100), then moves (while drawing) to (300, 30)
     -- One jumps to (100, 200), then moves (while drawing) to (0, 0)
     -- One jumps to (-50, 50), then moves (while drawing) to (100, 100)
    """

    jump_and_move_turtle(200,100,300,30)
    jump_and_move_turtle(100,200,0,0)
    jump_and_move_turtle(-50,50,100,100)

    ####################################################################
    # DONE: 4. Implement this function, per its doc-string above.
    #    Put a statement in   main   to test this function
    #    (by calling this function).  IMPORTANT, IMPORTANT, IMPORTANT:
    #    Keep reading the rest of this TO DO before doing the above!
    #
    # IMPORTANT: This function requires
    #   ** exactly 3 lines **
    # If you think it needs more, ** ASK FOR HELP. **
    # HINT: see   jump_and_move_turtle   above.
    #
    ####################################################################


def try_methods_and_functions():
    """
    Constructs a SimpleTurtle and sets its   pen  to a new rg.Pen
    that is 'blue' with thickness 5.

    Then makes the SimpleTurtle do the following (in the order listed):

      1. Go  backward  150 units.

      2. Change its speed to 1 (slowest).
         Draw 2 squares whose size (width and height) are 100,
         each "twisted" from the previous by 30 degrees.

      3. Change its speed to 5 (faster).
         Change its Pen's color to 'red'.
         Draw 10 squares whose size (width and height) are 50,
         each "twisted" from the previous by 15 degrees.

      4. Change its speed to 100 (about the fastest possible).
         Change its Pen's thickness to 35.
         Draw 8 squares whose size (width and height) are 300,
         each "twisted" from the previous by 60 degrees.

      5. Changes its Pen to be a NEW Pen whose color is 'black'
         and whose thickness is 3.

      6. Goes backward  200 units.

      7. Draw a CIRCLE whose radius is 30.

      8. Draw a SQUARE whose sides are each of length 50.
    """

    josh = rg.SimpleTurtle()
    josh.pen = rg.Pen('blue', 5)
    josh.backward(150)

    josh.speed = 1
    draw_many_squares(josh, 2, 100, 30)

    josh.speed = 5
    josh.pen = rg.Pen('red', 5)
    draw_many_squares(josh, 10, 50, 15)

    josh.speed = 100
    josh.pen = rg.Pen('red', 35)
    draw_many_squares(josh, 8, 300, 60)

    josh.pen = rg.Pen('black', 3)
    josh.backward(200)
    josh.draw_circle(30)
    josh.draw_square(50)

    ####################################################################
    # DONE: 5. Implement this function, per its doc-string above.
    #    Put a statement in   main   to test this function
    #    (by calling this function).  IMPORTANT, IMPORTANT, IMPORTANT:
    #    Keep reading the rest of this TO DO before doing the above!
    #
    # IMPORTANT: This function should ** CALL ** the
    #   draw_many_squares
    # function defined above.  If you don't see why, ** ASK FOR HELP. **
    #
    ####################################################################


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
