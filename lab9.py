<<<<<<< HEAD
#hello world
=======
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
>>>>>>> 0e1897299491d6f7acbb9980a3165335f235b722

def encode(password):
    encoded_password = ''
    for char in password:
        encoded_char = str(int(char) + 3)
        encoded_password += encoded_char
    return encoded_password