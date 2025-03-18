import string

def popular_words (text, words):
    for punctuation in string.punctuation:
        if punctuation in text:
            text = text.replace(punctuation, "")
    text = text.lower().split(" ")
    voc = {}
    for word in words:
        voc[word] = text.count(word)
    return voc
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
assert popular_words("", ["word", "test"]) == {"word": 0, "test": 0}
print('OK')