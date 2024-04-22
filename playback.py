def main():
    message = input("What do you want to tell the world? ",)
    slow_down(message)

def slow_down(message="Gotta go fast!"):
    print(message.replace(" ", "..."))

main()
