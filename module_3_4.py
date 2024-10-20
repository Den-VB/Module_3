# Задача "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])
        elif other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
    print(same_words)

single_root_words('rich', 'Ri', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'DisaBlemenTino', 'Able', 'Mable', 'Disable', 'Bagel')
