# wednesday review #

#date_reviewed = datetime.date(2025, 11, 20)
# 
# from movie import MovieReview
# 
# import datetime
# 
# Predator = MovieReview("Predator", "Trent Bauer", 4, (datetime.date(2025,11,6)))
# 
# # ERROR HANDLING #
# 
# def divide_numbers(num_one, num_two):
#     if type(num_one) != int or type(num_two) != int:
#         raise TypeError("Inputs must be integers")
#     try:
#         print(num_one / num_two)
#     except ZeroDivisionError as error:
#         print( f"could not divide {num_one} by {num_two}")
#     finally:
#         print("FUNCTION DONE")
# 
# def cube_number(number):
#     try:
#         number ** 3
#     except TypeError:
#         return "This data type cannot be cubed"
# 
# try:
#     divided_by_zero = 100/0
# except:
#     print("I could not divide by zero... WOMP WOMP")
# 
# print ("I am below the error")


# HTTP REQUESTS #

import requests 

def get_dad_joke():
    try:
        response=requests.get("https://icanhazdadjoke.com",headers={"Accept": "text/plain"}) 
        joke_text = response.text
        return joke_text
    except:
        print("Unable to fetch dad joke")

# new_joke = get_dad_joke()


def fetch_number_of_jokes(num_jokes):
    jokes_list = []
    for _ in range(num_jokes):
        fetched_joke = get_dad_joke()
        jokes_list.append(fetched_joke)
    return jokes_list

# WRITING TO JSON FILES #

import json

def put_in_json_file(list_data):
    current_jokes = get_from_json_file()
    with open('jokes.json', 'w') as json_file:
        combined_jokes = current_jokes + list_data
        json.dump(combined_jokes,json_file, indent=4)

def get_from_json_file():
    with open('jokes.json', 'r') as json_file:
        data = json.load(json_file)
        return data
    

# BUILIDING PROGRAM #

# user stories ----> a user will be able to 

# a user will be able to boot up the proram and see a menu
# a user will be able to fetch a new dad joke
# a user will be able to save or discard a fetched dad joke
# a user will be asnle to see their saved dad jokes
# a user will be able to exit the program

import time

class DadJokeApplication:

    running = True
    
    def run(self):
        while self.running:
            self.menu()
            user_choice = input("Please choose an option: ")
            time.sleep(1)
            print("You chose: ", user_choice)
            if user_choice == "1":
                self.get_dad_joke()
            elif user_choice == "2":
                self.print_saved_dad_jokes()
            elif user_choice == "3":
                self.exit()
            else:
                time.sleep(1)
                print("\nPlease choose a valid option! (┛◉Д◉)┛彡┻━┻ \n")

    def menu(self):
        print("Welcome to the Dad Jokes App--")
        print("1. Get new dad joke")
        print("2. See saved dad jokes")
        print("3. Exit")

    def get_dad_joke(self):
        time.sleep(1)
        new_joke = fetch_number_of_jokes(1)
        print("-----------------------------------")
        print(new_joke)
        print("-----------------------------------")
        user_input = input("Save Joke?  [Y/N]")
        time.sleep(1)
        if user_input == 'Y':
            print("Saving this gem of a joke")
            put_in_json_file(new_joke)
        else:
            print("Discarding the Joke")

    def print_saved_dad_jokes(self):
        time.sleep(1)
        print("-----------------------------------")
        saved_jokes = get_from_json_file()
        for joke in saved_jokes:
            print(joke)
        print("-----------------------------------")

    def exit(self):
        self.running = False
        print("\nDeuces!\n")

app = DadJokeApplication()
app.run()
    