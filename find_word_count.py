filepath = 'Word Count\paragraph.txt'


def paragraph_to_list(filepath):
    with open(filepath, 'r') as f_obj:
        lines = f_obj.readlines()

    special_characters = ['.', ' ', '', ',', '!', '?', '-', '(', ')', '\n']
    words_in_the_paragraph = []
    word = []

    for line in lines:
        for letter in line:
            if letter not in special_characters:
                word.append(letter)
            elif letter in special_characters:
                words_in_the_paragraph.append("".join(word))
                word.clear()

    return len(words_in_the_paragraph)


print(paragraph_to_list(filepath))
