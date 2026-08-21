huidig_budget = 3500.75
shirt_kosten = 9


def print_resterend_budget(budget):
  print("Je resterende budget is: $" + str(budget))

print_resterend_budget(huidig_budget)

# Schrijf je code hieronder: 

def trek_kosten_af(budget, kosten):

  return budget - kosten

nieuw_budget_na_shirt = trek_kosten_af(huidig_budget, shirt_kosten)
print_resterend_budget(nieuw_budget_na_shirt)