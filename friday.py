from collections import Counter



# Data Structure & Algorithms #

# data structure - list, dictionary - a piece of data containing other pieces of data

# algorithm - a set of instructions

# Example Challenege:
# write a function get_average() which accepts list_of_numbers:list\
#   Return all of those numbers averaged together

# 
# def get_average(list_of_numbers):
#     # pseudocode
#     #sum all the numbers
#     #iterate through and add all those numbers to a total
#     total = 0
#     for num in list_of_numbers:
#         total = total + num
#     print(total)
#     #divide by the length of the list
#     # Get length of the list
#     length = len(list_of_numbers)
#     result = total/length
#     #return all numbers averaged
#     return result

#STEP ONE - Make it work
#STEP TWO - then you can refine



def get_average(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)

get_average_lam = lambda list_of_numbers: sum(list_of_numbers)/len(list_of_numbers)
   

# Challenge One:
# Write a function bill_calculator() which accepts item_price_list:list, tax_rate:float and tip:float.
#     The item_price_list is a list of prices as floats such as [9.99, 5.80, 12.99]
#     tax_rate and tip are floats  that indicate the percentage that goes to each such as 0.087 and 0.20
#     The function returns the sum of the list plus the additional taxes and tips applied
#     BONUS: The function also accepts an optional parameter party_size which defaults to 1 and automatically divides the total by the number of people dining

def bill_calculator(item_price_list, tax_rate, tip_percentage,party_size=1):
    #add the items together
    total = ((sum(item_price_list))+((tax_rate+tip_percentage)*sum(item_price_list)))
    return total/party_size

    #return total and divide by party size if party size is greater than 1


# Challenge Two:
# Write a function reverse_list()  which accepts a data_list:list of arbitrary data
#     The function returns the list in reverse order
#     Do not use .reverse() or .sort() for this challenge
#     BONUS: Allow the function to accept and reverse a string as well


my_list = [1,2,3,4,5,6]


def reverse_list(data_list):
    #we need to reverse a list so 1,2,3 -> 3,2,1
    #maybe we can add the numbers to the end f the list then pop the initial numbers
    for item in data_list:
        x = data_list.pop
        data_list.append (x)
    return data_list

def reverse_list_2(data_list):
    new_data_list = []
    #we need to reverse a list so 1,2,3 -> 3,2,1
    #maybe we can add the numbers to the end f the list then pop the initial numbers
    for item in data_list:
        print(data_list)
        item = data_list.pop()
        new_data_list.append (item)
        print(new_data_list)
    return new_data_list

#while loop with an iterator

def reverse_list_3(data_list):
    new_data_list = []
    #we need to reverse a list so 1,2,3 -> 3,2,1
    #maybe we can add the numbers to the end f the list then pop the initial numbers
    while len(data_list) > 0:
        print(data_list)
        item = data_list.pop()
        new_data_list.append (item)
        print(new_data_list)
    return new_data_list

# potential answer

def reverse_list_4(data_list):
    reversed_list = []
    for item in data_list:
        reversed_list.insert(0,item)
    if isinstance(data_list,str):
        return "|||".join(reversed_list)
    return reversed_list

# potential answer with slice

def reverse_list_5(data_list):
    return data_list[::-1] #slice



# Challenge Three:
# Write a function character_counter() which accepts string:str as an argument
#     The function returns a dictionary with each key being a character and each value being the number of times it appeared
#     Example: character_counter("data") >>> { "d": 2, "a": 1, "t": 1 }
#     Example: character_counter("character") >>> { "c":2, "h":1, "a":2, "r":2, "t":1 }
#     Hint: There is a way to iterate through string characters
#     Hint: You should start with an empty dictionary
#     Hint: When assessing a character you may do something differently depending on whether it's in the dictionary already or not...


def character_counter(string:str):
    pass
    char_list = []
    char_num = {}
    for char in string: #you can iterate through a string, no need to create a list
        char_list.append (char)
        print (char_list)
    for item in char_list:
        if item in char_num:
            char_num[item] += 1
        else:
            char_num[item] = 1
    return char_num


#potential answer

def character_counter_2(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count

# Bonus Challenge One:
# Write a function fibonacci_of() which takes in an integer n:int  which gives the nth integer in the fibonacci sequence
#     You can find more information about the the fibonacci sequence here: link
#     There is something known as a recursive function where a function can call itself... use that information wisely!

def fibonacci_of(n):
    # return the nth number in the sequence
    # we need to calculate the number in the sequence by taking the two preceeding numbers and adding them together
    #0,1,1,2,3,5,8,quit(0),21...
    #if n = 6 then return index6 = 13
    num_list = [0,1]
    while len(num_list) < n:
        new_num = num_list[-1] + num_list[-2]
        print(new_num)
        num_list.append(new_num)
        print(num_list)
    return num_list[n-1]

#other answer

def fibonacci_2(n):
    print(f"fibonacci for n={n}")
    if n == 0:
        return 0
    if n == 1:
        return 1
    #recursive function
    return fibonacci_2(n-1) + fibonacci_2(n-2)


# Bonus Challenge Two:
# Write a function rot_13() which accepts a string:str as an argument
#     The function returns an altered string with each of the letter characters "rotated" 13 places in the alphabet
#     Example: rot_13("hello there") >>> "uryyb gurer"
#     Hint: There is a function chr() which allows you to see the character for an ascii code and ord() which allows you to see the ascii code for a character...
#     There are multiple ways of doing this!

def rot_13(string:str):
    result = ""
    for char in string:
        if 'a' <= char <= 'm':
            result += chr(ord(char) + 13)
        elif 'n' <= char <= 'z':
            result += chr(ord(char) - 13)
        else:
            result += char
    return result


#API KEY - authorization for your account to access an api

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')

print(API_KEY)

# make the request

import requests

def fetch_animal_facts(animal:str):
    base_url = "https://api.api-ninjas.com/v1/animals?name="
    response = requests.get(base_url+animal, headers={'X-Api-Key': API_KEY})
    return response

