"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, melon_flesh_color, melon_rind_color, melon_average_weight


def print_melon(name, price, seedless, flesh_color, rind_color, avaerage_weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price}')


for i in melon_names:
    print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
