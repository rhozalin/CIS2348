# Name-Rhozalin Nath
# PS ID: 2050395

class FoodItem:

    def __init__(self, item_name="None", amount_fat=0.0, amount_carbs=0.0, amount_protein=0.0):
        self.name = item_name
        self.fat = amount_fat
        self.carbs = amount_carbs
        self.protein = amount_protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')


if __name__ == "__main__":
    food_item1 = FoodItem()
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    num_servings = float(input())
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item1.get_calories(num_servings)))
    print()
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item2.get_calories(num_servings)))
