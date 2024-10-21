# app/calculations/autonomia.py

import CalculationsUtils

def calculate(params):
    autonomia_data = params.get('autonomia_data', [])

    if len(autonomia_data) != 7:
        raise ValueError("Invalid data for autonomia. Expected 7 elements.")

    soma = sum(autonomia_data) / 7
    fuzzy_aut = CalculationsUtils.calcfuzzy(soma, 1, 6)

    maior_fuzzy_aut = max(fuzzy_aut)
    for i in range(len(fuzzy_aut)):
        fuzzy_aut[i] = 1 if fuzzy_aut[i] == maior_fuzzy_aut else 0

    return fuzzy_aut
