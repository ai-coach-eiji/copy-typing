sentence = "Life is short, eat dessert first"

dc = {s: i for i, s in enumerate(sorted(sentence.replace(",", "").split()))}
print("vocabulary: ", dc)