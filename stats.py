def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    list = text.split()
    return len(list)

def character_count(text):
    dict = {}
    for i in text:
        i = i.lower()
        if i in dict:
            dict[i] += 1
        else:
            dict.update({i:1})
    return dict

def find_value(x):
    return x["num"]

def character_sort(dict):
    list = []
    for i in dict:
        x = dict[i]
        if i.isalpha():
            list.append({"char": i, "num": x})
    list.sort(reverse=True, key=find_value)
    return list
