#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:35:09 2018

@author: joe
"""


def fizzbuzz():
    count = 1
    while count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print('FizzBuzz')
            count += 1
        elif count % 3 == 0:
            print('Fizz')
            count += 1
        elif count % 5 == 0:
            print('Buzz')
            count += 1
        else:
            print(count)
            count += 1
   
fizzbuzz()
