"""
A very simple class to make running tests a bit simpler.
There are much stronger frameworks possible; this is a KISS framework.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  October 2015.
"""
import time
import sys


class SimpleTestCase(object):
    """
    A SimpleTestCase is a test to run.  It has:
      -- The function to test,
      -- its argument(s), and
      -- its correct returned value.
    """

    def __init__(self, function, arguments, correct_returned_value,
                 tolerance=None):
        """
        The arguments are:
          -- The function to test
          -- The arguments to use in the test, as a sequence
          -- The correct returned value.

        For example, if the intended test is:
           foo(blah1, blah2, blah3)
        with correct returned value True,
        then its SimpleTestCase would be construced by:
          SimpleTestCase(foo, [blah1, blah2, blah3], True)

        Note that the arguments must be a SEQUENCE even if there is
        only a single argument and an EMPTY sequence if there are no
        arguments.  For example:
          foo(blah)   with correct returned value 88
        would be constructed by:
          SimpleTestCase(foo, [blah], 88)
        """
        self.function_to_test = function
        self.arguments_to_use = arguments
        self.correct_returned_value = correct_returned_value
        self.tolerance = tolerance

    def run_test(self):
        """
        Runs this test, printing appropriate messages.
        Returns True if your code passed the test, else False.
        Does not attempt to catch Exceptions.
        """
        try:
            your_answer = self.function_to_test(*(self.arguments_to_use))
        except Exception:
            self.print_result('CRASHED (i.e., raised an Exception) on',
                              is_error=True)
            SimpleTestCase.print_failure_message(
                '  Your code CRASHED (i.e., raised an Exception)')
            raise

        if not self.tolerance:
            passed_test = your_answer == self.correct_returned_value
        else:
            try:
                difference = your_answer - self.correct_returned_value
                passed_test = abs(difference) < self.tolerance
            except Exception:
                passed_test = False

        self.print_result('PASSSED' if passed_test else 'FAILED')

        print('  Your code returned ..........:', your_answer)

        return passed_test

    def print_result(self, result, is_error=False):
        file = sys.stderr if is_error else sys.stdout
        if file == sys.stderr:
            sys.stdout.flush()
            time.sleep(1)  # For stdout messages to finish first

        print()
        print('Your code {:6} this test'.format(result), file=file)

        if len(self.arguments_to_use) == 0:
            format_string = '  ( )'
        else:
            f_beginning = '  {}( {}'
            f_args = ', {}' * (len(self.arguments_to_use) - 1)
            format_string = f_beginning + f_args + ' )'
        print(format_string.format(self.function_to_test.__name__,
                                   *(self.arguments_to_use)))

        print('  The correct returned value is:',
              self.correct_returned_value)

    @staticmethod
    def print_failure_message(message='  *** FAILED the above test. ***',
                              flush_time=1.0):
        """ Prints a message onto stderr, hence in RED. """
        time.sleep(flush_time)
        print(message,
              file=sys.stderr, flush=True)
        time.sleep(flush_time)

    @staticmethod
    def run_tests(function_name, tests):
        print()
        print('--------------------------------------------------')
        print('Testing the   {}   function:'.format(function_name))
        print('--------------------------------------------------')

        failures = 0
        for k in range(len(tests)):
            result = tests[k].run_test()
            if result is False:
                failures = failures + 1

        if failures > 0:
            text = '*** YOUR CODE FAILED SOME TESTS. ***'
            asterisks = len(text) * '*'
            message = '\n{}\n{}\n{}\n'.format(asterisks, text, asterisks)
            SimpleTestCase.print_failure_message(message)
