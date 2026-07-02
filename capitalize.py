def solve(s):
    words = s.split(" ")
    capitalized_words = []

    for word in words:
        if word:
            capitalized_words.append(word[0].upper() + word[1:])
        else:
            capitalized_words.append(word)

    return " ".join(capitalized_words)


# Example
print(solve("chris alan"))  # Output: Chris Alan
print(solve("hello world"))  # Output: Hello World