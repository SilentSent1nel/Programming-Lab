def winstpercentage(winst, verlies):
    verhouding = winst / (winst + verlies) * 100
    return verhouding

print(winstpercentage(5, 5))
print(winstpercentage(10, 0))