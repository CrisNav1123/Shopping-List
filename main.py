from contents import pantry, recipes


shopping_list = {}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index+1)] = key

# Displays recipe ingredient requirements, adds missing qty to shopping_list
def meal_plan():
    while True:
        # Display menu of recipes
        print("\nPlease choose your recipe")
        print("-------------------------")
        for key, value in display_dict.items():
            print(f"{key} - {value}")
        print("\n0 - Exit")
        choice = input(">")

        if choice == "0":
            break
        # Lists availability of ingredients
        elif choice in display_dict:
            selected_item = display_dict[choice]
            print(f"You have selected {selected_item}")
            print("Checking ingredients...")
            ingredients = recipes[selected_item]
            print(ingredients)
            for food_item, required_quantity in ingredients.items():
                quantity_in_pantry = pantry.get(food_item, 0)
                if required_quantity <= quantity_in_pantry:
                    print(f"\t{food_item} OK")
                else:
                #Adds missing ingredients to shopping_list
                    quantity_to_buy = required_quantity - quantity_in_pantry
                    quantity_to_buy += shopping_list.get(food_item, 0)
                    print(f"\tYou need to buy {quantity_to_buy} of {food_item}")     
                    shopping_list[str(food_item)] = quantity_to_buy

# Displays shopping_list
def get_shop_list():
    print("\nShopping list")
    print("-------------")
    if shopping_list:
        for food_item, quantity_to_buy in shopping_list.items():
            print(f"{food_item}: {quantity_to_buy}")
        print('\n')
    else:
        print("You have no items in the list.\n")


if __name__ == "__main__":
    while True:
        print("Choose option")
        print("------------------")
        print("1. Plan Meal")
        print("2. Show shopping list")
        print("3. Exit program")
        choice = int(input(">"))
        if choice == 3:
            break
        elif choice == 1: 
            meal_plan()
        elif choice == 2:
            get_shop_list()