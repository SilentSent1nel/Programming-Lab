def deelbaar_door_10(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(deelbaar_door_10(20))
# Zou "True" moeten printen

print(deelbaar_door_10(25))
# Zou "False" moeten printen