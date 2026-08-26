def letter_check(woord, letter):
    for char in woord:
        if char == letter:
            return True
    return False

print(letter_check("aardbei", "a"))
print(letter_check("aardbei", "o"))
