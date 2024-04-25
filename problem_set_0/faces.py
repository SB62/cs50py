def main():
    message = input("How are you feeling today? (Answer with a :) or a :( and why you're feeling that way.) ")
    print(convert(message))

def convert(feels="Don't feel anything?"):
    if ':)' in feels:
        feels = feels.replace(":)", "🙂")
    if ':(' in feels:
        feels = feels.replace(":(", "🙁")

    return feels


main()
