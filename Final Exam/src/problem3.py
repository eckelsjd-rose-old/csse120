"""
Final exam, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: m=5 and n=2')
    shape(5, 2)

    print()
    print('Test 2 of shape: m=3 and n=6')
    shape(3, 6)

    print()
    print('Test 3 of shape: m=7 and n=1')
    shape(7, 1)

    print()
    print('Test 4 of shape: m=6 and n=4')
    shape(6, 4)


def shape(m, n):
    ###########################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ###########################################################################
    """
    What comes in: Positive integers m and n.
    What goes out:  Nothing.
    Side effects:
      Prints  n  "v" shaped patterns of numbers,
      where the height of each "v" is m.
    Examples:
      It looks like this example for m=5 and n=2:

    5       5 5       5
     4     4   4     4
      3   3     3   3
       2 2       2 2
        1         1

      and like this for m=3 and n=6:

    3   3 3   3 3   3 3   3 3   3 3   3
     2 2   2 2   2 2   2 2   2 2   2 2
      1     1     1     1     1     1

    :type m: int
    :type n: int
    """

    count = 0

    for j in range(m, 0, -1):
        while count < n:
            for k in range(m - j):
                print(' ', end='')
            for i in range(1):
                print(j, end='')
            for l in range(0, 2*j - 3):
                print(' ', end='')
            for p in range(1):
                if j > 1:
                    print(j, end='')
            for w in range(m - j):
                print(' ', end='')
            print(' ', end='')
            count += 1
        print()
        count = 0

    # -------------------------------------------------------------------------
    # DONE: Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPORTANT:  See the RESTRICTION just below the DEF line.
    #
    # NOTE:
    #   If you are having trouble solving this problem,
    #   write code that prints a SINGLE  v-shaped  object for partial credit.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
