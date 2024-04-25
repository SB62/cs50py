def main():
    message = input("What message would you like to shout to the world? (USE ALL CAPS!)")
    shush(message)

def shush(msg="Guess you don't have much to say..."):
    print(msg.lower())

main()
