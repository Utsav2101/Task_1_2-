def word_frequencies(words):
    freq = {}
    for word in words:
        freq[word] = words.count(word)
    return freq

if __name__ == '__main__':
    words = input("Enter youe word here :")
    your_dictionary = word_frequencies(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ':' + str(your_dictionary[key]))

