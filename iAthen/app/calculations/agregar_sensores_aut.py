def calculate(params):
    # Extract vet1, vet2, and vet3 from the params dictionary
    vet1 = params.get('vet1')
    vet2 = params.get('vet2')
    vet3 = params.get('vet3')

    if not (vet1 and vet2 and vet3):
        return "Missing vectors 'vet1', 'vet2', or 'vet3'"

    resultado = []
    ncolunas_vet = len(vet1)

    # Ensure all vectors have the same number of columns
    if ncolunas_vet == len(vet2) == len(vet3):

        # Initialize the result array
        for i in range(ncolunas_vet):
            linha = [0.0]
            resultado.append(linha)


        # Calculate the maximum for each column
        for i in range(ncolunas_vet):
            resultado[i] = max(vet1[i], vet2[i], vet3[i])

        # Get the fuzzy output (max value in resultado)
        fuzzysaida = max(resultado)

        # Update resultado based on fuzzy output
        for i in range(ncolunas_vet):
            if resultado[i] == fuzzysaida:
                resultado[i] = 1
            else:
                resultado[i] = 0

        return resultado

    else:
        return "O número de colunas e de linhas são de tamanhos diferentes. (func agregar_sensores_aut)"
