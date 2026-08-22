trein_massa = 22680
trein_versnelling = 10
trein_afstand = 100
bom_massa = 1
c = 3 * 10 ** 8


f_temp = 0

def f_naar_c(f_temp):
    formule_f_naar_c = (f_temp - 32) * 5/9
    return formule_f_naar_c

f100_in_celsius = f_naar_c(100)

c_temp = 0
def c_naar_f(c_temp):
    formule_c_naar_f = c_temp * (9/5) + 32
    return formule_c_naar_f

c0_in_fahrenheit = c_naar_f(0)
print(c0_in_fahrenheit)



def bereken_kracht(massa, versnelling):
    kracht = massa * versnelling
    return kracht


trein_kracht = bereken_kracht(trein_massa, trein_versnelling)
print("De GE-trein levert", trein_kracht, "Newton aan kracht..")


def bereken_energie(massa, c):
    return massa * c * c

print("Een bom van 1 kg levert", bereken_energie(bom_massa, c), "Joule aan energie..")


def bereken_arbeid(massa, versnelling, afstand):
    arbeid = bereken_kracht(massa, versnelling) * afstand
    return arbeid

trein_arbeid = bereken_arbeid(trein_massa, trein_versnelling, trein_afstand)
print("De GE-trein verricht", trein_arbeid, "Joule aan arbeid over", trein_afstand, "meter.")