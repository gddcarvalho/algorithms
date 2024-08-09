import sys
from collections import Counter

#1- Write a script to count the number of occurrences of the given element in an array. 	
# arr = [1, 2, 3, 4, 4, 3]
# given_element = int(sys.argv[1])
# element_count = 0

# for element in arr:
#     if (element == given_element):
#         element_count += 1

# print("Number of ocurrences of the given element = {}".format(element_count))

#2- Given a number in an array form. Write a program to move all zeros to the end. 	
# arr = [1, 0, 0, 4, 4, 3]

# for idx, element in enumerate(arr):
#     if (element == 0):
#         arr.remove(arr[idx])
#         arr.append(0)

# print("Final array = {}".format(arr))

#3- Given are two ordered lists of size 7 and 3. The first list has three vacant spots in the end. Merge them in a sorted manner with minimum no. of steps.
# arr1 = [1, 2, 3, 5, 7, 8, 10]
# arr2 = [4, 6, 9]

# arr1.extend(arr2)
# arr1.sort()

# print("Final array = {}".format(arr1))

#4- Write a script to print the no. of occurrences of a given character or all letters in a string. 

# str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# given_character = sys.argv[1]
# char_count = 0

# for character in str:
#     if (given_character == character):
#         char_count += 1

# print("Number of ocurrences of a character = {}".format(char_count))

#5- How to reverse an array in the subset of N? e.g. Input: [1,3,5,7,9,11,15,17,19], Output: [5,3,1,11,9,7,19,17,15]. 

# arr = [1,3,5,7,9,11,15,17,19] # len(arr) = 9
# temp_arr = []
# final_arr = []

# subset = int(sys.argv[1]) #  = 3
# iterations = len(arr) / subset

# for idx, element in enumerate(arr):
#     if (subset > len(arr)):
#         final_arr = arr
#         break

#     temp_arr.append(element)
#     if (len(temp_arr) >= subset):
#         temp_arr.reverse()
#         final_arr.extend(temp_arr)
#         temp_arr.clear()
#         iterations -= 1
        
#         if (iterations >= 1):
#             continue
#         else:
#             if (len(arr) == len(final_arr)):
#                 break
#             else:
#                 temp_arr = (arr[len(final_arr):len(arr)])
#                 temp_arr.reverse()
#                 final_arr.extend(temp_arr)
#                 temp_arr.clear()

# print("Ordered array in the subset of {} = {}".format(subset, final_arr))

#6- Write code to count the duplicate characters in a given string. 	

# str = "Lorem ipsum dolor sit amet"
# new_arr = []
# dupl_count = 0

# for character in str:
#     if character not in new_arr:
#         new_arr.append(character)
#     else:
#         dupl_count += 1
        
# print("Number of duplicate characters = {}".format(dupl_count))

#7- Calculate the frequency of characters in a string. Print each char with its frequency. e.g. For input <abcabc>, output should be <(a,2),(b,2),(c,2)>.
# string = "abcabce"
# print(Counter(string))

#8- Print the first and final occurrence of a number in a sorted array of integers. e.g. int[] list = {1,2,3,4,5,5,7,8} 
# arr_of_interegers = [1,2,5,3,4,5,5,7,8]
# a_number = int(sys.argv[1])
# pos = []

# for idx, element in enumerate(arr_of_interegers):
#     if (element == a_number):
#         pos.append(idx)

# if (pos[0] == pos[-1]):
#     print(pos[0])
# else:
#     print(pos[0], pos[-1])


#9- Write a program to print the first non-repeated char in a string. e.g. A string “Is it your first company” returns ‘u’. 	
# string = "Is it your first company"
# arr = []

# def check_dup(entry_point):
#     no_of_chars = Counter(entry_point)
#     for char in entry_point.lower():
#         if (no_of_chars[char] == 1):
#             arr.append(char)

# check_dup(string)
# print(arr[0])

#10- Write code to print a 2×2 matrix in the spiral format. -

#https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

# DATA Structures in Python

# left rotation

# def rotateLeft(d, arr):
#     rotated_arr = []
#     arr_len = len(arr)
#     aux = 0
#     rotate_idx = d

#     while (rotate_idx < arr_len):
#         rotated_arr.insert(aux, arr[rotate_idx])
#         aux += 1
#         rotate_idx += 1
    
#     rotate_idx = 0

#     while (rotate_idx < d):
#         rotated_arr.insert(aux, arr[rotate_idx])
#         aux += 1
#         rotate_idx += 1 

#     print("Left rotation = {}".format(rotated_arr))

# rotateLeft(2, [1, 2, 3, 4, 5])

# right rotation

# def rotateRight(d, arr):
#     rotated_arr = []
#     arr_len = len(arr)
#     aux = 0
#     rotate_idx = d

#     while (rotate_idx < arr_len):
#         rotated_arr.insert(rotate_idx, arr[aux])
#         aux += 1
#         rotate_idx += 1
    
#     rotate_idx = 0

#     while (rotate_idx < d):
#         rotated_arr.insert(rotate_idx, arr[aux])
#         aux += 1
#         rotate_idx += 1 

#     print("Right rotation = {}".format(rotated_arr))

# rotateRight(3, [1, 2, 3, 4, 5])

#Insertion sort algorithm

# array = [5,6,2,3,8]

# for j in range(1, len(array) - 1):
#     key = array[j]
#     i=j-1

#     while i >= 0 and array[i] > key:
# 	    array[i+1] = array[i]
# 	    i=i-1
	
#     array[i+1]=key

# print("Insertion sorted = {}".format(array))

#Bubble sort algorithm

# array = [5,6,2,3,8]
# k = 0

# while k == 0:
# 	k = 1
# 	for i in range(0, len(array) - 1): #i until 5
# 		if (array[i] > array[i+1]):
# 			aux = array[i]
# 			array[i] = array[i+1]
# 			array[i+1] = aux
# 			k = 0

# print("Bubble sorted = {}".format(array))

#Selection sort algorithm

# array = [15, 7, 1, 4 ,18]

# for i in range(0, len(array) - 1): #0 until 5
#     min = i
    
#     for j in range(i+1, len(array) -1):
#         if (array[j] < array[min]):
# 	        min = j

#     if (min != i):
# 	    aux = array[i]
# 	    array[i] = array[min]
# 	    array[min] = aux

# print("Selection sorted = {}".format(array))

# parsing operations, maps and dicts
# some_string = "/* Device1 NullPointerError, Device2 SomeOtherStupidError, Device3 FodaSe */"

# elements = []

# for item in some_string.replace('/*', '').replace('*/', '').split(', '):
#     elements.append({
#                        "device": item.split(' ')[0],
#                        "error": item.split(' ')[1]
#                      })

# def return_devices_with_error(some_error):
#     for item in elements:
#         if item["error"] == some_error:
#             print("Found device= {} with error= {}".format(item["device"], item["error"]))

# return_devices_with_error("SomeOtherStupidError")

# A Better way would be:

# Python3 code to convert  
# a string to a dictionary 
  
# Initializing String  
# string = "A - 13, B - 14, C - 15"
  
# # Converting string to dictionary 
# Dict = dict((x.strip(), y.strip()) 
#              for x, y in (element.split('-')  
#              for element in string.split(', '))) 
  
# print(Dict) #{'C': '15', 'A': '13', 'B': '14'}

string = "A - 13, B - 14, C - 15"
  
# Converting string to dictionary 
for element in string.split(', '):
    for x, y in element.split('-'):
        print(x)
        print(y)
        #Dict = dict(device=x.strip(), error=y.strip())

#print(Dict) #{'C': '15', 'A': '13', 'B': '14'}