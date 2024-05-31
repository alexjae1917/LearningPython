def second_index(text: str, some_str: str) -> int or None:
    indexx = text.index(some_str) + 1
    if text.count(some_str) < 2:
        return None
    return text[indexx:].index(some_str)+indexx


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
