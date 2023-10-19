
import math
import numpy as np
import matplotlib

# function 0
def circle_area(radius):
    """ Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """

    return math.pi * radius * 2

# function 1
def find_max(numbers):
    """
    Find the maximum number in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The maximum number in the list, or None if the list is empty.
    """
     
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# function 2
def recursive_factorial(n):
    """
    Calculate the factorial of an integer, using a recursive approach.

    Args:
        n (int): integer for which to calculate the factorial.

    Returns:
        int: The factorial of the input integer.
    """

    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# function 3
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert a temperature in Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 9/5
    return celsius

# function 4
def simulate_height_water_in_tank(H, F, A, a, dt, t, g=9.81, plot=False):
    '''function that simulates the height of water in a tank of time, given the input and output of water.
    The function uses a differential equation that uses Torricelli's law.

    dH = F/A - a/A*sqrt(2 g t)

    the differential equation is solved using Euler's method H[n] = H[n-1] + dh * dt

    :param float H: Initial height of water in tank
    :param float F: volume of water that flows into the tank (m3 /s)
    :param float A: area of the bottom of the water tank (m2)
    :param float a: size of the hole in the bottom of the tank (m2)
    :param float dt: size of each step of the simulation (s)
    :param float t: length of the simulation (s)
    :param float g: the gravitational constant. Default=9.81 (m/s2)
    :param bool plot: variable used to indicate in you want to plot your results
    :return: np.array with heights
    '''
    from pylab import subplots, show

    number_of_steps = int(np.round(t / dt, 0))
    height_water = np.zeros(number_of_steps, dtype=np.float32)
    height_water[0] = H

    for n in range(1, number_of_steps):
        dh = F / A - a / A * np.sqrt(2 * g * height_water[n - 1])
        height_water[n] = height_water[n - 1] + dh * dt

    if plot:
        fig, ax = subplots(1,1,figsize=(8,8))
        ax.set_title(f"H={H}, F={F}, A={A}, a={a}, g={g}")
        ax.set_xlabel('time (s)')
        ax.set_ylabel('Height water (m)')
        ax.plot(np.arange(0,t, dt), height_water)
        show()

    return height_water

    


