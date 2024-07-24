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
