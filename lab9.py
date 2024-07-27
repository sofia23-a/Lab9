
def decode(password):
    new = ""
    for i in password:
        if i == "0":
            new += "7"
        elif i == "1":
            new += "8"
        elif i == "2":
            new += "9"
        else:
            new += str(int(i) - 3)

    return new


def encode(password):
    encoded_password = ''
    for char in password:
        encoded_char = str(int(char) + 3)
        encoded_password += encoded_char
    return encoded_password

def main():
    stored_password = ''

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        try:
            option = int(input("\nPlease enter an option: "))

            if option == 1:
                password = input("Please enter the password to encode: ")
                stored_password = encode(password)
                print("Your password has been encoded and stored!")

            elif option == 2:
                if stored_password:
                    original_password = decode(stored_password)
                    print(
                        f"The encoded password is {stored_password}, and the original password is {original_password}.")
                else:
                    print("Please encode a password first.")

            elif option == 3:
                print("Exiting...")
                break

            else:
                print("Invalid option. Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()