txt = "Hello all. Here's pretty cold and hot. Choose yourself."

sentences = txt.split(". ")
words_in_sentences = []
for i in sentences:
    words_in_sentences.append(len(i.split()))

print(words_in_sentences)
