def twee_keer_zo_groot(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False

print(twee_keer_zo_groot(20, 10))
# Zou "False" moeten printen
print(twee_keer_zo_groot(11, 5))
# Zou "True" moeten printen