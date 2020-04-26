"""
Exam 1, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Joshua Eckels.  December 2017.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()


###############################################################################
# DONE: 2.  READ the doc-string for the   is_prime   function below.
# Ask your instructor for help if you do not understand it.
#
# Once you are confident that you understand the doc-string
# (ignore the code itself!), change the TO-DO for this problem to DONE.
###############################################################################
def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
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
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above   is_prime   function
    #      - it has no TO-DO.
    #
    #   Do NOT copy code from the above   is_prime   function.
    #   Instead, ** CALL ** that function as needed in the problems below.
    # -------------------------------------------------------------------------


###############################################################################
# DONE: 3.  READ the doc-string for the   product_of_digits   function
# below.  Ask your instructor for help if you do not understand it.
#
# Once you are confident that you understand the doc-string
# (ignore the code itself!), change the TO-DO for this problem to DONE.
###############################################################################
def product_of_digits(number, digit_to_skip):
    """
    What comes in:
      -- number (a positive integer)
      -- digit_to_skip (a digit, that is, either 0, 1, 2, 3, ... or 9)
    What goes out:  The product of the digits in the given number,
      but with any instances of the "digit_to_skip" ignored.
    Side effects:   None.
    Examples:
      -- product_of_integers(83135, 3)
           returns (8 * 1 * 5), which is 40        (the 3s were ignored).

      -- product_of_integers(83135, 8)
           returns (1 * 3 * 3 * 5), which is 45    (the 8 was ignored).

      -- product_of_integers(2255, 5)
           returns (2 * 2), which is 4             (the 5s were ignored).

      -- product_of_integers(234, 7)
           returns (2 * 3 * 4), which is 24        (there are no 7s to ignore).

      -- product_of_integers(204, 7)
           returns (2 * 0 * 4), which is 0

      -- product_of_integers(2040, 0)
           returns (2 * 4), which is 8             (the 0s are ignored).
    """
    digit_product = 1
    remaining_number = number
    while True:
        if remaining_number == 0:
            break
        if remaining_number % 10 != digit_to_skip:
            digit_product = digit_product * (remaining_number % 10)
        remaining_number = remaining_number // 10

    return digit_product
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above   product_of_digits   function
    #      - it has no TO-DO.
    #
    #   Do NOT copy code from the above   product_of_digits   function.
    #   Instead, ** CALL ** that function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the   problem1a   function defined below.
    #   Include at least **   1 ADDITIONAL   ** test.
    #
    # Use the same 4-step process as for previous TEST functions.
    # In particular, include both EXPECTED and ACTUAL results.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 3271
    answer = problem1a(10, 2, 5)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 4 + 9 + 25 + 49  # which is 87
    answer = problem1a(2, 3, 2)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # -------------------------------------------------------------------------
    # TO-DO 4 continued: Put your ADDITIONAL test here:
    # -------------------------------------------------------------------------

    # Test 3:
    expected = 1 + 4 + 9 + 25 + 49  # which is 88
    answer = problem1a(1, 2, 3)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

###############################################################################
# IMPORTANT: in the following problem,
#    **  For full credit you must appropriately use (call)
#    **  the appropriate functions that are defined above,
#    **  possibly including ones you have written.
###############################################################################


def problem1a(a, b, p):
    """
    What comes in:  Positive integers a, b and p,
      with (b raised to the pth power) >= a.
    What goes out:  Returns the sum of the squares of the primes
      that are between a and (b raised to the pth power),
      but NOT including (b raised to the pth power) itself.
    Side effects:   None.
    Examples:
      -- problem1a(10, 2, 5)  returns 3271  because:
           It examines the integers from 10 to (2 to the 5th power),
           but NOT including (2 to the 5th power),
           that is,  10  11  12  13  ...  31, and returns:
             (11 squared) + (13 squared) + (17 squared) + (19 squared)
                + (23 squared) + (29 squared) + (31 squared),
             which is (121 + 169 + 289 + 361 + 529 + 841 + 961),
             which is 3271.
    """

    total = 0
    for k in range((b ** p) - a):
        value = k + a
        #print(k, b ** p, value)
        if is_prime(value) == True:
            total = total + value ** 2

    return total

    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above)
    #          (but you add one ADDITIONAL test, per TO-DO 4).
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # IMPORTANT NOTE
    #          If you happen to know how to use the range statement with 2 or 3
    #          arguments don't do that.  You are only allowed to use the 1
    #          argument version of the range statement to solve this problem.
    # -------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    # You may add more tests if you wish, but you are not required to do so.
    ###########################################################################

    # Test 1:
    expected = 364
    answer = problem1b(4, 2)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 464557714
    answer = problem1b(13, 3)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)


###############################################################################
# IMPORTANT: in the following problem,
#    **  For full credit you must appropriately use (call)
#    **  the appropriate functions that are defined above,
#    **  possibly including ones you have written.
###############################################################################
def problem1b(m, n):
    """
    What comes in:  Positive integers m and n.
    What goes out:  Returns the sum of the squares of the primes
      that are between m and (m raised to the nth power),
      but NOT including (m raised to the nth power) itself.
    Side effects:   None.
    Examples:
      -- problem1b(4, 2)  returns 364  because:
           It examines the integers  4  5  6  ...  15   and returns:
             (5 squared) + (7 squared) + (11 squared) + (13 squared)
             which is (25 + 49 + 121 + 169),
             which is 364.
    """

    total = 0
    for k in range((m ** n) - m):
        value = k + m
        if is_prime(value) == True:
            total = total + value ** 2
    return total

    # -------------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c   function:')
    print('--------------------------------------------------')

    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    # You may add more tests if you wish, but you are not required to do so.
    ###########################################################################

    # Test 1:
    expected = 5
    answer = problem1c(355, 362, 6)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 185
    answer = problem1c(3091, 4091, 0)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)


###############################################################################
# IMPORTANT: in the following problem,
#    **  For full credit you must appropriately use (call)
#    **  the appropriate functions that are defined above,
#    **  possibly including ones you have written.
###############################################################################
def problem1c(a, b, digit_to_skip):
    """
    What comes in:  Positive integers a, b and digit_to_skip,
      with b >= a.
    What goes out:  Returns the number of integers between a and b, inclusive,
      that satisfy the following property:
        The product of the digits in the integer, but excluding the given
        digit_to_skip, is odd.
    Side effects:   None.
    Examples:
      -- problem1a(355, 362, 6)  returns 5
           because the products of the digits:
             -- in 355, which has no 6s, is 3 * 5 * 5, which is  75 -- ODD
             -- in 356, excluding the 6, is 3 * 5,     which is  15 -- ODD
             -- in 357, which has no 6s, is 3 * 5 * 7, which is 105 -- ODD
             -- in 358, which has no 6s, is 3 * 5 * 8, which is 120 -- not odd
             -- in 359, which has no 6s, is 3 * 5 * 9, which is 135 -- ODD
             -- in 360, excluding the 6, is 3 * 0,     which is   0 -- not odd
             -- in 361, excluding the 6, is 3 * 1,     which is   3 -- ODD
             -- in 362, excluding the 6, is 3 * 2,     which is   6 -- not odd
           and 5 of the above are ODD.
    """

    count = 0
    for k in range(b - a):
        value = a + k
        if product_of_digits(value, digit_to_skip) % 2 == 1:
            count = count + 1
    return count

    # ------------------------------------------------------------------
    # DONE: 7. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
