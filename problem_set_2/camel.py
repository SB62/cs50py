def main():
    user_string = input("What's your variable name? ")
    print(camel_to_snake(user_string))


def camel_to_snake(camel_case):
  snake_case = ""
  for char in camel_case:
    if char.isupper() and snake_case:
      snake_case += "_"
    snake_case += char.lower()
  return snake_case

if __name__ == "__main__":
    main()
