# app/calculations/competencia.py

import CalculationsUtils

def calculate(params):
    competencia_data = params.get('competencia_data', [])

    if len(competencia_data) != 6:
        raise ValueError("Invalid data for competencia. Expected 6 elements.")

    soma = sum(competencia_data) / 6
    fuzzy_comp = CalculationsUtils.calcfuzzy(soma, 1, 6)

    maior_fuzzy_comp = max(fuzzy_comp)
    for i in range(len(fuzzy_comp)):
        fuzzy_comp[i] = 1 if fuzzy_comp[i] == maior_fuzzy_comp else 0

    return fuzzy_comp
