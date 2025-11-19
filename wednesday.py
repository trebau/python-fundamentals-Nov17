# 
# ### Tuesday Review ###
# 
# plants = ["tree", "flower", "fungus", "moss"]
# 
# def fungus_among_us(plants):
#     for plant in plants:
#         if plant == "fungus":
#             return True
#     return False
#     
# 
# item_costs = [12.99, 5.85, 14, 16]
# 
# def total_bill(item_costs):
#     return sum(item_costs)
#     
#     
# total_bill = lambda item_costs: sum(item_costs)
# 
# list_of_numbers=[1,2,3,4,5,6]
# 
# def halfway_there(list_of_numbers):
#     halfway = round(len(list_of_numbers)/2)
#     list_of_numbers.insert(halfway, "HALFWAY")
#     return list_of_numbers
# 
# 


# IMPORTING MODULES #

from robot import robot_uprising, Robot

# list_of_angry_bots = ["ANGRY " + bot for bot in list_of_bots]

wall_e = Robot("WALL-E", "2000 years", "not that smart, he likes garbage")

from human import Human

Trent = Human("Trent", "Bauer", 28, "Flagstaff AZ", True)