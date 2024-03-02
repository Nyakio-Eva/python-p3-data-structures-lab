spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods if "name" in food]

print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):

    dictionaries = []

    for food in spicy_foods:
        #check if there is a heat level key and if it's value is greater than 5
        if "heat_level" in food and food["heat_level"] > 5:
            dictionaries.append(food)

    return dictionaries   

print (get_spiciest_foods(spicy_foods))     


def print_spicy_foods(spicy_foods):
    #itearte over all the dictionaries
    for food in spicy_foods:
        #access keys in each dictionary using dictionary indexing
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        #create a string of emojis for heat level
        heat_emojis = "🌶" * heat_level
        #use string formating to print
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}") 

print_spicy_foods(spicy_foods)           
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #iterate over all dictionaries
    for food in spicy_foods:
        #retrieve the value of cuisine key using get()
        food_cuisine = food.get("cuisine", "please enter a valid cuisine")

        #check if cuisine retrieved matches the cuisine in func call
        if food_cuisine == cuisine:
            return food
        
    return food_cuisine
    
print(get_spicy_food_by_cuisine(spicy_foods,"American") ) 
print(get_spicy_food_by_cuisine(spicy_foods, "Thai") )             

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        if food["heat_level"] > 5:
            heat_emojis = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}") 
print_spiciest_foods(spicy_foods)           

def get_average_heat_level(spicy_foods):
    total_heat_level = 0  #initialize total heat level to 0 to keep track of sum of all heat levels
    num_spicy_foods = len(spicy_foods)
    for food in spicy_foods:
        food_heat_level = food.get("heat_level")
        total_heat_level += food_heat_level  #add heat levels for each food to the total
        
    if num_spicy_foods > 0:
        average_heat_level = total_heat_level / num_spicy_foods
        return int(average_heat_level)

print(get_average_heat_level(spicy_foods)) 

def create_spicy_food(spicy_foods,new_spicy_food):
    new_list = spicy_foods.copy()

    new_list.append(new_spicy_food)
    return new_list

print(create_spicy_food(spicy_foods, new_spicy_food={"name": "Griot","cuisine": "Haitian","heat_level": 10}))   
