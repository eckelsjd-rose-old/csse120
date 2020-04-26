"""
Final exam, problem 2.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st
import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2a()
    run_test_problem2b()
    run_test_problem2c()
    run_test_problem2d()


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:  True if the given integer is prime, else False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above   is_prime   function - it has no TO-DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def run_test_problem2a():
    """ Tests the    problem2a    function. """
    tests = [
        st.SimpleTestCase(problem2a,
                          [[rg.Point(3, 4),
                            rg.Point(3, 4),
                            rg.Point(3, 4)]],
                          12),
        st.SimpleTestCase(problem2a,
                          [[rg.Point(3, 4),
                            rg.Point(3, -4)]],
                          0),
        st.SimpleTestCase(problem2a,
                          [[rg.Point(3, 4)]],
                          4),
        st.SimpleTestCase(problem2a,
                          [[]],
                          0),
        st.SimpleTestCase(problem2a,
                          [[rg.Point(100, 40),
                            rg.Point(50,  10),
                            rg.Point(200, 50),
                            rg.Point(120, 30),
                            rg.Point(40,  88),
                            rg.Point(90,  60)]],
                          278),
        st.SimpleTestCase(problem2a,
                          [[rg.Point(200,  40),
                            rg.Point(50,  10),
                            rg.Point(10, 50),
                            rg.Point(120, 30),
                            rg.Point(40,  88),
                            rg.Point(90,  60)]],
                          278),
        st.SimpleTestCase(problem2a,
                          [[rg.Point(1,  40),
                            rg.Point(2,  10),
                            rg.Point(3,  50),
                            rg.Point(4,  30),
                            rg.Point(5,  88),
                            rg.Point(6,  66),
                            rg.Point(7,  55),
                            rg.Point(8,  44),
                            rg.Point(9,  99),
                            rg.Point(10,  6)]],
                          488),
         ]

    st.SimpleTestCase.run_tests('problem2a', tests)


def problem2a(points):
    """
    What comes in:
      -- A list of rg.Point objects.
    What goes out:
      -- Returns the sum of all the y-coordinates
           of the rg.Point objects in the list.
    Side effects: None.
    Examples:
      problem2a([rg.Point(3, 4), rg.Point(3, 4), rg.Point(3, 4)]) returns 12
      problem2a([rg.Point(3, 4), rg.Point(3, -4)])                returns 0
      problem2a([rg.Point(3, 4)])                                 returns 4
      problem2a([])                                               returns 0
    Type hints:
      :type points: list of rg.Point
      :rtype: int
    """
    total = 0
    for k in range(len(points)):
        point = points[k]
        total += point.y

    return total

    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


def run_test_problem2b():
    """ Tests the    problem2b    function. """
    tests = [st.SimpleTestCase(problem2b,
                               [[1, 20, 30], [1, 2, 3]],
                               1),
             st.SimpleTestCase(problem2b,
                               [[0, -50, 30], [1, 2, 3]],
                               2),
             st.SimpleTestCase(problem2b,
                               [[10, 11, 12], [1, 2, 3]],
                               0),
             st.SimpleTestCase(problem2b,
                               [[111], [222]],
                               -1),
             st.SimpleTestCase(problem2b,
                               [[], []],
                               -1),
             st.SimpleTestCase(problem2b,
                               [[3, 3, -3, -3], [3, 3, -3, -30]],
                               3),
             ]

    st.SimpleTestCase.run_tests('test_problem2b', tests)


def problem2b(numbers1, numbers2):
    """
    What comes in:
      -- Two lists of numbers.
         Assume that the lists have the same length.
    What goes out:
      -- Returns the smallest index at which the number in the first list
           is bigger than the corresponding number in the second list,
           or -1 if no number in the first list is bigger than its
           corresponding number in the second list.
    Side effects: None.
    Examples:
      problem2b([1, 20, 30], [1, 2, 3])     returns 1
      problem2b([0, -50, 30], [1, 2, 3])    returns 2
      problem2b([10, 11, 12], [1, 2, 3])    returns 0
      problem2b([111], [222])               returns -1
      problem2b([], [])                     returns -1
    Type hints:
      :type numbers1: list of (int | float)
      :type numbers2: list of (int | float)
      :rtype: int
    """
    smallest_index = -1

    for k in range(len(numbers1)):
        number1 = numbers1[k]
        number2 = numbers2[k]
        if number1 > number2:
            smallest_index = k
            return smallest_index

    return smallest_index

    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


def run_test_problem2c():
    """ Tests the    problem2c    function. """
    tests = [
        st.SimpleTestCase(problem2c, [3], 11),
        st.SimpleTestCase(problem2c, [-3], 11),
        st.SimpleTestCase(problem2c, [200], 40009),
        st.SimpleTestCase(problem2c, [123], 15131),
        st.SimpleTestCase(problem2c, [4], 17),
        st.SimpleTestCase(problem2c, [5], 29),
        st.SimpleTestCase(problem2c, [6], 37),
        st.SimpleTestCase(problem2c, [7], 53),
    ]

    st.SimpleTestCase.run_tests('problem2c', tests)


def problem2c(m):
    # ------------------------------------------------------------------
    # NOTE: there is an   is_prime   function near the top of this file.
    # ------------------------------------------------------------------
    """
    What comes in:
      -- A positive integer m.
    What goes out:
      -- Returns the smallest prime number that is bigger than m squared.
    Side effects: None.
    Examples:
      problem2c(3) returns 11
      problem2c(4) returns 17
      problem2c(5) returns 29
      problem2c(6) returns 37
      problem2c(7) returns 53
    Type hints:
      :type m: int
      :rtype: int
    """
    number = 0

    while True:
        number += 1
        if is_prime(number) and number > m ** 2:
            break

    return number

    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


def run_test_problem2d():
    """ Tests the    problem2d    function. """
    tests = [st.SimpleTestCase(problem2d,
                               [[2, 3, 4, 5, 6, 7]],
                               7),
             st.SimpleTestCase(problem2d,
                               [[6, 7, 8, 9]],
                               7),
             st.SimpleTestCase(problem2d,
                               [[53, 54, 55, 56]],
                               53),
             st.SimpleTestCase(problem2d,
                               [[200, 5, 5000]],
                               5),
             st.SimpleTestCase(problem2d,
                               [[4, 6, 8, 9, 10]],
                               -1),
             st.SimpleTestCase(problem2d,
                               [[]],
                               -1),
             st.SimpleTestCase(problem2d,
                               [[137]],
                               137),
             st.SimpleTestCase(problem2d,
                               [[150, 5, 151, 200]],
                               151),
             ]

    st.SimpleTestCase.run_tests('test_problem2d', tests)


def problem2d(seq):
    # ------------------------------------------------------------------
    # NOTE: there is an   is_prime   function near the top of this file.
    # ------------------------------------------------------------------
    """
    What comes in:
      -- A sequence of positive integers m.
    What goes out:
      -- Returns the biggest prime number in the list,
           or -1 if there are no prime numbers in the list.
    Side effects: None.
    Examples:
      problem2d([2, 3, 4, 5, 6, 7])        returns 7
      problem2d([6, 7, 8, 9])              returns 7
      problem2d([53, 54, 55, 56])          returns 53
      problem2d([200, 5, 5000])            returns 5
      problem2d([4, 6, 8, 9, 10])          returns -1
      problem2d([])                        returns -1
    Type hints:
      :type seq: list of int
      :rtype: int
    """

    biggest_index = -1

    for k in range(len(seq)):
        if is_prime(seq[k]):
            biggest_index = k
            break

    if biggest_index != -1:
        for k in range(len(seq)):
            if is_prime(seq[k]) and seq[k] > seq[biggest_index]:
                biggest_index = k

        return seq[biggest_index]

    return biggest_index


    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
