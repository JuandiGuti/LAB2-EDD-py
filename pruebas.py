contexto = [ "Parker Inc", "Conn - Huels", "Hickle, Ziemann and Legros", "Nolan LLC", "McDermott, Cummerata and Thompson", "Welch - Shields", "O'Hara and Sons", "Parisian, Gleichner and Collins", "Moore and Sons", "Gottlieb - Sporer", "Schiller, Fadel and Gislason", "Rowe LLC", "Tremblay Inc", "Schuppe, D'Amore and Hilpert", "Dickinson - Nikolaus", "Vandervort - Weimann", "Jenkins - Douglas", "Lind Inc", "Connelly - Swaniawski", "Block and Sons", "Emard LLC", "Daugherty Group", "Hermiston, Lakin and Jacobi", "Swift - Volkman", "Wunsch LLC", "Witting - Becker", "Jones, Grady and Breitenberg", "Ziemann - Borer", "Upton LLC", "Barrows and Sons", "Maggio LLC", "Daniel - Franey", "Stehr - Langosh", "Gaylord, Schiller and Murray", "Pollich and Sons", "Schuster, Olson and Doyle", "Turner LLC", "Jacobs - Farrell", "Lakin - Altenwerth", "Mante - Lesch", "Kub and Sons", "Mayer, Block and Gaylord", "Pagac - Bosco", "Wisozk - Strosin", "Cassin, Kreiger and McKenzie", "Corkery - Rosenbaum", "Marvin - Legros", "Gislason Group", "Mertz, Casper and Hirthe", "Ziemann and Sons" ]

def obtener_numero_codificacion(companies):
    return sum([contexto.index(compania) for compania in companies if compania in contexto])

def codificar(dpi, companies):
    numero_codificacion = obtener_numero_codificacion(companies)
    # Convertir ambos números a binario y luego a XOR
    bin_dpi = bin(dpi)[2:]  # [2:] para quitar el '0b' inicial
    bin_numero_codificacion = bin(numero_codificacion)[2:]

    # Asegurarse de que ambos tengan la misma longitud, rellenando con ceros
    max_len = max(len(bin_dpi), len(bin_numero_codificacion))
    bin_dpi = bin_dpi.zfill(max_len)
    bin_numero_codificacion = bin_numero_codificacion.zfill(max_len)

    # Realizar la operación XOR
    bin_codificado = ''.join(['1' if a != b else '0' for a, b in zip(bin_dpi, bin_numero_codificacion)])
    
    # Convertir de nuevo a entero
    return int(bin_codificado, 2)

def decodificar(dpi_codificado, companies):
    # Dado que XOR es su propia inversa, podemos usar la misma función para decodificar
    return codificar(dpi_codificado, companies)

dpi_codificado = codificar(persona['dpi'], persona['companies'])
print(f"dpi codificado: {dpi_codificado}")

dpi_decodificado = decodificar(dpi_codificado, persona['companies'])
print(f"dpi decodificado: {dpi_decodificado}")

