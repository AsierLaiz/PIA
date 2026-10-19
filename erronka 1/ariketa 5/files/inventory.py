"""Produktuen inbentarioa eta prezioak kudeatzeko modulua."""

produktuak = {"apple": 0.5, "bread": 1.2, "milk": 0.9}


def price(product):
    """Produktu baten prezioa itzultzen du, edo mezu bat produktua ez badago aurkitzen."""
    return produktuak.get(product, "Produktua ez da aurkitu")
