#
# life.py - Game of Life lab
#
# Name: racahel kondrat
# Pledge: i pledge my honor that i have abided bythe stevens honor system
#

import random

import sys 

def createOneRow(width):  
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height): 
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A
    
def printBoard( A ):  
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):  
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''returns a 2d array of all live cells- with the value 1 -
    except for a one cell wide border of empty cells w/ the value 0
    around the edge of the 2nd array'''
    A = createBoard( w, h )
    
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = 1
    return A
            

def randomCells(w,h):
    '''returns an array of randomly assigned 1s and 0s except that the outer edge
    of the array is still completely empty'''
    A = createBoard( w, h )
    
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = random.randrange(0,2)
    return A

def copy(A):
    '''will make a deep copy of the 2nd array.'''
    output = createBoard( len(A[0]), len(A) )
  
    for row in range(len(A[0])):
        for col in range(len(A)):
            output[row][col]= A[row][col]
    return output
            
def innerReverse(A):
    '''creates a new generation of the same shape and size but the opposite of A's cells'''
    output = copy(A)

    for row in range(1, len(A[0]) - 1):
        for col in range(1, len(A) - 1):
            if A[row][col] == 1:
                output[row][col] = 0
            else:
                output[row][col] = 1    
    return output


def countNeighbors( row, col, A ):
    '''returns the number of live neighbors'''
    count = 0
    if A[row-1][col-1] == 1:
        count+=1
    if A[row-1][col] == 1:
        count+=1
    if A[row-1][col+1] == 1:
        count+=1
    if A[row][col-1] == 1:
        count+=1
    if A[row][col+1] == 1:
        count+=1
    if A[row+1][col-1] == 1:
        count+=1
    if A[row+1][col] == 1:
        count+=1
    if A[row+1][col+1] == 1:
        count+=1
    return count

def next_life_generation( A ):
    """ makes a copy of A and then advanced one generation of Conway's game of life within
    the *inner cells* of that copy. The outer edge always stays 0.
    """
    output = copy(A)
    for row in range(1, len(output) - 1):
        for col in range(1, len(output[0]) - 1):
            if A[row][col] == 1 and countNeighbors(row, col, A) > 3:
                output[row][col] = 0
            elif A[row][col] == 1 and countNeighbors(row, col, A) < 2:
                output[row][col] = 0
            elif A[row][col] == 0 and countNeighbors(row, col, A) == 3:
                output[row][col] = 1
    return output


