"""
PRACTICE Test 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in SEQUENCES-OF-SUBSEQUENCES problems.  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 2 question.
#     5 is a "typical" Test 2 question.
#     7 is a "hard" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
########################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_integers()
    run_test_big_letters()


def run_test_integers():
    """ Tests the    integers    function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  integers  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    #
    #   Try to choose tests that might expose errors in your code!
    #
    #   As usual, include both EXPECTED and ACTUAL results in your tests
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   integers   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]
    answer = integers([(3, 1, 4),
                       (10, 'hi', 10),
                       [1, 2.5, 3, 4],
                       'hello',
                       [],
                       ['oops'],
                       [[55], [44]],
                       [30, -4]
                       ])
    print('Expected is:', expected)
    print('Actual is:  ', answer)

    # Test 2:

    expected = [1, 2, 3, 4, 5]
    answer = integers([['hi', 2.3, 0.2, 1, 'hi'], [2, 3], [], [4, 'bye'],
                       [5]])
    print('Expected is:', expected)
    print('Actual is:  ', answer)


def integers(sequence_of_sequences):
    """
    Returns a new list that contains all the integers
    in the subsequences of the given sequence, in the order that they
    appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    then this function returns:
        [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]

    Type hints:
      :type sequence_of_sequences: (list|tuple) of (list|tuple|string)
      :rtype: list of int
    """

    list1 = []
    for j in range(len(sequence_of_sequences)):
        sublist = sequence_of_sequences[j]
        for k in range(len(sublist)):
            if type(sublist[k]) is int:
                list1 += [sublist[k]]
    return list1

    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    ####################################################################
    # HINT: The
    #           type
    #       function can be used to determine the type of
    #       its argument (and hence to see if it is an integer).
    #       For example, you can write expressions like:
    #         -- if type(34) is int: ...
    #         -- if type(4.6) is float: ...
    #         -- if type('three') is str: ...
    #         -- if type([1, 2, 3]) is list: ...
    #       Note that the returned values do NOT have quotes.
    #       Also, the   is   operator tests for equality (like ==)
    #       but is more appropriate than == in this situation.
    # ------------------------------------------------------------------
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:  10 minutes.
    # ------------------------------------------------------------------


def run_test_big_letters():
    """ Tests the    big_letters    function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  big_letters  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    # ------------------------------------------------------------------
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   big_letters   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 'OTSSSOOPSAPSBOSCOPDOO'
    answer = big_letters([(3, 1, 4),  # not a string
                          'Ok what is ThiSSS?',  # OTSSS
                          (10, 'Ok what is ThiSSS?', 10),  # not a string
                          [],  # not a string
                          ['oops'],  # not a string
                          'oops',  #
                          ['OOPS'],  # not a string
                          '1 OOPS !',  # OOPS
                          'A',  # A
                          'ooPS $$&*#%&&',  # PS
                          'B',  # B
                          'oOpS',  # OS
                          'C',  # C
                          'OoPs'  # OP
                          'D',  # D
                          'OOps'  # OO
                          ])
    print('Expected is:', expected)
    print('Actual is:  ', answer)

    # Test 2:

    print()
    expected = 'ABCD'
    answer = big_letters([[1, 3, 4, 5], 'A', (0, 'hiHI'), 'bcdefBghi', [0,
                                                                       'cd',
                                                                       1],
                         'abCD'])
    print('Expected is:', expected)
    print('Actual is:  ', answer)


def big_letters(sequence_of_sequences):
    """
    Returns a new STRING that contains all the upper-case letters
    in the subsequences of the given sequence that are strings,
    in the order that they appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),                          # not a string
        'Ok what is ThiSSS?',                # OTSSS
        (10, 'Ok what is ThiSSS?', 10),      # not a string
        [],                                  # not a string
        ['oops'],                            # not a string
        'oops',                              #
        ['OOPS'],                            # not a string
        '1 OOPS !',                          # OOPS
        'A',                                 # A
        'ooPS $$&*#%&&',                     # PS
        'B',                                 # B
        'oOpS',                              # OS
        'C',                                 # C
        'OoPs'                               # OP
        'D',                                 # D
        'OOps'                               # OO
         ]
    then this function returns:
        'OTSSSOOPSAPSBOSCOPDOO'

    Precondition:  the given argument is a sequence of sequences.
    """
    new_str = ''
    for j in range(len(sequence_of_sequences)):
        sublist = sequence_of_sequences[j]
        for k in range(len(sublist)):
            if type(sublist) is str:
                if sublist[k].isupper():
                    new_str += str(sublist[k])
    return new_str

    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    ####################################################################
    # IMPORTANT:
    #   There is a STRING METHOD that determines whether or not
    #   a string contains upper-case letters.  To find that method,
    #   somewhere in this file type:
    #           "".
    #   and pause after the dot.
    #   That will display ALL the STRING methods.
    #
    #   Look for a method whose name begins with
    #           is
    #       e.g.   isalnum()  isdigit() ... [but find the one for upper]
    #
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  12 minutes.
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
