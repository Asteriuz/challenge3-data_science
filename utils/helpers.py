def format_float(value):
    """Formata números com ponto como separador de milhares e vírgula como decimal"""
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_integer(value):
    """Formata inteiros com ponto como separador de milhares"""
    return f"{value:,}".replace(",", ".")
