"""Denda kalkulagailuaren fitxategi nagusia."""

import cart

if __name__ == "__main__":
    erosketa = ["apple", "bread", "milk", "apple"]
    guztizkoa = cart.calculate_total(erosketa)
    print(f"Ordaindu beharreko guztizkoa: {guztizkoa}")
