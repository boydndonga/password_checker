
def validity(password):
    special_char = ["$", "#", "@"]

    if len(password) < 6 or len(password) > 12:
        return False
    for i in range(len(password)):
        if password[i] in special_char:
            return True
    return False
