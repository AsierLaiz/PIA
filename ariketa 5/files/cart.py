"""Erosketa-saskiaren guztizko zenbatekoa kalkulatzeko modulua."""

import inventory


def calculate_total(product_list):
    """Produktu-zerrenda baten prezioen batura kalkulatzen du, aurkitzen ez diren produktuak alde batera utziz."""
    guztizkoa = 0
    for produktua in product_list:
        prezioa = inventory.price(produktua)
        if isinstance(prezioa, str):
            print(f"Abisua: {produktua} ez da aurkitu, alde batera utzi da.")
            continue
        guztizkoa += prezioa
    return guztizkoa
