
################################ Notice ################################

# Maman 14 - Shavit Shabtay Michaeli , I.D. 205782659
# First, Since Python 3.7 Dictioneries are already sorted, in anyway, this code is should be sorted without the Python Hash tables sorting method.
# I've inserted in each of those algorithms counting which will count both *Comparisons* and *Assignments* any time that it be needed.
# Notice of the imports, The Jit is running on this file.
# Also notice that the Python system is avoiding from getting a big number of recursion steps. So I've changed it to allow us excecute this program.
# Thank You Very Much!!!
####################### Imports and System Controllers ########################

import warnings
warnings.filterwarnings("ignore")
from numba import jit #Jit import
import sys
import numpy as np
import random
sys.setrecursionlimit(10 ** 9)


################################ Question No.1 #################################
# This is the original algorithm from Maman 11, Which checking how many diffrents varibales are contained in the array.

def D1(A):
    @jit
    def temp():  # Initialize comp, assign, Usize
        comp = 0
        assign = 0
        USize = 1
        assign += 1  # assigning USize
        for i in range(1, len(A)):  # First for loop in this algorithm, in each iteration the 'U = True' which assigning each and coparrasing  through the for loop. Complexity of O(N).
            comp += 1
            U = True
            assign += 1
            for j in range(0,USize):  # Second loop of this algorithm.checking in each iteration, if the variable A[i] is equals to A[j]
                # if it is, the U Changing into False and j is changing into USize, to start running from this spot in the next iteration of the first loop,
                # if not, that means that we've reached all the differnce between the variables in the array.
                comp += 1
                if A[j] == A[i]:
                    comp += 1
                    U = False
                    j = USize
                    assign += 2
            if U == True:
                A[USize] = A[i]
                USize += 1
                assign += 2

        return comp, assign, USize

################################# Printing Q.1 #################################

    comp, assign, total_diffs = temp()
    print(f'Total comparisons: {comp}')
    print(f'Total assignments: {assign}')
    print(f'Total differences: {total_diffs}\n')


################################ Question No.2 #################################
# This question is using the Insertion Sort, which means, that in every iteration the number which provided by the array,
# is checking if the number itself is bigger than the number before him, if its not, the number is keep checking which number is smaller than him,
# if smaller number is found before the current number, the current number will be placed in the right postion just after the number which is smaller than him.
# if it not: the bigger number will remain in it's position on the array and the array continue to the next iteration.

def D2(A):
    @jit
    def temp():  # Initialize comp, assign, count
        comp = 0
        assign = 0
        count = 1
        assign += 1  # Count assigning
        for i in range(1, len(A)):  # First loop,
            comp += 1  # Compares in for loop
            key = A[i]
            j = i - 1
            assign += 2  # Assigning both key and j
            while j >= 0 and key < A[j]:  # Second loop
                comp += 1
                A[j + 1] = A[j]
                j -= 1
                assign += 2
            if A[j] != key:
                comp += 1
                count += 1
                assign += 1
            A[j + 1] = key
            assign += 1
        return comp, assign, count

################################# Printing Q.2 #################################

    comp, assign, total_diffs = temp()
    print(f'Total comparisons: {comp}')
    print(f'Total assignments: {assign}')
    print(f'Total differences: {total_diffs}\n')


################################ Question No.3 #################################
# This QuickSort Algorithm is using randomized pivot, for getting better run time results, his using recursion for both
# the QuickSort function and the recursion.
def D3(A):
    @jit
    def temp():
        # Sorting the array
        comp, assign = quickSort(A, 0, len(A) - 1)

        # Duplicate checking algorithm
        dup_list = [0] * 100
        for element in A:  # After using QuickSort,
            dup_list[element - 1] += 1
            comp += 1
            assign += 1

        # assign += len(A)  # For the dup_list assignment
        total_diffs = len([count for count in dup_list if count > 0])
        comp += 100 * 2  # For loop and loop condition
        return comp, assign, total_diffs

################################# Printing Q.3 #################################

    comp, assign, total_diffs = temp()
    print(f'Total comparisons: {comp}')
    print(f'Total assignments: {assign}')
    print(f'Total differences: {total_diffs}\n')

############################ QuickSort Function ################################
@jit
def quickSort(A, start, stop):
    comps = 0
    assigns = 0

    if (start < stop):
        comps += 1
        pivotindex, new_comps, new_assigns = partitionrand(A, start, stop)  # Getting Each iteration the new pivot
        comps += new_comps
        assigns += new_assigns

        new_comps, new_assigns = quickSort(A, start, pivotindex - 1)
        comps += new_comps
        assigns += new_assigns

        new_comps, new_assigns = quickSort(A, pivotindex + 1, stop)
        comps += new_comps
        assigns += new_assigns

    return comps, assigns

######################## Partition Random Function #############################

@jit
def partitionrand(A, start, stop):
    randpivot = random.randrange(start, stop)

    # Remember to add 2 assignments
    A[start], A[randpivot] = A[randpivot], A[start]

    pivot, comps, assigns = partition(A, start, stop)
    assigns += 2

    return pivot, comps, assigns

############################ Partition Function ################################

@jit
def partition(A, start, stop):
    comps = 0
    assigns = 0
    pivot = start #assiging pivot
    i = start + 1

    assigns += 2
    for j in range(start + 1, stop + 1):
        if A[j] <= A[pivot]:
            assigns += 3
            A[i], A[j] = A[j], A[i]
            i = i + 1
        comps += 2  # For loop and if
    A[pivot], A[i - 1] = \
        A[i - 1], A[pivot]
    pivot = i - 1
    assigns += 3
    return pivot, comps, assigns

################################ Question No.4 #################################
# This Algorithm is using the C Array counting sort, which uses an empty values array and by
# the C array is presenting the count of how many variables in the array are equals to the number of
# the place givin by the array. means C[0] will show how many times the number 1 is been provided by
# the A Array.

def D4(A):
    @jit
    def temp():
        assign = 0
        comp = 0
        count = 0
        assign += 1  # Assigning count
        C = [0] * 100
        assign += 1
        for i in range(len(A)):
            comp += 1
            C[A[i] - 1] = C[A[i] - 1] + 1
            assign += 1
        for i in range(len(C)):
            if C[i] != 0:
                comp += 1
                count += 1
                assign += 1
        return comp, assign, count


################################# Printing Q.4 #################################

    comp, assign, total_diffs = temp()
    print(f'Total comparisons: {comp}')
    print(f'Total assignments: {assign}')
    print(f'Total differences: {total_diffs}\n')

################################ Question No.5a #################################
# Both of those algorithms are Hash tables array using python dictionary functions.
# By using those function we can see each of our
def D5a(A):
    comp = 0
    assign = 0
    dup_list = {list1: {} for list1 in range(0, 10)}  # initializing the dup_list for using as hash table
    comp += 10
    assign += 10
    count = 0
    assign += 1
    for e in range(0, len(A)):
        comp += 1
        if A[e] // 10 in dup_list[A[e] % 10]:
            comp += 1
            dup_list[A[e] % 10][A[e] // 10] += 1
            assign += 1
        else:
            dup_list[A[e] % 10][A[e] // 10] = {}
            dup_list[A[e] % 10][A[e] // 10] = 1
            count += 1
            assign += 2
    total_diffs = count
################################# Printing Q.5a #################################

    print(f'Total comparisons: {comp}')
    print(f'Total assignments: {assign}')
    print(f'Total differences: {total_diffs}\n')

################################ Question No.5b #################################

def D5b(A):
    assign = 0
    comp = 0
    count = 0
    assign += 1  # Assigning count
    dup_list = {list1: 0 for list1 in range(1, 101)}  # Initialising the Hash table, The complexity of this for loop is O(100) ⇒ O(1)
    for element in A:  # After initialising, inputing the varible into the hash table while 'element' not finished checking all the elements at A,
        # This loop complexity is O(N), but, because it depends on the user to input a number, The finished complexity is O(1)
        if dup_list[element] != 0:
            dup_list[element] += 1
        else:
            dup_list[element] += 1
            count += 1  # counting the different keys inputted into the hash table/
        comp += 1  # adding comp into each if statement coperasing
        assign += 1  # adding assign into each assignment into the hash table
    total_diffs = count
    comp += 100 * 2  # For loop and loop condition
################################# Printing Q.5b #################################

    print(f'Total comparisons: {comp}')
    print(f'Total assignments: {assign}')
    print(f'Total differences: {total_diffs}\n')


################################ Main Function #################################
# This is the main function which containing the Array A Initialize, and contaion

def main():
    N = int(input("Please enter the array size:"))
    A = list(range(0, N))
    A = np.random.randint(1, 101, (N,))
    print(f'\nFor N = {N} numbers in D1:\n')
    D1(A.copy())
    print(f'For N = {N} numbers in D2:\n')
    D2(A.copy())
    print(f'For N = {N} numbers in D3:\n')
    D3(A.copy())
    print(f'For N = {N} numbers in D4:\n')
    D4(A.copy())
    print(f'For N = {N} numbers in D5a:\n')
    D5a(A.copy())
    print(f'For N = {N} numbers in D5b:\n')
    D5b(A.copy())



if __name__ == "__main__":
    main()
