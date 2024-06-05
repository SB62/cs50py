def main():
    user_input = input("Input: ")
    print(f'Output: {cap_scrubber(user_input)}')

def cap_scrubber(word):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    scrubbed_word = ''

    for letter in word:
        if letter in vowels:
            continue
        else:
            scrubbed_word += letter
    return scrubbed_word

if __name__ == "__main__":
    main()
