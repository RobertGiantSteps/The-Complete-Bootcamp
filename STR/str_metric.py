# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    lower_text = text.lower()
    total_characters = len(text)
    metric = total_characters * vowels

    return metric


if __name__ == '__main__':
    run('ordenador')