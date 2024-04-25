def main():
    salutation = input("Greeting: ")
    print(corpgreeting(salutation))

def corpgreeting(greeting):
    # Normalize Greeting
    greeting = greeting.strip().lower()
    if greeting.startswith('hello'):
        return "$0"
    elif greeting.startswith('h'):
        return "$20"
    else:
        return "$100"

main()
