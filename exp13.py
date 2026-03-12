from collections import Counter
 
reviews = [
    "This product is very good",
    "Good quality and good price",
    "Product quality is excellent",
    "Very good product"
]

text = " ".join(reviews).lower()

words = text.split()

word_freq = Counter(words)

print("Word Frequency Distribution:\n")
for word, count in word_freq.items():
    print(word, ":", count)
