def correct_sentence(text: str) -> str:
    text = text.capitalize()
    res = text.split('. ')
    for i in range(0, len(res)):
        res[i] = res[i].capitalize()
    text = '. '.join(res)
    if text[-1] != '.':
        text += '.'
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
