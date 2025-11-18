# 
# def create_full_name(first_name:str, last_name:str):
#     if type(first_name) != str or type(last_name) != str:
#         return "Name Must Be Text"
#     else:
#         return(first_name + " " + last_name)
# 
# answer_1 = create_full_name("Trent", "Bauer")
# 
# # print(answer_1)
# 
# 
# 
# 
# def c_to_f(temp_celsius:int):
#     if type(temp_celsius) != int:
#         return "Temperature Must Be a Number"
#     else:
#         return round((temp_celsius*9/5) + 32, 2)
# 
# answer_2 = c_to_f(28)
# 
# # print(answer_2)
# 
# 
# def open_thieves_cave(Passphrase:str):
#     if type(Passphrase) != str: 
#         return "Passphrase Must Be a Word"
#     if Passphrase == "open sesame":
#         return True
#     else:
#         return False
#     
# 
# answer_3 = open_thieves_cave("open sesame")
# 
# # print(answer_3)
# 
# 
# # LIST # 
# 
# sodas = [ "Coke", "Pepsi", "Dr Pepper", "Sprite" ]
# 
# # print(sodas)
# 
# # index - where it is in the list
# # Python indexing starts at 0
# # Indexes start at 0 and they must be integers
# # if we have negative indexes (except 0) they will count from the end instead of the beginning
# 
# sodas[0] # "Coke"
# 
# sodas[3] or sodas[-1] # "Sprite"
# 
# sodas[1]= "Root Beer" #Changes "Pepsi" to "Root Beer"
# 
# #you may use different types of data in a list
# 
# different_stuff = [True, "whatever", 12, 12.0, [], "The End"]
# 
# listception = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# 
# #this will access the first list's second element
# listception[0][2] #2
# 
# # how do we add to the end of a list
# sodas.append("Fanta")
# sodas.append("Cream Soda")
# 
# #how do we see what the length of a list is
# len(sodas) #6
# 
# #How to add an item to a secific postiion in a list
# sodas.insert(0, "Diet Coke Zero")
# 
# #If I want to sort
# 
# sodas.sort() #will sort alphabetically
# 
# #To remove last item
# sodas.pop()
# 
# #To remove an item by its index
# sodas.pop(3)
# 
# #lambdas - short function
# plus_one = lambda x: x+1
# 
# create_fullname = lambda first_name, last_name: first_name + " " + last_name
# 
# #higher order funtion - takes in a function and does something with it
# 
# def do_three_times (fn):
#     fn()
#     fn()
#     fn()
# 
# def say_hi():
#     print("HI")
# 
# 
# pass_in_3 = lambda fn: fn(3)
# 
# # result = filter(lambda soda: soda == "Diet Coke Zero", sodas)
# 
# # list(result)
# 
# # print(sodas)
# # print(result)
# 
# furniture = ["chair", "table", "bed"]
# 
# 
# # TUPLE #
# 
# # we may not alter or mutate the tuple
# # when we create the tuple it will be like this until the program ends
# my_tuple = ("pizza", "hamburger", "hotdog", "salad")
# 
# 
# # SET #
# 
# #sets are unordered, unique data
# 
# my_set=(1,2,3,4,5,6,7,7,7,7,7) # {1,2,3,4,5,6,7}
# 
# # DICTIONARIES
# 
# my_dict = {'key': 'value'}
# 
# person = {
#     'first_name': 'Trent', 
#     'last_name' : 'Bauer',
#     'height' : '6 feet 4 inches',
#     'age' : '28',
#     'favorite_sodas': ['Coke', 'Pepsi']
# }
# 
# # print(person['height']) # accesses the height in the dict
# 
# # person ['fav_movie'] # will result in a key error
# 
# # person.get('fav_movie') # will not result in a key error
# 
# person['first_name'] = "TJ"
# 
# def legally_able_to_drive(person:dict):
#     return person['age'] >=16
# 
# # LOOPS and ITERATION #
# 
# # for item in sodas:
# #     print(item)
# # 
# # while False:
# #     print("hello")
# 
# index = 0
# 
# while index < len(sodas):
#     print(sodas[index])
#     index += 1
# 
# #list comprehension
# 
# empty_sodas = [("Empty " + item) for item in sodas]
# 
# 
# shaken_sodas = [s+" Exlosion" for s in sodas]
# 
# my_numbers = [1,2,3,4,5]
# squared = [num * num for num in my_numbers]
# 
# result = squared

# print(result)

# new function called fizz_buzz_list
# this accepts a list as an argument
# with the list I want to see for each item inside whether that item is cleanly divisible by 3 or 5
# if the number is divisible by 3 we replace the item with "Fizz"
# if the number is divisible by 5 we replace the item with "Buzz"
#if the number is divisible by 3 AND 5 we replace the item with "Fizz Buzz"
# if not divisible by either we leave the umber as is
# return the altered list

test_case_one = [1,2,3,6,7,8]

test_case_two = [52, 55, 98, 133]

test_case_three = [6081, 1200, 134, 547, 896, -200, -35, -6081, 0]

# def fizz_buzz_list(list_of_numbers):
#     for number in list_of_numbers:
#         if number % 3 == 0 and number % 5 == 0:
#             index = list_of_numbers.index(number)
#             list_of_numbers[index] = 'Fizz Buzz'
#         # if the number is divisible by three
#         elif number % 3 == 0:
#             #replace the number with Fizz by first getting its index
#             index = list_of_numbers.index(number)
#             list_of_numbers[index] = 'Fizz'
#         elif number % 5 == 0:
#             index = list_of_numbers.index(number)
#             list_of_numbers[index] = 'Buzz'
#     return list_of_numbers

def fizz_buzz_list(list_of_numbers):
    index=0
    while index < len(list_of_numbers):
        if list_of_numbers[index] % 3 == 0 and list_of_numbers[index] % 5 == 0:
            list_of_numbers[index] = "Fizz buzz"
        elif list_of_numbers[index] % 3 == 0:
            list_of_numbers[index] = "Fizz"
        elif list_of_numbers[index] % 5 == 0:
            list_of_numbers[index] = "Buzz"
        index += 1
    return list_of_numbers
            