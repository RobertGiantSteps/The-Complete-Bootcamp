# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    split_cleaning = html.lstrip('<')
    h_number = split_cleaning.partition('>')
    rigth_strip = h_number[0]
    left_strip = h_number[2]
    left_partition = left_strip.partition('<')
    message = left_partition[0]
    md_number = rigth_strip.lstrip('h')
    caracter_md = '#' * int(md_number)
    
    markdown = f'{caracter_md} {message}'

    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')