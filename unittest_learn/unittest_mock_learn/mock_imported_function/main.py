from helpers import complex_function


# function_a is coupled to the output of complex_function
def function_a():
    print('main')
    return complex_function().upper()
