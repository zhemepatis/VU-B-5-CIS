def friedman_test(text, guessed_length):
    text_length = len(text)

    coincidences = 0
    for i in range(guessed_length, text_length):
        if text[i] == text[i-guessed_length]:
            coincidences = coincidences + 1

    return coincidences / (text_length - guessed_length)