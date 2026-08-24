lijst = []


def boven_9000(lijst):
    som = 0
    for num in lijst:
        som = num + som
        if som > 9000:
            return som
    return som

print(boven_9000([8000, 900, 120, 5000]))