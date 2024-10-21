def calculate(params):
    # Extract vet1, vet2, vet3, vet4, vet5 from the params dictionary
    vet1 = params.get('vet1')
    vet2 = params.get('vet2')
    vet3 = params.get('vet3')
    vet4 = params.get('vet4')
    vet5 = params.get('vet5')

    # Ensure all vectors are provided
    if not (vet1 and vet2 and vet3 and vet4 and vet5):
        return "Missing vectors 'vet1', 'vet2', 'vet3', 'vet4', or 'vet5'"

    resultado = []
    need = []

    # Get dimensions
    ncolunas_vet = len(vet1[0])
    nlinhas_vet = len(vet1)

    # Ensure all vectors have the same dimensions
    if ncolunas_vet == len(vet2[0]) == len(vet3[0]) == len(vet4[0]) == len(vet5[0]):

        # Initialize resultado with zeros
        for i in range(nlinhas_vet):
            linha = [0.0] * ncolunas_vet
            resultado.append(linha)

        # Calculate the maximum for each element
        for i in range(nlinhas_vet):
            for j in range(ncolunas_vet):
                resultado[i][j] = max(vet1[i][j], vet2[i][j], vet3[i][j], vet4[i][j], vet5[i][j])

        # Find the column index with the maximum value in the first row of resultado
        fuzzysaida = resultado[0].index(max(resultado[0]))

        # Initialize need with zeros
        for i in range(nlinhas_vet):
            linha = [0.0] * ncolunas_vet
            need.append(linha)

        # Set the corresponding column in the first row of need to 1
        need[0][fuzzysaida] = 1.0

        return need

    else:
        return "O número de colunas e de linhas são de tamanhos diferentes. (func agregar_sensores_comp)"
