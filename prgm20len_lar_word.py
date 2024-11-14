num_elements = int(input("Enter the number of words: "))

# Step 2: Accept the values into the list
words = []
for _ in range(num_elements):
    word = input("Enter a word: ")
    words.append(word)

# Step 3: Assume the first word is the largest
largest_word = words[0]

# Step 4: Use a for loop to compare lengths of the words
for word in words:
    if len(word) > len(largest_word):
        largest_word = word

# Step 5: Display the word with the longest length
print(f"The largest word is '{largest_word}' with length {len(largest_word)}.")