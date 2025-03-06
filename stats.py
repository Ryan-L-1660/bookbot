def get_num_words(text):
    return len(text.split())

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def num_chars(text):
    characterCount = {}
    for i in text:
        i = i.lower()
        if i in characterCount:
            characterCount[i] += 1
        else:
            characterCount[i] = 1

    return characterCount


def sort_character_count(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

    