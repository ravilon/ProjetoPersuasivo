# app/calculations/afinidade.py

import CalculationsUtils

def calculate(params):
    afinidade_data = params.get('afinidade_data', [])

    if len(afinidade_data) != 8:
        raise ValueError("Invalid data for afinidade. Expected 8 elements.")

    soma = sum(afinidade_data) / 8
    fuzzy_afin = CalculationsUtils.calcfuzzy(soma, 1, 6)

    maior_fuzzy_afin = max(fuzzy_afin)
    for i in range(len(fuzzy_afin)):
        fuzzy_afin[i] = 1 if fuzzy_afin[i] == maior_fuzzy_afin else 0

    return fuzzy_afin
