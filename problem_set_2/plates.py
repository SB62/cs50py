def is_valid_vanity_plate(plate):
    # Check length of the plate
    if not (2 <= len(plate) <= 6):
        return False

    # Check for no periods, spaces, or punctuation marks
    if not plate.isalnum():
        return False

    # Check if the plate starts with at least two letters
    if not plate[:2].isalpha():
        return False

    # Check for the valid placement of numbers
    if any(char.isdigit() for char in plate):
        # Find the first digit in the plate
        first_digit_index = next((i for i, char in enumerate(plate) if char.isdigit()), len(plate))
        # Ensure all characters after the first digit are also digits
        if not plate[first_digit_index:].isdigit():
            return False
        # Ensure the first digit is not '0'
        if plate[first_digit_index] == '0':
            return False

    return True

def main():
    plate = input("Enter a vanity plate: ").strip()
    if is_valid_vanity_plate(plate):
        print(f"VALID")
    else:
        print(f"INVALID")

if __name__ == "__main__":
    main()



"""
    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”
"""
