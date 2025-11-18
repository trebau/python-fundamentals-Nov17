variable

# comment - what is it? A little note just for you
# a comment does not get read by python
# variable
# given it a name
# given it a value
variable_name = "hello world"
                    #string - a piece of text
print( variable_name )

my_favorite_dad_joke = "why did the scarecrow win an award? Becasue he was outstanding in his field!"

question = 'what do you call fake spaghetti?'
answer = 'an impasta'

formatted_joke = f"{question}  {answer}" + ". " + my_favorite_dad_joke


# print ( my_favorite_dad_joke )
# 
# print (formatted_joke)

# integer
number_of_snakes = 12

#floating point number or "float"
average_number_of_snakes = 9.8

# print (number_of_snakes)

# boolean
# true / false
i_am_true = True
i_am_false = False

first_name = "Trent"
last_name = 12
not i_am_truthy

first_name_is_not_string = type(first_name) != str
last_name_is_not_string = type(last_name) != str

#conditionals
if first_name == "Trent" and last_name == "Bauer":
    print("Welcome Trent")

    if number_of_snakes >= 10:
        print("you have a lot of snakes today Trent")

elif first_name_is_not_string or last_name_is_not_string: 
    print( "ENTRY MUST BE TEXT")
elif first_name:
    print("hello stranger")
else:
    print ("EMPTY FIRST NAME TRY AGAIN")


print("ALL DONE")


##################################################################################### #

Part 2 --- Funttions ----- #

def say_hello():
    #put whatever the function does right here
    print("hello")

#call funtion
what_we_get = say_hello()

print (what_we_get)

def add_one_plus_one():
    return 1+1

what_we_get = add_one_plus_one()

print( what_we_get)

#function with parameters
def add(number_one:int, number_two:int ):
    return number_one + number_two

result = add(1, 5)

def multiply (a,b,c=5):
    return a*b*c

result_two = multiply(5,2)

print (result_two)

print(result)

def dad_joke_creator(question:str, punchline:str):
    return f"{question} {punchline} :D"

dad_joke = dad_joke_creator("why can't your nose be 12 inches long?", "Becasue then it would be a foot!")

print(dad_joke)

# scope
outside_thoughts = "I am happy and well adjusted"
# 
# using the global variable
def think_about_thoughts():
    global outside_thoughts
    outside_thoughts = outside_thoughts + " " + "but I would like a sports car"

think_about_thoughts()

print(outside_thoughts)

def think_inside_thoughts():
    #delaring a new variable in the local scope
    outside_thoughts = "I am an outside thought I think"
    print(outside_thoughts)

think_inside_thoughts()

print(outside_thoughts)

def multiple_returns():
    #this first return ends the fucntion execution 
    return "I am the return"
#These other returns have no effect
    return "I'll be back"
    return "More Returns"
    return " EVEN MORE RETURNS"

result = multiple_returns()

print (result)

def login(username:str, password:str):
    if username and password:
        correct_username = "user123"
        correct_password = "password123"
        if username == correct_username and password == correct_password:
            return True
      
    
    return False
    
logged_in=login("user123", "password123") #True
print("Lgged In:", logged_in)

logged_in=login("henry123", "password123") #False
print("Lgged In:", logged_in)

logged_in=login("", "") #False
print("Lgged In:", logged_in)

def passable_function():
    pass


# Practice
# 
# takes in the total price of the meal, optionally add a tip, if there are multiple people divide the grand total by the number of people
# your output should be a float
# what happens if someone puts somehing that isn't a number
# what happens if the number of people is 0

def multiply (a,b,c=5):
    return a*b*c

result_two = multiply(5,2)

print (result_two)

Party_Equals_Zero = party == 0

def calculate_price(price:int, party:int=1, tip:int=1):
    if Party_Equals_Zero:
        print ("Party Must Be Greater Than Zero")
        if price and party and tip:
            return (price*(tip+1))/party

result = calculate_price(50,0,.20)

print(result)

def restaurant_bill_calculator(total:float, number_of_guests:int=1, tip_percentage:float=0.0):

    if type (total) == int and type(number_of_guests) == int and type(tip_percentage) == float:
        if number_of_guests > 0:
            subtotal = total * (1 + tip_percentage)
            per_guest_total = subtotal / number_of_guests
            return float(per_guest_total)
        else:
            return "get some friends"
    else:
         return "incorrect data types, try again"

the_bill = restaurant_bill_calculator(50,1,0.0)
print("the bill:", the_bill)

the_bill = restaurant_bill_calculator(50,2,0.0)
print("the bill:", the_bill)

the_bill = restaurant_bill_calculator(50,2,.20)
print("the bill:", the_bill)

the_bill = restaurant_bill_calculator(50)
print("the bill:", the_bill)

the_bill = restaurant_bill_calculator(50,0.0)
print("the bill:", the_bill)

the_bill = restaurant_bill_calculator("50 buckos",5)
print("the bill:", the_bill)

the_bill = restaurant_bill_calculator(50,"six",0.0)
print("the bill:", the_bill)

#this is the end of the file