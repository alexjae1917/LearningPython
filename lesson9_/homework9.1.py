import string


def valid(char):
    if char in string.punctuation:
        return False
    return True


def popular_words (text: str, words: list) -> dict:
    result = {}
    clear_text = filter(valid, text)
    text = ''.join(list(clear_text))
    text = text.lower().split()
    for i in words:
        counter = text.count(i)
        result.update({i: counter})

    return result




#popular_words('When I was One I had !just begun When I was Two, I was nearly new',['i','was'] )
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 },'Test 1'