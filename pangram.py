def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World"))
print(is_pangram("Sphinx of black quartz, judge my vow"))