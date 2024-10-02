"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

import numpy 

num_lst = [1,2,3,4,5]


def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    num_lst = [1,2,3,4,5]
    
    x_sum = 0
    for i in num_lst:  # Finding x mean
        x_sum = x_sum + i
    x_mean = (1/x)*x_sum 
    
    x_squared_sum = 0
    for i in num_lst: # Finding the mean of squares
        x_squared_sum += i**2
    s_mean = x_squared_sum/x
    
    variance = s_mean - x_mean**2

    sd = variance**0.5
    
    return sd


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """ 
    num_lst = [1,2,3,4,5]
     
    x_sum = sum(num_lst)
    x_mean = x_sum/len(num_lst)
    
    x_squared_sum = sum(i**2 for i in num_lst)
    s_mean = x_squared_sum/len(num_lst)
    
    variance = s_mean - x_mean**2
    
    sd = variance**0.5
    
    return sd


print(f'This is the standard deviation of {num_lst} using loops: {std_loops(5)}')

print(f'This is the standard deviation of {num_lst} using sum and len: {std_loops(5)}')

print(f'This is the standard deviation of {num_lst} using the std() command: {numpy.std(num_lst)} ')




