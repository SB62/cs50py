fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 50,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

def main():
    user_input = input("Item: ")
    if check_fruits(user_input):
        print(f'Calories: {check_fruits(user_input)}')
    else:
        exit()


def check_fruits(fruit):
    if fruit.lower() in fruits:
        return fruits[fruit.lower()]

if __name__ == "__main__":
    main()
