def get_num_words(text):
    return len(text.split())

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def num_chars(text):
    character_count = {}
    text = text.lower()
    for i in text:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1

    return character_count


def sort_character_count(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
        char_list.sort(key=lambda x: x["char"])
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

    