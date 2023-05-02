def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f'{i}. {dwarf}')
        i += 1

def summon_captain_planet(planeteer_calls):
    return [call.title() + '!' for call in planeteer_calls]

def long_planeteer_calls(words):
    for call in words:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ("cheddar", "gouda", "camembert")
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None
