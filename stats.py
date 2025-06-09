def count_words(text):
    words = text.split()
    return len(words)

def count_letters(book):
    letter_counter = {}
    for character in list(book):
        ch = character.lower()
        if ch in letter_counter:
            letter_counter[ch] += 1
        else:
            letter_counter[ch] = 1
    return letter_counter

def get_sorted_key_counter_pairs(unsorted):
    pairs = []
    for key in unsorted:
        pairs.append({"char": key, "num": unsorted[key]})
    pairs.sort(reverse=True, key=sort_on)
    return pairs

def sort_on(dict):
    return dict["num"]