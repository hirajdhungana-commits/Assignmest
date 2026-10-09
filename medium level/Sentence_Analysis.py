sentence = input("Enter a sentence: ")
words = sentence.lower().split()
clean_sentence = " ".join(words)

total_words = len(words)
python_count = words.count("python")

if total_words >0:
    longest_word = max(words, key=len)
else:
    longest_word = "No words"

print("Clean sentence:", clean_sentence)
print("Total words:", total_words)
print("Times 'python' appears :", python_count)
print("Longest word:",longest_word)
