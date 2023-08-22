# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    lost_word = text.find(target_word)
    word_len = len(target_word)
    text_first_part = text[:lost_word]
    second_part = lost_word + word_len
    text_second_part = text[second_part:]
    
    
    
    mtext = text_first_part + replace_word + text_second_part

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')