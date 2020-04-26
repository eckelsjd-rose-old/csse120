########################################################################
#
# Run this module and review the code to see if you can trace the flow of program execution
#
########################################################################


def main():
    hello()
    goodbye()
    hello()
    hello()

    hello_and_goodbye()


def hello():
    print('Hello!  How are things?')


def goodbye():
    print('Goodbye!')
    print('   Ciao!')
    print('   Bai bai!')


def hello_and_goodbye():
    hello()
    goodbye()


main()
