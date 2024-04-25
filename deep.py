def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    print(check_answer(answer))

def check_answer(input):
    # Normalize Input
    input = input.strip().lower().replace("-", " ")

    if input == "42" or input == "forty two":
        return "Yes"
    else:
        return "No"

main()
