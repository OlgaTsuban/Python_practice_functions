def strings(string: str) -> dict:
    codes = {}
    for char in string:
        if char not in codes:
            codes[char] = ord(char)
    return codes

print(strings("hello"))
