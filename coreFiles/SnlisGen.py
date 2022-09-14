# this is SNILS generator for single SNILS

import random
import math
from tkinter import *
import sys
sys.setrecursionlimit(10000)


def randomizer():

    # generating random 9 digits
    first = (random.randint(0, 9))
    sec = (random.randint(0, 9))
    third = (random.randint(0, 9))
    fourth = (random.randint(0, 9))
    fifth = (random.randint(0, 9))
    sixth = (random.randint(0, 9))
    seventh = (random.randint(0, 9))
    eighth = (random.randint(0, 9))
    ninth = (random.randint(0, 9))

    # pack them inside the list
    nums = [first, sec, third, fourth, fifth, sixth, seventh, eighth, ninth]

    # counting control num
    multiply_nums = ((nums[0] * 9) + (nums[1] * 8) + (nums[2] * 7)
                     + (nums[3] * 6) + (nums[4] * 5) + (nums[5] * 4)
                     + (nums[6] * 3) + (nums[7] * 2) + (nums[8] * 1))
    # print(multiply_nums) for debag
    # joining digits to each other

    numbers = int(''.join(map(str, nums)))

    # print(numbers) for debag

    # checking the control sum
    nums_to_count = multiply_nums

    if nums_to_count < 100:
        nums_to_count = multiply_nums

    elif nums_to_count <= 101:
        nums_to_count = 00

    elif nums_to_count == 100:
        nums_to_count = 00

    elif nums_to_count > 101:
        nums_to_count = nums_to_count % 101
        # print(nums_to_count)
        if 0 < nums_to_count < 10:
            nums_to_count = str('0' + str(nums_to_count))
            '''print(nums_to_count)
            print('less than 10')'''
    else:
        print('countingError')

    # getting string with SNILS
   # print((str(numbers) + str(nums_to_count)))

    snils = str(numbers) + str(nums_to_count)
    sys.stdout = open('snilsList.txt', 'a')
    print(snils)
    return randomizer()

print(randomizer())