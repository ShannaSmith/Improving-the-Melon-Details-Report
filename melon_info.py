"""Print out all the melons in our inventory."""


from melons import melons


# def print_melon(name, price, seedless, flesh_color, rind_color, avaerage_weight):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])


def print_all_melons(melons):
    for melon_name, info in melons.items():
        print(melon_name.upper())
        for info, value in info.items():
            print(f'{info}: {value}')

print_all_melons(melons)