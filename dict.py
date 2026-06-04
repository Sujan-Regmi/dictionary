lines = [
    "apple banana apple",
    "banana cherry banana",
    "apple cherry cherry cherry"
]

word_count = {}

for sentence in lines:
    words = sentence.split()   # split sentence into words
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)