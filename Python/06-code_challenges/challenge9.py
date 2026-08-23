def film_review(rating):
    if rating <= 5:
        return "Ontwijk ten alle kosten!"
    elif rating < 9:
        return "Deze film was leuk."
    else:
        return "Fantastisch!"

# Zou "Fantastisch!" moeten printen
print(film_review(9))

# Zou "Ontwijk ten alle kosten!" moeten printen
print(film_review(4))

# Zou "Deze film was leuk." moeten printen
print(film_review(6))