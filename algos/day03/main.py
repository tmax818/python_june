# Swap String For Array Negative Values
# Replace any negative array values with 'Dojo'.

arr = [1, -3, 4, -76, 8, -6, 98]

def replaceNegWithDojo(arrParam):
    newArray = []
    for i in arrParam:
        if(i < 0):
            print('Dojo')
            newArray.append('Dojo')
        else:
            print(i)
            newArray.append(i)
    print(newArray)
    return newArray


# print(replaceNegWithDojo(arr))


# Print Odds 1-255
# Print all odd integers from 1 to 255.

# for i in range(1,256):
#     if(i % 2 != 0):
#         print(i)


# Iterate and Print Array
# Iterate through a given array, printing each value.


def printEach(arrParam):
    for i in arrParam:
        print(i)

# printEach(arr)

# Get and Print Average
# Analyze an array’s values and print the average.

arr = [0,1,2,3,4,5,6,7]
def printAvg(arrParam):
    length = len(arrParam)
    sum = 0
    for i in arrParam:
        sum += i
    print(sum/length)

# printAvg(arr)
# Square the Values
# Square each value in a given array, returning that same array with changed values.
arr = [0,1,2,3,4,5,6,7]

def sqrVals(arrParam):
    for i in range(len(arrParam)):
        print("before ", arrParam[i])
        arrParam[i] = arrParam[i]**2
        print("after ",arrParam[i])



print(sqrVals(arr))

print(arr)

# Zero Out Negative Numbers
# Return the given array, after setting any negative values to zero.
arr = [3, -4, 98, -8, 9 , 5, -7]

def replaceNegWithZero(arrParam):
    for i in range(len(arrParam)):
        if(arrParam[i] < 0):
            arrParam[i] = 0

# replaceNegWithZero(arr)
# print(arr)

# Shift Array Values
# Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.

arr = [1,2,3,4,5] #=> [2,3,4,5,0] => [3,4,5,0,0]

# print(arr[-1])
# arr.pop(0)
# arr.append(0)
def shiftVals(arrParam):
    for i in range(len(arrParam)):
        if(i+1 == len(arrParam)):
            arrParam[i] = 0
        else:
            arrParam[i] = arrParam[i + 1]



shiftVals(arr)
print(arr)

