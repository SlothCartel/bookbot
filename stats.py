def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    output = {}

    for ch in text.lower():
        if ch in output:
            output[ch] += 1
        else:
            output[ch] = 1

    return output

def sort_dict(chars):
    output = []


    for key, value in chars.items():
        dict_list = {}
        dict_list["char"] = key
        dict_list["num"] = value
        output.append(dict_list)

    output.sort(key=lambda x: x["num"], reverse=True)
    return output
