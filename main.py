#!/usr/bin/python

import random
import os
import time
current_matrix = [[random.choice([' ',u'\u2588',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']) for i in list(range(0,80))] for j in list(range(0,40))]

def edges(matrix):
    for i in list(range(0,40)):
        for j in list(range(0,80)):
            if(i == 0 or i == 39 or j == 0 or j == 79):
                current_matrix[i][j] = '-'
edges(current_matrix)
next_matrix = current_matrix

def print_matrix(matrix):
    for i in list(range(0,40)):
        for j in list(range(0,80)):
            print(matrix[i][j], end="")
        print()

def adjacent_counter(x, y):
    counter = 0
    for i in list(range(x-1,x+2)):
        for j in list(range(y-1,y+2)):
            if(i == x and j == y):
                counter = counter
            else:
                if(current_matrix[i][j] == u'\u2588'):
                    counter = counter + 1
    return counter

generation_counter = 0

while(True):
    os.system("clear")
    print_matrix(current_matrix)
    print("Generation : ",generation_counter, end="")
    generation_counter += 1
    time.sleep(0.20)
    for i in list(range(1,39)):
        for j in list(range(1,79)):
            if(i == 1):
                current_matrix[i][j] = ' '
            elif(i == 38):
                current_matrix[i][j] = ' '
            elif(j == 1):
                current_matrix[i][j] = ' '
            elif(j == 78):
                current_matrix[i][j] = ' '
            else:
                alive = adjacent_counter(i,j)
                if(current_matrix[i][j] == ' '):
                    if(alive == 3):
                        next_matrix[i][j] = u'\u2588'
                else:
                    if(alive < 2):
                        next_matrix[i][j] = ' '
                    elif(alive > 3):
                        next_matrix[i][j] = ' '
                    elif(alive == 2):
                        next_matrix[i][j] = u'\u2588'
                    elif(alive == 3):
                        next_matrix[i][j] = u'\u2588'
    current_matrix = next_matrix
