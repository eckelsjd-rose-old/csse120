"""
Exam 2, problem 1.

Authors: Dave Fisher, David Mutchler, Matt Boutell, their colleagues,
         and Joshua Eckels.  Jan 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import time
import testing_helper


###############################################################################
# Problem 1 uses the following very simple   Triangle   class.
# READ but do NOT modify this  Triangle   class.
###############################################################################
class Triangle(object):
    """ Represents a triangle. """

    def __init__(self, a, b, c):
        """
        Sets instance variables a, b, and c
        for the lengths of the sides of this triangle.
        """
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        """
        Returns a string representation of this Triangle, as per this example:
              Triangle(   15, 18.26,  3.80)
        Note:
            The representation displays integers without using a decimal point
            and floating point numbers using two decimal points, as in the
            above example.  Each side-length is printed using 5 places,
            to make it easier to compare Triangles listed in a column.
        """
        format_string = 'Triangle({}, {}, {})'
        return format_string.format(prettify(self.a),
                                    prettify(self.b),
                                    prettify(self.c))

    def __eq__(self, other_triangle):
        """
        Two Triangle objects are equal if their instance variables a, b,
        and c are the same, that is, they have the same lengths for
        their sides, stored in the SAME order.

        Note: for REAL triangles, we would say that two Triangles are equal
        if they have the same lengths for their sides, regardless of order.
        Here, we will use the simpler definition (where the order of a,
        b and c DOES matter), just to keep the class as simple as we can.

        For example:
          Triangle(3, 4, 5)  ==   Triangle(3, 4, 5)
        evaluates to True, as you would expect.
          Triangle(3, 4, 5)  ==   Triangle(4, 3, 5)
        evaluates to False, which might be a little surprising.

        Numbers are rounded to 6 decimal places before comparisons,
            to allow for floating-point arithmetic.
        """
        # noinspection PyBroadException
        try:
            return ((round(self.a, 6) == round(other_triangle.a, 6))
                    and (round(self.b, 6) == round(other_triangle.b, 6))
                    and (round(self.c, 6) == round(other_triangle.c, 6)))
        except Exception:
            return False

    def get_area(self):
        """ Returns the area of the given triangle using Heron's Formula. """
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


###############################################################################
# Do NOT modify this  prettify  function.  The Triangle class uses it.
###############################################################################
def prettify(number):
    """
    Returns a "pretty" representation of a number, as per these examples:
       prettify(12)         returns  '   12'
       prettify(12.0035)    returns  '12.00'
       prettify(4.38712)    returns  ' 4.39'
       prettify(4.38499)    returns  ' 4.38'
       prettify(4.2)        returns  ' 4.20'
       prettify(11.999999)  returns  '   12'
       prettify(12.000001)  returns  '   12'
    """
    if abs(round(number) - round(number, 6)) < 10 ** -6:
        # Treat it as an integer:
        return '{:5}'.format(round(number))
    else:
        # Treat it as a float to 2 decimal places:
        return '{:5.2f}'.format(number)


###############################################################################
# The  main  function and the TODOs for you are after this:
###############################################################################
def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    print('  This test case calls: problem1a( Triangle(3, 4, 5) )')
    expected = Triangle(6, 8, 10)
    actual = problem1a(Triangle(3, 4, 5))
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)  # Prints in RED if the test fails.
    # Test 2:
    print()
    print('Test 2:')
    print('  This test case calls: problem1a( Triangle(2, 2, 2) )')
    expected = Triangle(4, 4, 4)
    actual = problem1a(Triangle(2, 2, 2))
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3, part 1:
    print()
    print('Test 3, part 1:')
    print('  This test case calls: problem1a( Triangle(32, 45, 56) )')
    t1 = Triangle(32, 45, 56)
    same_as_t1 = Triangle(32, 45, 56)
    expected = Triangle(64, 90, 112)
    actual = problem1a(t1)
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3, part 2:
    print()
    print('Test 3, part 2 (continuation of the above):')
    print('  Tests that the function does not MUTATE its argument.')
    print("  Expected:", same_as_t1)
    print("  Actual:  ", t1)  # Tests that the argument is NOT mutated.
    print_result_of_test(same_as_t1, t1)

    # Test 4, part 1:
    print()
    print('Test 4, part 1:')
    print('  This test case calls: problem1a( Triangle(50, 1.5, math.pi) )')
    t2 = Triangle(50, 1.5, math.pi)
    same_as_t2 = Triangle(50, 1.5, math.pi)
    expected = Triangle(100, 3.0, 2 * math.pi)
    actual = problem1a(t2)
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 4, part 2:
    print()
    print('Test 4, part 2 (continuation of the above):')
    print('  Tests that the function does not MUTATE its argument.')
    print("  Expected:", same_as_t2)
    print("  Actual:  ", t2)  # Tests that the argument is NOT mutated.
    print_result_of_test(same_as_t2, t2)


def problem1a(triangle):
    """
    What comes in:  a Triangle
    What goes out:  Returns a new Triangle whose side lengths are all
        double the given Triangle's side lengths.
    Side effects: None.
    Example:

      If the given triangle has side lengths 3, 4, 5
      then this function returns a new Triangle whose side lengths are 6, 8, 10

    Type hints:
      :type triangle: Triangle
      :rtype: Triangle
    """

    tri2 = Triangle(triangle.a * 2, triangle.b * 2, triangle.c * 2)
    return tri2

    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the   problem1b   function. """

    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    expected = 6 + 24 + 0 + 6.0  # that is, 36.0
    actual = problem1b([Triangle(3, 4, 5),
                        Triangle(6, 8, 10),
                        Triangle(0, 0, 0),
                        Triangle(4, 5, 3)])
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 2 (same as Test 1, but using a tuple instead of list):
    print()
    print('Test 2:')
    expected = 6 + 24 + 0 + 6.0  # that is, 36.0
    actual = problem1b((Triangle(3, 4, 5),
                        Triangle(6, 8, 10),
                        Triangle(0, 0, 0),
                        Triangle(4, 5, 3)))
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 3:
    print()
    print('Test 3:')
    expected = 0
    actual = problem1b([])
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 4:
    print()
    print('Test 4:')
    expected = 600 + 2400 + 0 + 6.0  # that is, 3006.0
    actual = problem1b([Triangle(30, 40, 50),
                        Triangle(60, 80, 100),
                        Triangle(0, 0, 0),
                        Triangle(4, 5, 3)])
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 5:
    print()
    print('Test 5:')
    t1 = Triangle(32, 45, 56)
    same_as_t1 = Triangle(32, 45, 56)
    expected = 719.6714093945931
    actual = problem1b([t1])
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 6:
    print()
    print('Test 6:')
    print('  Tests that the function does not MUTATE a list ITEM in Test 5.')
    print("  Expected:", same_as_t1)
    print("  Actual:  ", t1)
    print_result_of_test(same_as_t1, t1)

    # Test 7:
    print()
    print('Test 7:')
    t1 = Triangle(32, 45, 56)
    ten_t1s = [t1, t1, t1, t1, t1, t1, t1, t1, t1, t1]
    same_as_ten_t1s = [t1, t1, t1, t1, t1, t1, t1, t1, t1, t1]
    expected = 719.6714093945931 * 10  # that is, 7196.7140939459305
    actual = problem1b(ten_t1s)
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 8:
    print()
    print('Test 8:')
    print('  Tests that the function does not MUTATE its argument in Test 7.')
    print("  Expected:", same_as_ten_t1s)
    print("  Actual:  ", ten_t1s)
    print_result_of_test(same_as_ten_t1s, ten_t1s)

    # Test 9:
    print()
    print('Test 9:')
    print('  Tests that the function does not mutate list ITEMS in Test 7.')
    print("  Expected:", same_as_t1)
    print("  Actual:  ", t1)
    print_result_of_test(same_as_t1, t1)

    # Test 10:
    print()
    print('Test 10:')
    t1 = Triangle(32, 45, 56)
    t2 = Triangle(123, 456, 567)
    t3 = Triangle(0.5, 0.3, 0.4)
    t1_t2_t3 = [t1, t2, t3]
    same_as_t1_t2_t3 = [Triangle(32, 45, 56),
                        Triangle(123, 456, 567),
                        Triangle(0.5, 0.3, 0.4)
                        ]
    expected = 719.6714093945931 + 13454.021703565071 + 0.06  # that is,
    # 14173.753112959665
    actual = problem1b(t1_t2_t3)
    print("  Expected:", expected)
    print("  Actual:  ", actual)
    print_result_of_test(expected, actual)

    # Test 11:
    print()
    print('Test 11:')
    print('  Tests that the function does not MUTATE its argument in Test 10.')
    print("  Expected:", same_as_t1_t2_t3)
    print("  Actual:  ", t1_t2_t3)
    print_result_of_test(same_as_t1_t2_t3, t1_t2_t3)


# -----------------------------------------------------------------------------
# HINT, IMPORTANT: In the following problem, do NOT try to write code to
# compute the area of a Triangle.  Instead, look at the definition
# of the Triangle class (at the top of this file) for a useful method.
# -----------------------------------------------------------------------------
def problem1b(triangles):
    """
    What comes in:  a sequence of Triangle objects (which could be empty)
      (where the   Triangle   class is defined above).
    What goes out:  Returns the sum of the areas of all the triangles.
    Side effects: None.
    Example:
      If   triangles  is a list that contains:
        -- a Triangle with side lengths 3, 4, 5 (area 6)
        -- a Triangle with side lengths 6, 8, 10 (area 24)
        -- a Triangle with side lengths 0, 0, 0 (area 0)
        -- a Triangle with side lengths 4, 5, 3 (area 6)
      then this function returns 36

      If   triangles  is an empty sequence, then this function returns 0.

    Type hints:
      :type triangles: list | tuple of Triangle
      :rtype: int | float
    """
    total = 0
    for k in range(len(triangles)):
        triangle = triangles[k]
        total += triangle.get_area()
    return total

    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # IMPORTANT: See the HINT just before the DEF of this function.
    # -------------------------------------------------------------------------


# noinspection PyNoneFunctionAssignment
def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print('Test 1:')
    print('  This test case calls: problem1c(t1)')
    print('  where t1 is  Triangle(33, 4, 58)')
    t1 = Triangle(33, 4, 58)
    returned_value = problem1c(t1)  # returned_value should be None

    # Check that the Triangle's sides changed correctly:
    expected = Triangle(58, 4, 33)  # what t1 should be AFTER the function call
    print()
    print("  AFTER the function call:")
    print("    The EXPECTED sides for triangle t1 are:", 58, 4, 33)
    print("    The ACTUAL   sides for triangle t1 are:", t1.a, t1.b, t1.c)
    print_result_of_test(expected, t1)

    # Check that the returned value is None:
    print()
    print('Test 1 (continued):')
    print("  Expected returned value:", None)
    print("  Actual returned value:  ", returned_value)
    print_result_of_test(None, returned_value)

    # Test 2:
    print()
    print('Test 2:')
    print('  This test case calls: problem1c(t2)')
    print('  where t2 is  Triangle(33, 4, 58)')
    t2 = Triangle(10, 20, 30)
    returned_value = problem1c(t2)  # returned_value should be None

    # Check that the Triangle's sides changed correctly:
    expected = Triangle(30, 20, 10)  # what t2 should be AFTER function call
    print()
    print("  AFTER the function call:")
    print("    The EXPECTED sides for triangle t2 are:", 30, 20, 10)
    print("    The ACTUAL   sides for triangle t2 are:", t2.a, t2.b, t2.c)
    print_result_of_test(expected, t2)

    # Check that the returned value is None:
    print()
    print('Test 2 (continued):')
    print("  Expected returned value:", None)
    print("  Actual returned value:  ", returned_value)
    print_result_of_test(None, returned_value)

    # Test 3:
    print()
    print('Test 3:')
    print('  This test case calls: problem1c(t3)')
    print('  where t3 is  Triangle(7, 7, 7)')
    t3 = Triangle(7, 7, 7)
    returned_value = problem1c(t3)  # returned_value should be None

    # Check that the Triangle's sides changed correctly:
    expected = Triangle(7, 7, 7)  # what t3 should be AFTER the function call
    print()
    print("  AFTER the function call:")
    print("    The EXPECTED sides for triangle t3 are:", 7, 7, 7)
    print("    The ACTUAL   sides for triangle t3 are:", t3.a, t3.b, t3.c)
    print_result_of_test(expected, t3)

    # Check that the returned value is None:
    print()
    print('Test 3 (continued):')
    print("  Expected returned value:", None)
    print("  Actual returned value:  ", returned_value)
    print_result_of_test(None, returned_value)


def problem1c(triangle):
    """
    What comes in:  a Triangle
    What goes out:  Nothing (i.e. None)
    Side effects:
      -- Swaps the a and c sides of the given triangle
    Example:

      If the given triangle has side lengths 33, 4, 58
      then this function returns nothing,
      but changes (mutates) the given triangle to have side lengths 58, 4, 33.

    Type hints:
      :type triangle: Triangle
    """

    a = triangle.a
    triangle.a = triangle.c
    triangle.c = a

    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_result_of_test(expected, actual):
    testing_helper.print_result_of_test(expected, actual)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
