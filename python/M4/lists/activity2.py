# Activity 2: Word Matching

words = ["level", "apple", "madam", "python", "radar", "hello"]
count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        print(word, "matches!")
        count += 1

print("Total matching words:", count)
