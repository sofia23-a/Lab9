def encode(password):
    new = ""
    for i in password:
        new += str(int(i) + 3)
    return new

