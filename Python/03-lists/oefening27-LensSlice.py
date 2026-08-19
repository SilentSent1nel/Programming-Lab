toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prijzen = [2, 6, 1, 3, 2, 7, 2]

aantal_twee_dollar_plakken = prijzen.count(2)
print(aantal_twee_dollar_plakken)

aantal_pizzas = len(toppings)
print(aantal_pizzas)

print("We sell", aantal_pizzas, "different kinds of pizza!")
pizza_en_prijzen = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_en_prijzen)

pizza_en_prijzen.sort()
print(pizza_en_prijzen)

goedkoopste_pizza = pizza_en_prijzen[0]
print(goedkoopste_pizza)

duurste_pizza = pizza_en_prijzen[-1]
print(duurste_pizza)

pizza_en_prijzen.pop()
print(pizza_en_prijzen)

pizza_en_prijzen.insert(5, [2.5, "peppers"])
print(pizza_en_prijzen)

drie_goedkoopste = pizza_en_prijzen[0:4]
print(drie_goedkoopste)