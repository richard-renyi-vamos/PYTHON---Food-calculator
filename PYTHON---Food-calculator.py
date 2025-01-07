class VeganFood:
    def __init__(self, name, calories, protein, fat, carbs):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

# Database of vegan foods
VEGAN_FOODS = {
    "tofu": VeganFood("Tofu", 144, 15, 8, 4),
    "lentils": VeganFood("Lentils", 230, 18, 1, 40),
    "quinoa": VeganFood("Quinoa", 222, 8, 4, 39),
    "almonds": VeganFood("Almonds", 164, 6, 14, 6),
    "broccoli": VeganFood("Broccoli", 55, 5, 0, 11),
    "spinach": VeganFood("Spinach", 23, 3, 0, 4),
    "avocado": VeganFood("Avocado", 240, 3, 22, 12),
    "oats": VeganFood("Oats", 154, 6, 3, 27),
    "banana": VeganFood("Banana", 105, 1, 0, 27),
    "chickpeas": VeganFood("Chickpeas", 269, 15, 4, 45),
}

def display_foods():
    print("\nAvailable Vegan Foods:")
    for name, food in VEGAN_FOODS.items():
        print(f"- {name.title()} (Calories: {food.calories}, Protein: {food.protein}g, Fat: {food.fat}g, Carbs: {food.carbs}g)")

def main():
    print("Welcome to the Vegan Food Diet Calculator!\n")

    total_calories = 0
    total_protein = 0
    total_fat = 0
    total_carbs = 0

    while True:
        display_foods()
        choice = input("\nEnter a food name to add to your diet (or type 'done' to finish): ").strip().lower()

        if choice == "done":
            break

        if choice in VEGAN_FOODS:
            quantity = float(input(f"Enter quantity of {choice.title()} in grams: "))
            food = VEGAN_FOODS[choice]

            total_calories += (food.calories / 100) * quantity
            total_protein += (food.protein / 100) * quantity
            total_fat += (food.fat / 100) * quantity
            total_carbs += (food.carbs / 100) * quantity

            print(f"Added {quantity}g of {choice.title()} to your diet.")
        else:
            print("Food not found. Please choose from the list.")

    print("\nDaily Nutritional Summary:")
    print(f"- Total Calories: {total_calories:.2f} kcal")
    print(f"- Total Protein: {total_protein:.2f} g")
    print(f"- Total Fat: {total_fat:.2f} g")
    print(f"- Total Carbohydrates: {total_carbs:.2f} g")

if __name__ == "__main__":
    main()
