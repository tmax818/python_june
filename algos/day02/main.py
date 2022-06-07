# Print 1-255
# Print all the integers from 1 to 255.

# for i in range(1,256):
#     print(i)

# Print Sum 0-255
# Print integers from 0 to 255, and with each integer print the sum so far.

# sum = 0
# for i in range(256):
#     sum = sum + i
#     print("the number is",i)
#     print("The sum is currently", sum)

# Find and Print Max
# Given an array, find and print its largest element.
test_array = [1,2,3,4, 654,5,6,7,455]
test_array1 = [1,2,3,4]

# def printMax(theArrayParam):
#     max = theArrayParam[0]
#     for i in theArrayParam:
#         if(i > max):
#             max = i
#     print(max)


# printMax(test_array)
# printMax(test_array1)

# Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).

# oddList = []

# for i in range(1,256):
#     if(i % 2 != 0):
#         oddList.append(i)
# print(oddList)

# Greater Than Y
# Given an array and a value Y, count and print the number of array values greater than Y.

# test_array = [1,2,3,4, 654,5,6,7,455]
# test_array1 = [1,2,3,4]

# def greaterThanY(arrParam, yParam):
#     count = 0
#     for i in arrParam:
#         if(i > yParam):
#             count += 1
#     print(count)



# greaterThanY(test_array1, 20)


# Max, Min, Average
# Given an array, print the max, min and average values for that array.

testarray = [1,2,3, 5, 78, 4]

def maxMinAvg(arrParam):
    max = arrParam[0]
    min = arrParam[0]
    sum = 0
    for i in arrParam:
        sum += i
        if(i > max):
            max = i
        if(i < min):
            min = i
    print(max, min, sum/len(arrParam))

maxMinAvg(testarray)



# Swap String For Array Negative Values
# Replace any negative array values with 'Dojo'.


# Print Odds 1-255
# Print all odd integers from 1 to 255.


# Iterate and Print Array
# Iterate through a given array, printing each value.


# Get and Print Average
# Analyze an array’s values and print the average.


# Square the Values
# Square each value in a given array, returning that same array with changed values.


# Zero Out Negative Numbers
# Return the given array, after setting any negative values to zero.


# Shift Array Values
# Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.