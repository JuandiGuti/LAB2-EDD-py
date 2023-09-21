contexto = [ "Parker Inc", "Conn - Huels", "Hickle, Ziemann and Legros", "Nolan LLC", "McDermott, Cummerata and Thompson", "Welch - Shields", "O'Hara and Sons", "Parisian, Gleichner and Collins", "Moore and Sons", "Gottlieb - Sporer", "Schiller, Fadel and Gislason", "Rowe LLC", "Tremblay Inc", "Schuppe, D'Amore and Hilpert", "Dickinson - Nikolaus", "Vandervort - Weimann", "Jenkins - Douglas", "Lind Inc", "Connelly - Swaniawski", "Block and Sons", "Emard LLC", "Daugherty Group", "Hermiston, Lakin and Jacobi", "Swift - Volkman", "Wunsch LLC", "Witting - Becker", "Jones, Grady and Breitenberg", "Ziemann - Borer", "Upton LLC", "Barrows and Sons", "Maggio LLC", "Daniel - Franey", "Stehr - Langosh", "Gaylord, Schiller and Murray", "Pollich and Sons", "Schuster, Olson and Doyle", "Turner LLC", "Jacobs - Farrell", "Lakin - Altenwerth", "Mante - Lesch", "Kub and Sons", "Mayer, Block and Gaylord", "Pagac - Bosco", "Wisozk - Strosin", "Cassin, Kreiger and McKenzie", "Corkery - Rosenbaum", "Marvin - Legros", "Gislason Group", "Mertz, Casper and Hirthe", "Ziemann and Sons" ]

def obtener_numero_codificacion(companies):
    return sum([contexto.index(compania) for compania in companies if compania in contexto])

def codificar(dpi, companies):
    numero_codificacion = obtener_numero_codificacion(companies)
    
    # Codificar el DPI usando XOR con el número de codificación
    dpi_codificado = int(dpi) ^ numero_codificacion
    
    # Añadir el número de codificación al final del DPI codificado para usarlo en la decodificación
    return int(str(dpi_codificado) + str(numero_codificacion).zfill(4))

def decodificar(dpi_codificado_con_info):
    # Extraer el número de codificación del final del DPI
    numero_codificacion = int(str(dpi_codificado_con_info)[-4:])
    
    # Extraer el DPI codificado sin la información añadida
    dpi_codificado = int(str(dpi_codificado_con_info)[:-4])
    
    # Decodificar usando XOR
    return dpi_codificado ^ numero_codificacion

# Ejemplo de uso:
persona = {
    "name": "dennis",
    "dpi": "4981559841093",
    "datebirth": "1974-05-02T01:29:03.706Z",
    "address": "cambridge",
    "companies": ["Hermiston, Lakin and Jacobi","Parker Inc","Hickle, Ziemann and Legros", "Conn - Huels"]
}

dpi_codificado = codificar(persona['dpi'], persona['companies'])
print(f"dpi codificado: {dpi_codificado}")

dpi_decodificado = decodificar(dpi_codificado)
print(f"dpi decodificado: {dpi_decodificado}")


