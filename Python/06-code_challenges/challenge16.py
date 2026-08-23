nums = []

def deelbaar_door_10(nums):
    teller = 0
    for nummer in nums:
        if nummer % 10 == 0:
            teller += 1
    return teller

print(deelbaar_door_10([20, 25, 30, 35, 40]))