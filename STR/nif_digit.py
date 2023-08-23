# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    remainder_number = int(nif) % 23
    letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
    control_digit = letters[remainder_number]
    wnif = nif + control_digit

    return wnif


if __name__ == '__main__':
    run('78654355')