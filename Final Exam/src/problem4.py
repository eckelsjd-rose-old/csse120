"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


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
    if n < 2:
        return False  # Integers less than 2 are treated as NOT prime
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above   is_prime   function - it has no TO-DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem4():
    """ Tests the    problem4    function. """

    # Test 1
    print('Test 1')
    print('-------------')
    first_list = [0, 7, 2, 3, 4, 5]
    expected_list = [0, -1, -1, -1, 4, -1]
    expected_index = 1
    actual_index = problem4(first_list)
    actual_new_list = first_list

    print('Expected index:', expected_index)
    print('Actual index:', actual_index)
    print()
    print('Original List:', [0, 7, 2, 3, 4, 5])
    print('Expected new list:', expected_list)
    print('Actual new list:', actual_new_list)
    print()

    # Test 2
    print('Test 2')
    print('-------------')
    first_list = [55, 4, 4, 20]
    expected_list = [55, 4, 4, 20]
    expected_index = -99
    actual_index = problem4(first_list)
    actual_new_list = first_list

    print('Expected index:', expected_index)
    print('Actual index:', actual_index)
    print()
    print('Original List:', [55, 4, 4, 20])
    print('Expected new list:', expected_list)
    print('Actual new list:', actual_new_list)
    print()

    # Test 3
    print('Test 3')
    print('-------------')
    first_list = [55, 55, 7, 31, 4, 2]
    expected_list = [55, 55, -1, -1, 4, -1]
    expected_index = 2
    actual_index = problem4(first_list)
    actual_new_list = first_list

    print('Expected index:', expected_index)
    print('Actual index:', actual_index)
    print()
    print('Original List:', [55, 55, 7, 31, 4, 2])
    print('Expected new list:', expected_list)
    print('Actual new list:', actual_new_list)
    print()


    # -------------------------------------------------------------------------
    # DONE: 2. Implement at least THREE tests here.
    #
    # ** Do NOT use the   simpleTestCase  form in this problem. **
    #
    # Instead, use any form you like that clearly demonstrates
    # whether the test passed or failed.
    #
    # Make sure you test different cases, for example, some that return -1
    # -------------------------------------------------------------------------


def problem4(integers):
    # -------------------------------------------------------------------------
    # NOTE: there is an   is_prime   function near the top of this file.
    # -------------------------------------------------------------------------
    """
    What comes in:
      -- A list of integers.
    Side effects:
      -- MUTATES the given list of integers so that each prime number in the
           list is replaced by -1.
    What goes out:
      -- Returns the index of the first prime number in the original list
           (i.e., the first number that was replaced by -1),
           or -99 if the list contained no prime numbers.
    Example #1:
         integers = [55,  13,  30,  31,   4,   4,  20]
         print(integers)
         value = problem4(integers)
         print(integers)
         print(value)
      should print:
                    [55,  13,  30,  31,   4,   4,  20]
                    [55,  -1,  30,  -1,   4,   4,  20]
                    2
    Example #2:
         integers = [55,  4,   4,  20]
         print(integers)
         value = problem4(integers)
         print(integers)
         print(value)
      should print:
                    [55,  4,   4,  20]
                    [55,  4,   4,  20]
                    -99
    Type hints:
      :type integers: list of int
      :rtype: int
    """

    count = 0
    value = -99

    for k in range(len(integers)):
        number = integers[k]
        if is_prime(number):
            integers[k] = -1
            count += 1
            time.sleep(.1)
        if count == 1:
            value = k

    return value

    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
