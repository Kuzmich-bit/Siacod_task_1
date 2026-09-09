def line(base_text, base_stop_word):
    clear_text = []
    base_text = base_text.split()
    for word in base_text:
        if word not in base_stop_word: #можно перевести в список наверно, но я так понимаю потеряем скорость
            clear_text.append(word)
    print(clear_text)
