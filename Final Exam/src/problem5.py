"""
Final exam, problem 5.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Joshua Eckels.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem5a()
    run_test_problem5b()
    run_test_problem5c()


def is_prime(n):
    """
    What comes in:  An integer.
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


def run_test_problem5a():
    """ Tests the    problem5a    function. """
    tests = [
        st.SimpleTestCase(problem5a,
                          [[(4, 25),
                            (33, 54, 20, 55, 10),
                            (6, 11, 70, 33),
                            (7, 11),
                            (5, 5, 3)
                            ]],
                          (6, 11, 70, 33)),
        st.SimpleTestCase(problem5a,
                          [[[4, 6, 8],
                            [7, 10, 2]]],
                          [7, 10, 2]),
        st.SimpleTestCase(problem5a,
                          [[[4, 6, 8],
                            [4, 6, 8]]],
                          -1),
        st.SimpleTestCase(problem5a,
                          [[[11],
                            [4, 6, 8],
                            [7, 10, 2]]],
                          [11]),
        st.SimpleTestCase(problem5a,
                          [[[],
                            []]],
                          -1),
        st.SimpleTestCase(problem5a,
                          [[[],
                            [4, 6, 8],
                            [10, 2, 4, 5],
                            [11, 17, 53]]],
                          [10, 2, 4, 5]),
        st.SimpleTestCase(problem5a,
                          [[(6, 11, 70, 33),
                            (4, 25),
                            (33, 54, 20, 55, 10),
                            (7, 11),
                            (5, 5, 3)
                            ]],
                          (6, 11, 70, 33)),
        st.SimpleTestCase(problem5a,
                          [[(4, 25),
                            (6, 11, 70, 33),
                            (33, 54, 20, 55, 10),
                            (7, 11),
                            (5, 5, 3)
                            ]],
                          (6, 11, 70, 33)),
        st.SimpleTestCase(problem5a,
                          [[(4, 25),
                            (33, 54, 20, 55, 10),
                            (7, 11),
                            (6, 11, 70, 33),
                            (5, 5, 3)
                            ]],
                          (7, 11)),
        st.SimpleTestCase(problem5a,
                          [[(4, 25),
                            (33, 54, 20, 55, 10),
                            (7, 11),
                            (5, 5, 3),
                            (6, 11, 70, 33),
                            ]],
                          (7, 11)),
        st.SimpleTestCase(problem5a,
                          [[(4, 25),
                            (33, 54, 20, 55, 10),
                            (7,),
                            (5, 5, 3),
                            (6, 11, 70, 33),
                            ]],
                          (7,)),
        st.SimpleTestCase(problem5a,
                          [[(4, 25),
                            (33, 54, 20, 55, 10),
                            (12, 7),
                            (5, 5, 3),
                            (6, 11, 70, 33),
                            ]],
                          (12, 7)),
    ]

    st.SimpleTestCase.run_tests('problem5a', tests)


def problem5a(seq_of_seq):
    """
    What comes in:
      -- A sequence of subsequences of integers.
    What goes out:
      -- Returns the first subsequence that contains a number that is prime,
           or -1 if no subsequence contains a number that is prime.
    Side effects: None.
    Examples:
      problem5a([(4, 25),
                 (33, 54, 20, 55, 10),
                 (6, 11, 70, 33),
                 (7, 11),
                 (5, 5, 3)
                ]
                returns (6, 11, 70, 33)
      problem5a([[4, 6, 8], [7, 10, 2]])      returns [7, 10, 2]
      problem5a([[4, 6, 8], [4, 6, 8]])       returns -1
      problem5a([[4, 6, 8], [[10, 2, 4, 5]])  returns [10, 2, 4, 5]
      problem5a([[], []])                     returns -1
    Type hints:
      :type seq_of_seq: list of list of int
      :rtype: (list of int) | int
    """

    for j in range(len(seq_of_seq)):
        subseq = seq_of_seq[j]
        for k in range(len(subseq)):
            if is_prime(subseq[k]):
                return subseq

    return -1

    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem5b():
    """ Tests the    problem5b    function. """
    tests = [st.SimpleTestCase(problem5b,
                               [18],
                               [1, 2, 3, 6, 9, 18]),
             st.SimpleTestCase(problem5b,
                               [13],
                               [1, 13]),
             st.SimpleTestCase(problem5b,
                               [40],
                               [1, 2, 4, 5, 8, 10, 20, 40]),
             st.SimpleTestCase(problem5b,
                               [1],
                               [1]),
             st.SimpleTestCase(problem5b,
                               [8],
                               [1, 2, 4, 8]),
             st.SimpleTestCase(problem5b,
                               [42],
                               [1, 2, 3, 6, 7, 14, 21, 42]),
             st.SimpleTestCase(problem5b,
                               [123],
                               [1, 3, 41, 123]),
             st.SimpleTestCase(problem5b,
                               [123],
                               [1, 3, 41, 123]),
             st.SimpleTestCase(problem5b,
                               [12345],
                               [1, 3, 5, 15, 823, 2469, 4115, 12345]),
             ]

    st.SimpleTestCase.run_tests('problem5b', tests)


def problem5b(n):
    """
    What comes in:
      -- A positive integer n.
    What goes out:
      -- Returns a list of the factors of n, that is,
           a list of the positive integers that divide evenly into n.
    Side effects: None.
    Examples:
      problem5b(18)   returns [1, 2, 3, 6, 9, 18]
      problem5b(13)   returns [1, 13]
      problem5b(40)   returns [1, 2, 4, 5, 8, 10, 20, 40]
      problem5b(1)    returns [1]
      problem5b(8)    returns [1, 2, 4, 8]
    """

    list1 = []

    for k in range(1, n + 1):
        number = n // k
        if n - (number * k) == 0:
            list1 += [k]

    return list1

    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem5c():
    """ Tests the    problem5c    function. """
    tests = [
        st.SimpleTestCase(problem5c, ["aaab"], "aaa"),
        st.SimpleTestCase(problem5c, ["abcbcdc"], "ccc"),
        st.SimpleTestCase(problem5c, ["bbaaa"], "aaa"),
        st.SimpleTestCase(problem5c, ["aaabb"], "aaa"),
        st.SimpleTestCase(problem5c, ["a"], "a"),
        st.SimpleTestCase(problem5c, ["Hello"], "ll"),
        st.SimpleTestCase(problem5c, ["abb"], "bb"),
        st.SimpleTestCase(problem5c, ["aaabcbcdca"], "aaaa"),
        st.SimpleTestCase(problem5c, ["CSSE120"], "SS"),
    ]

    st.SimpleTestCase.run_tests('problem5c', tests)


def problem5c(s):
    # -------------------------------------------------------------------------
    # HINT: Use a NESTED LOOP (i.e., a loop within a loop)
    #   to solve this problem.
    # -------------------------------------------------------------------------
    """
    What comes in:
      -- A non-empty string s.
    What goes out:
      -- Returns a string that contains only the most common character
           in the given string, repeated as many times as it appears
           in the given string.  (See examples below.)
    Note: You can assume that one character will be more common than all the
          others (i.e. there won't be a tie for the most common character).
    Side effects: None.
    Examples:
      problem5c("aaab") returns "aaa"
      problem5c("abb") returns "bb"
      problem5c("abcbcdc") returns "ccc"
      problem5c("aaabcbcdca") returns "aaaa"
    Type hints:
      :type s: str
      :rtype: str
    """

    count = 1
    string1 = ''
    longest_length = 0

    for j in range(len(s)):
        letter = s[j]
        for k in range(len(s)):
            if s[k] == letter:
                count += 1

        if count > longest_length:
            longest_length = count
            string1 = str((count-1) * letter)
        count = 1

    return string1

    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # IMPORTANT:  See the HINT just below the DEF line.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
