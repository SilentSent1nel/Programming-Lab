def in_bereik(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

print(in_bereik(10, 10, 10))
# Zou "True" moeten printen

print(in_bereik(5, 10, 20))
# Zou "False" moeten printen