"""
Final exam, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st
import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()
    run_test_problem1d()


def run_test_problem1a():
    """ Tests the    problem1a    function. """
    # -------------------------------------------------------------------------
    # STUDENTS:
    #   If you do not know how testing using  SimpleTestCase  works,
    #   jusk ASK US TO EXPLAIN IT.
    # -------------------------------------------------------------------------
    tests = [st.SimpleTestCase(problem1a,
                               [-1, 0],  # Arguments
                               1),  # Correct answer
             st.SimpleTestCase(problem1a,
                               [77, 77],  # Arguments
                               108.8944,  # Correct answer
                               0.0001),  # Tolerance - ok if off by this
             st.SimpleTestCase(problem1a,
                               [-3, 4],  # Arguments
                               5),  # Correct answer
             st.SimpleTestCase(problem1a,
                               [5, -10],  # Arguments
                               11.1803,  # Correct answer
                               0.0001),  # Tolerance - ok if off by this
             st.SimpleTestCase(problem1a,
                               [0, 0],  # Arguments
                               0),  # Correct answer
             ]

    st.SimpleTestCase.run_tests('problem1a', tests)


def problem1a(x, y):
    """
    What comes in:
      -- Numbers x and y.
    What goes out:
      -- Returns the distance that the point (x, y)
           is from the origin (0, 0).
    Side effects: None.
    Examples:
      problem1a(-1, 0)  returns 1
      problem1a(77, 77) returns 108.8944 (approximately)
      problem1a(-3, -4) returns 5
    Type hints:
      :type x: int | float
      :type y: int | float
      :rtype: float
    """

    distance = math.sqrt(x ** 2 + y ** 2)
    return distance

    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the    problem1b    function. """
    tests = [st.SimpleTestCase(problem1b,
                               ['dog', 'cat'],
                               'DogCat'),
             st.SimpleTestCase(problem1b,
                               ['hello', 'bob'],
                               'HelloBob'),
             st.SimpleTestCase(problem1b,
                               ['Already', 'Capitalized'],
                               'AlreadyCapitalized'),
             st.SimpleTestCase(problem1b,
                               ['uPPER', 'tURNs LoweR'],
                               'UpperTurns lower'),
             st.SimpleTestCase(problem1b,
                               ['', 'after empty string'],
                               'After empty string'),
             ]

    st.SimpleTestCase.run_tests('problem1b', tests)


def problem1b(s1, s2):
    ###########################################################################
    # HINT: Use the string method  capitalize  to return a capitalized
    #   version of a string.
    ###########################################################################
    """
    What comes in:
      -- Strings s1 and s2.
    What goes out:
      -- Returns s1 followed by s2, but with each "capitalized".
           See examples below.  IMPORTANT: See the   HINT  above.
    Side effects: None.
    Examples:
      problem1('dog', 'cat')               returns 'DogCat'
      problem1('hello', 'bob')             returns 'HelloBob'
      problem1('Already', 'Capitalized')   returns 'AlreadyCapitalized'
      problem1('uPPER', 'tURNs LoweR')     returns 'UpperTurns lower'
      problem1('', 'after empty string')   returns 'After empty string'
    Type hints:
      :type s1: str
      :type s2: str
      :rtype: str
    """

    new_s1 = s1.capitalize()
    new_s2 = s2.capitalize()

    s3 = new_s1 + new_s2

    return s3

    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # IMPORTANT: See the  HINT  just below the DEF line.
    # -------------------------------------------------------------------------


def run_test_problem1c():
    """ Tests the    problem1c    function. """
    tests = [st.SimpleTestCase(problem1c,
                               [["foo", "robots"]],
                               ["foo", "robots", "robots"]),
             st.SimpleTestCase(problem1c,
                               [["a", "robots", "b", "robots", "c"]],
                               ["a", "robots", "robots",
                                "b", "robots", "robots", "c"]),
             st.SimpleTestCase(problem1c,
                               [["foo", "robots", "robots", "ok"]],
                               ["foo", "robots", "robots",
                                "robots", "robots", "ok"]),
             st.SimpleTestCase(problem1c,
                               [["foo", "the end"]],
                               ["foo", "the end"]),
             st.SimpleTestCase(problem1c,
                               [["robots", "foo", "robots", "bar"]],
                               ["robots", "robots", "foo",
                                "robots", "robots", "bar"]),
             st.SimpleTestCase(problem1c,
                               [["robots", "robots", "robots"]],
                               ["robots", "robots", "robots",
                                "robots", "robots", "robots"]),
             st.SimpleTestCase(problem1c,
                               [[]],
                               []),
             ]

    st.SimpleTestCase.run_tests('problem1c', tests)


def problem1c(strings):
    """
    What comes in:
      -- A list of strings.
    What goes out:
      -- Returns a new list where any time the word "robots"
           appears in the original (given) list, it is doubled
           (that is, repeated twice) in the new list.
    Side effects: None.
    Examples:
      problem1c(["foo", "robots"])
         returns
                ["foo", "robots", "robots"]

      problem1c(["a", "robots", "b", "robots", "c"])
         returns
                ["a", "robots", "robots", "b", "robots", "robots", "c"]

      problem1c(["foo", "robots", "robots", "ok"])
         returns
                ["foo", "robots", "robots", "robots", "robots", "ok"]

      problem1c(["foo", "the end"])
         returns
                ["foo", "the end"]
    Type hints:
      :type strings: list of str
      :rtype: list of str
    """
    new_list = []
    for k in range(len(strings)):
        if strings[k] == 'robots':
            new_list += ['robots'] + ['robots']
        else:
            new_list += [strings[k]]

    return new_list


    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem1d():
    """ Tests the    problem1d    function. """
    tests = [st.SimpleTestCase(problem1d,
                               [[1, 5, 10, 11, 13, 18, 19, 100, 105]],
                               100),
             st.SimpleTestCase(problem1d,
                               [[40, 42, 50, 55, 57, 60]],
                               57),
             st.SimpleTestCase(problem1d,
                               [(10,)],
                               -1),
             st.SimpleTestCase(problem1d,
                               [[]],
                               -1),
             st.SimpleTestCase(problem1d,
                               [[1, 1, 1, 1, 1, 1, 1]],
                               1),
             st.SimpleTestCase(problem1d,
                               [[-10, -5, -4, -3, -2, -1]],
                               -2),
             st.SimpleTestCase(problem1d,
                               [[-1, 0, 1]],
                               0),
             st.SimpleTestCase(problem1d,
                               [[-1, 0]],
                               -1),
             ]

    st.SimpleTestCase.run_tests('problem1d', tests)


def problem1d(sequence):
    """
    What comes in:
      -- A sequence of integers in SORTED ORDER, e.g.
           [1, 5, 10, 11, 13, 18, 19, 100, 105]
    What goes out:
      -- Returns the second-largest number in the list,
           or -1 if the list contains fewer than two numbers.
    Examples:
      problem1d([1, 5, 10, 11, 13, 18, 19, 100, 105]) returns 100
      problem1d([40, 42, 50, 55, 57, 60]              returns 57
      problem1d([-1, 0, 1])     returns 0
      problem1d([-5, 0])        returns -5
      problem1d([])             returns -1
      problem1d([42])           returns -1
    Type hints:
      :type sequence: list of int
      :rtype: int
    """
    if len(sequence) >= 2:
        index = len(sequence) - 2
        return sequence[index]
    else:
        return -1

    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
