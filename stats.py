def get_count_characters(text):
    characters_dict = {}
    for i in text:
        i = i.lower()
        if i in characters_dict:
            characters_dict[i] += 1
        else: 
            characters_dict[i] = 1
    return characters_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def report_sort(characters_dict):
    liste =[]
    for k,v in characters_dict.items():
        liste.append({"character": k , "value" : v})
    liste = sorted(liste, key = lambda x : x ["value"], reverse=True )
    return liste