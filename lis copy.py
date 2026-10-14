palavras = ["maca", "banana", "abacaxi", "uva"]

def is_long_word(word):

    return len(word) > 6

palavras_longas = filter(is_long_word, palavras)

print(list(palavras_longas)) # Saida: ["abacaxi"]