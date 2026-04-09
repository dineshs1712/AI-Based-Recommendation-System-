

def get_movies(genre):
    data = {
        "action": ["Avengers", "Batman"],
        "comedy": ["Mr. Bean", "The Mask"],
        "horror": ["Conjuring", "Annabelle"]
    }
    return data.get(genre, [])


def get_food(food_type):
    data = {
        "veg": ["Idli", "Dosa"],
        "nonveg": ["Chicken Biryani", "Fish Fry"]
    }
    return data.get(food_type, [])


def get_games(game_type):
    data = {
        "indoor": ["Chess", "Carrom"],
        "outdoor": ["Cricket", "Football"]
    }
    return data.get(game_type, [])


def display(items, title):
    if items:
        print(f"\nRecommended {title}:")
        for item in items:
            print("-", item)
    else:
        print("No recommendation found")


def main():
    print("===== AI Recommendation System =====")
    print("1. Movies")
    print("2. Food")
    print("3. Games")

    choice = input("Select option: ")

    if choice == "1":
        genre = input("Enter genre (action/comedy/horror): ").lower()
        result = get_movies(genre)
        display(result, "Movies")

    elif choice == "2":
        food_type = input("Enter type (veg/nonveg): ").lower()
        result = get_food(food_type)
        display(result, "Food")

    elif choice == "3":
        game_type = input("Enter type (indoor/outdoor): ").lower()
        result = get_games(game_type)
        display(result, "Games")

    else:
        print("Invalid option")

    print("\nThank you for using the system")
    
    
if __name__ == "__main__":
    main()