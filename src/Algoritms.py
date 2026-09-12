
def line(base_text, base_stop_word):
    clear_text = []
    base_text_list = base_text.split()
    for word in base_text_list:
        if word not in base_stop_word:
            clear_text.append(word)
    return clear_text
def binary(base_text, base_stop_word):
    clear_text = []
    base_stop_word_sorted = sorted(base_stop_word)

    def if_stop_word(word):
        low = 0
        high = len(base_stop_word_sorted) - 1
        while low <= high:
            middle = (low + high) // 2
            if word == base_stop_word_sorted[middle]:
                return True
            elif word < base_stop_word_sorted[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return False

    for word in base_text.split:
        if not if_stop_word(word):
            clear_text.append(word)
    return clear_text
def hash(base_text, base_stop_word):
    clear_text = []
    return clear_text