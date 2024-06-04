import string



def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = list(text)
    for i in text:
        if i in string.punctuation:
            text.remove(i)

    text = ''.join(''.join(text).split())

    rev = text[::-1]
    if text == rev:
        return True
    return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
