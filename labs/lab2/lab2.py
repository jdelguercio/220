# 1: What will this program do?
# This program will take as many numbers as the user inputs spit out the rms average, the harmonic mean, and the geometric mean

# 2: inputs: how many numbers, numbers, output: rms avg, harmonic mean, geometric mean

# 3: step-by-step:
    # ask the user for number of values they wish to enter
    # ask the user for each individual number
    # calculate rms avg, harmonic mean, and geometric mean
    # print results to user

import math

def CalculateAverages():
    n = eval(input('how many values would you like to enter? '))
    rms_sum = 0
    harmo_sum = 0
    geo = 1
    for _ in range(0, n):
        temp = eval(input('enter value: '))
        rms_sum += temp**2
        harmo_sum += 1/temp
        geo *= temp
    rms = math.sqrt(rms_sum / n)
    harmo = n/harmo_sum
    geomet = geo ** (1 / n)
    print('rms average: ', round(rms,3))
    print('harmonic mean: ', round(harmo,3))
    print('geometric mean: ', round(geomet,3))
